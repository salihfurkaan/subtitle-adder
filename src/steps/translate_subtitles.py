from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from languages.languages import lang_code_dict
from models.models import TRANSLATION_MODEL_NAME as model_name
from logging import log

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)


def translate(text, target_lang_code, tensor_type="pt"):
    """
    A function that translates the subtitle text
    Args:
        text: Subtitle text
        target_lang_code: Target language
        tensor_type: The type of the tensor when returning. Don't change it if you don't know what to do..
    Return:
        Returns the translated text.
    """
    inputs = tokenizer(text, return_tensors=tensor_type)

    lang = lang_code_dict[target_lang_code]
    translated_tokens = model.generate(**inputs, forced_bos_token_id=tokenizer.convert_tokens_to_ids(lang)) 

    translated_text = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
    return translated_text

def translate_subtitles(input_file='subtitles.srt', output_file='subtitles_translated.srt', target_language='turkish'):
    """
    A function that saves the translations in a .SRT format to embed.
    Args:
        input_file: Originial subtitle path
        output_file: The output file path where the translated subtitles will be saved at
        target_language: The language name you want to translate the subtitles to
    Return:
        Returns the path of the translated subtitles
    """
    translated_segments = []

    target_lang_code = lang_code_dict.get(target_language.lower())
    if target_lang_code is None:
        raise ValueError(f"Language '{target_language}' is not supported.")

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

        for line in lines:
            if not line.strip().isdigit() and "-->" not in line and line.strip() != "":
                translated_text = translate(line.strip(), target_lang_code)
                translated_segments.append(translated_text)
            else:
                translated_segments.append(line.strip())

    with open(output_file, 'w', encoding='utf-8') as f:
        for segment in translated_segments:
            f.write(segment + "\n")

    log(f"The given video was successfully translated to {target_language} and saved at {output_file} !")

    return output_file

#translate_subtitles(input_file='subtitles.srt', output_file='subtitles_tr.srt', target_language='turkish')