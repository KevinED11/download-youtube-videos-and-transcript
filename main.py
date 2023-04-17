from pytube import YouTube
from youtube.download_video import clean_file_name, get_file_names, save_video_in_path, get_videos, existing_video, download_video, get_video_information, get_file_paths
import openai
from audio.audio_to_text import transcript_audio_to_text
from config import load_config
     

def main(url_list: list[str], save_path: str, transcript: bool = False) -> None:
     apy_key: dict = load_config()
     openai.api_key = apy_key.get("openai_api_key")
     video_list: list[YouTube] = get_videos(url_list=url_list)

     print(existing_video(file_names=get_file_names(video_list), file_paths=get_file_paths(save_path=save_video_in_path(save_path), file_names=get_file_names(video_list))))

     download_video(video_list=video_list, save_path=save_video_in_path(save_path), 
                    video_information=get_video_information(video_list), file_names=get_file_names(video_list))
     

     if transcript:
          print(transcript_audio_to_text(file_paths=get_file_paths(save_video_in_path(save_path), get_file_names(video_list))))
          


if __name__ == "__main__":
     main(url_list=[
                    "https://www.youtube.com/watch?v=A9pd3M1Sxe8&list=RDGMEMQ1dJ7wXfLlqCjwV0xfSNbA&start_radio=1&rv=_MdQaLGwUF0",
                    ],
          save_path="/downloads",
          transcript=True)