import requests
import json
from Recorder import record_audio, read_audio
from explanation import recognise_and_explain
import shlex 
import subprocess
import readline
# Wit speech API endpoint
API_ENDPOINT = 'https://api.wit.ai/speech'

# Wit.ai api access token
wit_access_token = '5XSGMLPWESNYCRXTTPNLDGO2AZMR5GSX'

#-----------------------------------------------------------------
curl_request = """curl \
 -H 'Authorization: Bearer 5XSGMLPWESNYCRXTTPNLDGO2AZMR5GSX' \
 'https://api.wit.ai/message?v=20200623&q="""

def text_clean(text):
    for i in text:
        if(i==' '):
            text = text.replace(' ','%20')
    return text

def rlinput(prompt, prefill=''):
   readline.set_startup_hook(lambda: readline.insert_text(prefill))
   try:
      return input(prompt)
   finally:
      readline.set_startup_hook()
#-----------------------------------------------------------------
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
    #print('data dictionary = ',data['entities'].keys())
    # get text from data
    text = 'Did not receive any input.'
    received_audio_input = 0
    try:
        text = data['text']
        received_audio_input = 1
    except:
        print('There was some issue recording your query, please try again')
        return
    #-----------------------------------------------------------
    if(received_audio_input==1):
        #processing the returned text
        default_value = text
        print("\n Note : You can edit the query below inplace, if it didn't match what you asked\n")
        print('Did you say?')
        stuff = rlinput("", default_value)
        text = stuff
        sample_text = text_clean(text)
        # print('original text = ',text)
        final_request = curl_request+sample_text+"'"
        # print('curl_request = ',final_request)
        sub_list = shlex.split(final_request)
        #-----------------------------------------------------------
        #Sending request to api again
        #-----------------------------------------------------------
        process = subprocess.Popen(sub_list,
                             stdout=subprocess.PIPE, 
                             stderr=subprocess.PIPE,
                             universal_newlines=True)
        stdout, stderr = process.communicate()
        # print('standard output=',stdout)
        # print('final output=',type(stdout))
        final_dict =json.loads(stdout)
        #print('final_dict = ',(final_dict['entities'].keys()))
        entities = list((final_dict['entities'].keys()))
    #-----------------------------------------------------------
    if text == 'Did not receive any input.':
        print("\nSorry!...We did not recieve any input\n")
    else:
        print("\nYour final query: {}".format(text))
    # return the entity list
    return entities


# if __name__ == "__main__":
#     ### When calling RecognizeSpeech function by clara, then pass language as parameter too
#     lang = 'py'
#     entities =  RecognizeSpeech('myspeech.wav', 6)
#     recognise_and_explain(entities, lang)
    




