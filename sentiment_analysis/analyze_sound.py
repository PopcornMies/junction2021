import MeetingSpeechAnalysis as msa
import sys
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

audio_file = sys.argv[1]

audio_file = msa.convert_file_to_wav(audio_file)
sentence, duration = msa.transcribe_audio(audio_file)
print('Text: ' + sentence)
analysis = msa.get_text_sentiment(sentence)
print(analysis)
msa.dump_to_database(-1, analysis, duration)

