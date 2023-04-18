from pytube import YouTube
from youtube.download_video import clean_file_name, get_file_names, save_video_in_path, get_videos, existing_video, download_video, get_video_information, get_file_paths
import openai
from audio.audio_to_text import transcript_audio_to_text, write_transcription_in_file
from config import load_config
from pathlib import Path


def main(url_list: list[str], save_path: str, transcript: bool = False) -> None:
     api_key: dict = load_config()
     openai.api_key = api_key.get("openai_api_key")
     save_directory: Path = save_video_in_path(save_path)
     
     video_list: list[YouTube] = get_videos(url_list=url_list)

     video_names: list[str] = get_file_names(video_list, extension=".mp4")
     file_paths: list[Path] = get_file_paths(save_path=save_directory, file_names=video_names)

     video_information: list[str] = get_video_information(video_list)

     print(existing_video(file_names=video_names, 
                          file_paths=file_paths, 
                          ))

     download_video(video_list=video_list, save_path=save_directory, 
                    video_information=video_information, 
                    file_names=video_names)
     

     if transcript:
          transcriptions: list[str] = transcript_audio_to_text(file_paths=file_paths, 
                                                               file_names=video_names)

          print(transcriptions)

          write_transcription_in_file(transcriptions=transcriptions, path_save=save_video_in_path(path="transcriptions"), 
                                      file_names=get_file_names(video_list, extension=".txt"))



          


if __name__ == "__main__":
     main(url_list=[
                    "https://www.youtube.com/watch?v=Zi_XLOBDo_Y",
                    ],
          save_path="downloads",
          transcript=True)