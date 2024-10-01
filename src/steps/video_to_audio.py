from moviepy.editor import VideoFileClip
from logging import log
import os

def convert_to_audio(file_path:str) -> str:
    """
    A function that converts the video file to audio. You may remove this step if you already have the audio
    Args:
        file_path: The video path
    Return:
        Returns the path of output file
    """
    video_clip = VideoFileClip(file_path)
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_name = f"{base_name}_audio.mp3"
    video_clip.audio.write_audiofile(output_name)
    log(f"The video was converted to audio successfully at {output_name} !")
    return output_name