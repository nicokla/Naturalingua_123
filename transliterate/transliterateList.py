
from transliterateAll import transliterate
from transliterateListHebrew import transliterateListHebrew
from languageCodes import getCode, getLanguage
import sys
sys.path.append('/Users/nicolas/Desktop/NaturaLingua/utils')
from utils import languagesLatines

def transliterateList(phrases, languageCode):
	print('transliterateList', languageCode)
	if(getLanguage(languageCode) in languagesLatines):
		for phrase in phrases:
			if(phrase.romanized == ''):
				phrase.romanized = phrase.original
				phrase.original = ''
	elif(languageCode.startswith('he')):
		transliterateListHebrew(phrases)
	else:
		longueur=len(phrases)
		for index,phrase in enumerate(phrases):
			print(f'\r{index/longueur*100} %', end='', flush=True)
			phrase.romanized = transliterate(phrase.original, languageCode)

def transliterateList2(word, language):
	return transliterateList(word, getCode(language))

