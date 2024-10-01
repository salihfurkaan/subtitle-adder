import steps
import steps.audio_to_text
import steps.create_subtitles
import steps.embed_subtitles
import steps.translate_subtitles
import steps.video_to_audio


def add_subtitle(video_path,
                 subtitled_video_path,
                 target_language=None,
                 original_subtitle_file_name='subtitles.srt'
                 ):
    """
    A function that adds subtitle to the target video in the provided language.
    Args:
        video_path: Original video path 
        subtitled_video_path: The path where the subtitles will be located at
        target_language: The language of the subtitle. Leave this empty if you want it to be in its original language
        original_subtitle_file_name: Name of the subtitles file. Leave this empty if you don't have a fresh file name idea
    """
    
    audio_file = steps.video_to_audio(video_path)
    transcription_result = steps.audio_to_text(audio_file)
    subtitle_path = steps.create_subtitles(transcription_result, original_subtitle_file_name)

    if target_language is not None:
        subtitle_path = steps.translate_subtitles(subtitle_path, f"subtitles_{target_language}.srt", target_language)

    steps.embed_subtitles(video_path, subtitle_path, subtitled_video_path)





