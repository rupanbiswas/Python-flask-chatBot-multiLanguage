
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apiKey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apiKey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    #write the code here
    frenchText = language_translator.translate(
    text=englishText,
    model_id='en-fr').get_result()
    print(json.dumps(frenchText, indent=2, ensure_ascii=False))
    print(frenchText['translations'][0]['translation'],'rupan')
    return frenchText['translations'][0]['translation']

def frenchToEnglish(frenchText):
    #write the code here
    englishText = language_translator.translate(
    text=frenchText,
    model_id='fr-en').get_result()
    print(json.dumps(englishText, indent=2, ensure_ascii=False))
    return englishText['translations'][0]['translation']