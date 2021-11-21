from pydub import AudioSegment
from textblob import TextBlob
import speech_recognition as sr
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#class MeetingSpeechAnalysis():
    
def convert_file_to_wav(filename):
    """Takes an audio file of non .wav format and converts to .wav"""
    # Import audio file
    audio = AudioSegment.from_file(filename)

    # Create new filename
    new_filename = filename.split(".")[0] + ".wav"

    # Export file as .wav
    audio.export(new_filename, format='wav')
    return new_filename


def transcribe_audio(filename):
    """Takes a .wav format audio file and transcribes it to text."""
    # Setup a recognizer instance
    recognizer = sr.Recognizer()

    # Import the audio file and convert to audio data
    audio_file = sr.AudioFile(filename)
    speech_duration = audio_file.DURATION
    with audio_file as source:
        audio_data = recognizer.record(source)

    # Return the transcribed text
    return recognizer.recognize_google(audio_data), speech_duration


def get_text_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    return sid.polarity_scores(text)


def get_text_sentiment2(text):
    return TextBlob(text).sentiment
    

def dump_to_database(id, results, duration):
    line = "{};{};{};{};{}"
    line = line.format(id, results['neg'], results['neu'], results['pos'], duration)
    with open('database.csv','a') as outfile:
        outfile.write(line + "\n")
    return