import MeetingSpeechAnalysis as msa

with open('database.csv','w') as outfile:
    outfile.write('id;negativity;neutrality;positivity;duration\n')

meeting = open('meeting.txt', 'r')
line = meeting.readline()

while(line):
    try:
        speaker_id = line.split(':')[0].strip()
        #print(speaker_id)
        sentence = line.split(':')[1].strip()
        #print(sentence)
        duration = len(sentence)
        results = msa.get_text_sentiment(sentence)
        msa.dump_to_database(speaker_id, results, duration)
    except:
        print("wtfff  " + line)
    line=meeting.readline()