from src.pipelines import subtitle_adder_pipeline

if __name__ == '__main__':

    video_path = "Put the video path here..."
    output_subtitled_video_path = "Put the final video path here, this video will be with the subtitles."
    target_language = "Put here the name of the language you want to translate it to. If you want it to be in the original language, leave this None"
    original_subtitle_file_name = "What should be the name of the subtitles? Remove this from the code below if you don't have an original file name"
    
    subtitle_adder_pipeline.add_subtitle(video_path, output_subtitled_video_path, target_language, original_subtitle_file_name)
