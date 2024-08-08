import pandas
import requests
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('BDE8iVtvKyo3sw5eh-pw6nsqdfkiYpPdsNhWX_O1ih8Y')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.au-syd.text-to-speech.watson.cloud.ibm.com/instances/cbdc45d4-a40d-4764-997f-6a4d0937beb6')

text_to_translate = 'hello, this is our first test of text to speech'

voice_to_use = 'en-US_AllisonV3Voice'

with open('TTS1.mp3', 'wb+') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            text_to_translate,
            voice=voice_to_use,
            accept='audio/mp3'
        ).get_result().content
    )
