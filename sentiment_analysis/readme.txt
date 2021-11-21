This stuff was used to produce the data used in the demo for sentiment analysis for Miro

You can run this stuff using docker, if you have docker, download the codes and build the container
Running the container with and giving the wanted python script (and command line arguments as needed) 
as arguments will get the results shown

Few demos included, analyze_sound.py can analyze sentiment from speech.
If you want to try it out, add a sound file to the folder you're building the container
from, and give it as command line argument to analyze_sound.

parse_meeting.py and meeting_summary use the included meeting transcript to analyze the overall sentiment
of a meeting as a score between [-1, 1] and overall activity among the participants as a score 
(the higher the more active participants have been equally).

If there was a capability in the meeting software to get realtime sound/transcript and feed it to
these codes, the meeting sentiment analysis could be done in real time...

Meeting transcript is in meeting.txt, originally from:
https://shahparawe.blogspot.com/2013/01/example-script-for-formal-meeting.html

Used libraries include nltk, SpeechRecognition, pydub and other usual stuff like pandas

