from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from pypdf import PdfReader
import os


API_KEY = os.environ.get("IBM_API_KEY")
ENDPOINT = 'https://api.au-syd.text-to-speech.watson.cloud.ibm.com/instances/cbdc45d4-a40d-4764-997f-6a4d0937beb6'
print(os.getenv("IBM_API_KEY"))

authenticator = IAMAuthenticator(API_KEY)
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)
text_to_speech.set_service_url(ENDPOINT)


pdf_name = input("Name your PDF file (do not include file type): ")
reader = PdfReader(f'PDFs/{pdf_name}.pdf')
text_to_translate = ''
for page in reader.pages:
    text_to_translate += page.extract_text()
#print(text_to_translate)

tts_name = input("Name your TTS file (do not include file type): ")
voice_to_use = 'en-US_AllisonV3Voice'

print("Generating TTS file, please wait, this may take a few minutes . . .")
with open(f'converted/{tts_name}.mp3', 'wb+') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            text_to_translate,
            voice=voice_to_use,
            accept='audio/mp3'
        ).get_result().content
    )
print("File Generated, check 'converted' folder")
