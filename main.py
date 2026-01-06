from bs4 import BeautifulSoup
import requests

from parsers import synonyms_antonyms_parser, parser_v2


SYNONYMS_URL = "https://www.wordhippo.com/what-is/another-word-for/"
ANTONYMS_URL = "https://www.wordhippo.com/what-is/the-opposite-of/"
DEFINITION_URL = ""
SENTENCES_URL = ""
TRANSLATIONS_URL= "https://www.wordhippo.com/what-is/process-form.html"

def get_synonyms(word):
    url = SYNONYMS_URL + f"{word}.html"
    response = requests.get(url)
    synonyms_antonyms_parser(response)

def get_antonyms(word):
    url = ANTONYMS_URL + f"{word}.html"
    response = requests.get(url)
    parser_v2(response)

def get_definition():
    pass

def get_sentences():
    pass

# def translate_to_english(from_lang, sentence):
#     ### Some issue with the process form - Facing the verification issue by the cloudflare bot detection.
#     sentence_url_encoded = sentence.strip().replace(" ", "+")
#     url = TRANSLATIONS_URL + f"?type=to_en&lang={from_lang}&word={sentence_url_encoded}&action=translate"
#     print(sentence_url_encoded)
#     print(url)
#     response = requests.get(url=url, verify=True)
#     print((response.text))

def translate_from_english():
    pass
    

# translate_to_english(from_lang="bengali", sentence="Dhonnobad")
get_antonyms(word="Juxtaposition")

