from moviepy.editor import VideoFileClip
import speech_recognition as sr
import os

def extract_audio(video_path, output_path="outputs/audio.wav"):
    os.makedirs("outputs", exist_ok=True)

    video = VideoFileClip(video_path)
    video.audio.write_audiofile(output_path)

    return output_path


def speech_to_text(audio_path):
    r = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio = r.record(source)

    try:
        text = r.recognize_google(audio)
    except:
        text = ""

    return text


def count_filler_words(text):
    filler_words = ["um", "uh", "like", "you know"]
    count = sum(1 for word in text.lower().split() if word in filler_words)
    return count