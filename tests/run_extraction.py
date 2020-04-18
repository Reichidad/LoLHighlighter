from extract import audio_extraction
from audio_test import audio_test

def extract_youtube(url):
    YouTubeURL = url

    try:
        audio_filename = audio_extraction(YouTubeURL)
        directory = './audio/'+audio_filename+'.mp4'

        audio_test(directory)

    except Exception as e:
        print(e)
