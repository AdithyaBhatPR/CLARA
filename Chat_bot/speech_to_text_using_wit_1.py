import requests
import json
from Recorder import record_audio, read_audio
from explanation import recognise_and_explain
# Wit speech API endpoint
API_ENDPOINT = 'https://api.wit.ai/speech'

# Wit.ai api access token
wit_access_token = '5XSGMLPWESNYCRXTTPNLDGO2AZMR5GSX'


def RecognizeSpeech(AUDIO_FILENAME, num_seconds):

    # record audio of specified length in specified audio file
    record_audio(num_seconds, AUDIO_FILENAME)

    # reading audio
    audio = read_audio(AUDIO_FILENAME)

    # defining headers for HTTP request
    headers = {'authorization': 'Bearer ' + wit_access_token,
               'Content-Type': 'audio/wav'}

    # making an HTTP post request
    resp = requests.post(API_ENDPOINT, headers = headers,
                         data = audio)
    #print('Http post request=',resp)
    # converting response content to JSON format
    data = json.loads(resp.content)
    #print(data)
    entities = list(data['entities'].keys())
    #print('data dictionary = ',entities)
    # get text from data
    text = data['text']

    print("\nYou said: {}".format(text))
    # return the text
    return entities


if __name__ == "__main__":
    entities =  RecognizeSpeech('myspeech.wav', 7)
    recognise_and_explain(entities)
    #print("\nYou said: {}".format(text))
