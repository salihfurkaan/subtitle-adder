import whisper
from src.models.models import TRANSCRIBER_MODEL as transcriber

def convert_to_text(
        path: str,
        verbose: bool = True,
        log_text: bool = False
):
    """
    A function that converts audio to text with timestamps
    Args:
        path: Audio path
        verbose: Whether it should be verbosed
        log_text: Whether it should write the texts from the audio
    Return:
        result: Transcription result
    """

    model = whisper.load_model(transcriber)
    result = model.transcribe(path, verbose=verbose)

    if log_text:
        print(result["text"])
    
    return result