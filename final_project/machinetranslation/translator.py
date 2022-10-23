"""
This file defines the translation service from English to French
and from French to English.
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
APIKEY = os.environ['apikey']
URL = os.environ['url']

authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)
language_translator.set_service_url(URL)


def english_to_french(english_text):
    """
    This code translates from English to French
    Takes one string as input, returns translated
    string as output.
    """
    try:
        translation = language_translator.translate(
            text = english_text, model_id='en-fr').get_result()
        french_text = translation["translations"][0]["translation"] # pylint: disable=unsubscriptable-object
    except:
        french_text = ""
    return french_text

def french_to_english(french_text):
    """
    This code translates from French to English
    Takes one string as input, returns translated
    string as output.
    """
    try:
        translation = language_translator.translate(text = french_text,
            model_id='fr-en').get_result()
        english_text = translation["translations"][0]["translation"] # pylint: disable=unsubscriptable-object
    except:
        english_text = ""
    return english_text
