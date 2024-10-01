from logging import log

def write_srt(transcription_result,
            output_file):
    """
    A function that creates the subtitles for the audio in .SRT format
    Args:
        transcription_result: Results of the transcription operation
        output_file: The output file path where the subtitles will be located at
    Return:
        output_file: Output file path
    
    """
    with open(output_file, 'w') as f:
        for i, segment in enumerate(transcription_result['segments']):
            f.write(f"{i + 1}\n")

            start_time = segment['start']
            end_time = segment['end']

            start_str = f"{int(start_time // 3600):02}:{int((start_time % 3600) // 60):02}:{int(start_time % 60):02},{int((start_time % 1) * 1000):03}"
            end_str = f"{int(end_time // 3600):02}:{int((end_time % 3600) // 60):02}:{int(end_time % 60):02},{int((end_time % 1) * 1000):03}"

            f.write(f"{start_str} --> {end_str}\n")

            f.write(f"{segment['text'].strip()}\n\n")
    log("Subtitles were created successfully in .SRT format!")
    return output_file


