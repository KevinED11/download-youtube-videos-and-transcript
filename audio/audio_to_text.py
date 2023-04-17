import openai
from pytube import YouTube
from youtube.download_video import get_file_paths
from pathlib import Path
from youtube.download_video import get_file_names


def transcript_audio_to_text(file_paths: list[Path]) -> str:
    transcriptions: list[dict] = []
    
    for audio_path in file_paths:
        audio_file = open(audio_path, "rb")
        transcript = openai.Audio.transcribe("whisper-1", audio_file)

        transcriptions.append(transcript)


        audio_file.close()
        
    return transcriptions
    

        
    