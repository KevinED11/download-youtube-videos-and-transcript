from pathlib import Path


from pytube import YouTube
from pytube.exceptions import PytubeError
from unidecode import unidecode


def get_videos(url_list: list[str]) -> list[YouTube]:
     if not url_list:
         raise ValueError("List of url is empty")
     
     return [YouTube(url=link) for link in url_list]
    

def save_video_in_path(path: str | Path = "downloads") -> Path:
    dest_path: Path = Path(Path.cwd()/path).resolve()

    if not dest_path.is_dir():
         dest_path.mkdir(parents=True)

    return dest_path


def get_video_information(video_list: list[YouTube]) -> list[dict[str, str | int]]:
     return [{"tittle": video.title, "description": video.description, 
            "punlish_date": video.publish_date, "author": video.author, 
            "channel": video.channel_url, "views": video.views, "duration": video.length} for video in video_list]
     

def download_message(video_list: list[YouTube]) -> None:
     print({"Downloading": video.title for video in video_list}) 
    

def clean_file_name(name_video: str) -> str:
    return unidecode(name_video)
    


def get_file_names(video_list: list[YouTube], extension: str = ".mp4") -> list[YouTube]:
    return [f"{clean_file_name(video.title)}{extension}" for video in video_list]


def get_file_paths(save_path: Path, file_names: list[str]) -> list[Path]:
    return [save_path/file_name for file_name in file_names]


def existing_video(file_paths: list[Path],
                   file_names: list[str]) -> list[str]:


    messages: list[str] = [f"Video with the title: {video_file_name} exist" if file_path.exists() 
                           else None 
                           for file_path, video_file_name in  zip(file_paths, file_names)]

    filtered_messages: list[str] = [message for message in messages if message is not None]

    for i, file_path in enumerate(file_paths):
      print(f"Video {i+1}: {file_names[i]}")
      print(f"Expected path: {file_path}")   
      print(f"File exists? {file_path.exists()}")

    


    if not filtered_messages:
        return ["Downloading new videos..."]
        
    return filtered_messages


def download_video(video_list: list[YouTube], save_path: Path, 
                   video_information: list[dict[str, str | int]],
                   file_names: list[str] 
                   ) -> None:
    
     try:
        for video, video_file_name in zip(video_list, file_names):
          video.streams.filter(progressive=True).get_highest_resolution().download(
          output_path=save_path, 
          skip_existing=True,
          filename=video_file_name
          )
          
     except PytubeError:
         raise PytubeError



    