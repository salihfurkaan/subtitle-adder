import subprocess
from logging import log


def embed_subtitles(video_path, subtitles_path, output_path):
    command = [
        'ffmpeg',
        '-i', video_path,        
        '-vf', f'subtitles={subtitles_path}',  
        output_path              
    ]

    subprocess.run(command)
    log("The subtitles were embedded into the video successfully, happy watching!")

