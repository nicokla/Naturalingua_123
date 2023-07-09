from transliterateHindi import transliterateHindi
from transliterateChinese import transliterateChinese
from transliterateJapanese import transliterateJapanese
from transliterateKorean import transliterateKorean
from transliterateArabic import transliterateArabic
from transliterateHebrew import transliterateHebrew
from transliterateRussian import transliterateRussian
from transliterateGreek import transliterateGreek
from transliteratePersian import transliteratePersian
from transliterateThai import transliterateThai
from languageCodes import getCode

# https://www.alchemysoftware.com/livedocs/ezscript/Topics/Catalyst/Language.htm
def transliterate(phrase, languageCode):
	if languageCode.startswith('ja'):
		return transliterateJapanese(phrase)
	elif languageCode.startswith('ar'):
		return transliterateArabic(phrase)
	elif languageCode.startswith('ko'):
		return transliterateKorean(phrase)
	elif languageCode.startswith('el'):
		return transliterateGreek(phrase)
	elif languageCode.startswith('zh'):
		return transliterateChinese(phrase)
	elif languageCode.startswith('ru'):
		return transliterateRussian(phrase)
	elif languageCode.startswith('hi'):
		return transliterateHindi(phrase)
	elif languageCode.startswith('fa'):
		return transliteratePersian(phrase)
	elif languageCode.startswith('th'):
		return transliterateThai(phrase)
	elif languageCode.startswith('he'):
		return transliterateHebrew(phrase)
	else:
		return phrase


def transliterate2(word, langue):
	return transliterate(word, getCode(langue))
