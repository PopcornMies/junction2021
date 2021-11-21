import pandas as pd

def get_meeting_summary():
    meeting_data = pd.read_csv('./sentiment_analysis/database.csv', delimiter=';')
    meeting_duration = 4000

    num_speeches = meeting_data.shape[0]

    sentiment_mean = (meeting_data.positivity.sum()-meeting_data.negativity.sum()) / num_speeches
    sentiment_mean = sentiment_mean*100 + 50
    print('Mean sentiment: ' + str(sentiment_mean))

    # calculate fts-score
    mean_speech_length_prct = meeting_data.duration.sum()/num_speeches/meeting_duration

    # Calculate speaking time per speaker
    unique_speakers = meeting_data.id.unique()

    time_per_speaker = []

    # Get total speaking time for each speaker, normalised by the meeting duration
    for speaker in unique_speakers:
        total_time_spoken_prct = meeting_data.loc[meeting_data.id == speaker, 'duration'].sum()/meeting_duration
        time_per_speaker.append(total_time_spoken_prct)

    # Variance of the normalized total speaking times
    speech_length_var = (time_per_speaker - mean_speech_length_prct).sum()/num_speeches

    # Activity score for the meeting: number of speeches over the meeting duration 
    # and variance of total speech durations
    fts = num_speeches/meeting_duration/speech_length_var*100

    print('FTS Score: ' + str(fts))

    return sentiment_mean, fts


