'''
This is code is to use ibm watson tools
to translate from english to french and vice versa
'''
import json
import os

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
URL = os.environ['url']

AUTHENTICATOR = IAMAuthenticator(apikey)
VERSION = '2018-05-01'

language_translator = LanguageTranslatorV3(version=VERSION,authenticator=AUTHENTICATOR)
language_translator.set_service_url(URL)

def english_to_french(english_text):
    '''
    translate text from english to french
    '''
    tr_response = language_translator.translate(text=english_text, model_id='en-fr')
    translation  = tr_response.get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    '''
    translate text from french to english
    '''
    tr_response = language_translator.translate(text=french_text, model_id='fr-en')
    translation  = tr_response.get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
