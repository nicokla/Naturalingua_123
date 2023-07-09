

ru2la = [[u"о",u'o'],[u"О",u'O'],[u'Щ',u'Shtsh'],[u'щ',u'shtsh'],[u'Х',u'Kh'],[u'х',u'kh'],[u'Ч',u'Tsh'],[u'ч',u'tsh'],[u'Ш',u'Sh'],[u'ш',u'sh'],[u'Ц',u'Ts'],[u'ц',u'ts'],[u'Ё',u'Io'],[u'ё',u'io'],[u'е',u'ie'],[u'ю',u'iu'],[u'Е',u'Ie'],[u'Ю',u'Iu'],[u'Я',u'Ia'],[u'я',u'ia'],[u'а',u'a'],[u'з',u'z'],[u'э',u'e'],[u'р',u'r'],[u'т',u't'],[u'у',u'u'],[u'и',u'i'],[u'п',u'p'],[u'с',u's'],[u'д',u'd'],[u'Ф',u'f'],[u'г',u'g'],[u'ж',u'j'],[u'к',u'k'],[u'л',u'l'],[u'м',u'm'],[u'в',u'v'],[u'б',u'b'],[u'н',u'n'],[u'й',u'y'],[u'А',u'A'],[u'З',u'Z'],[u'Э',u'E'],[u'Р',u'R'],[u'Т',u'T'],[u'У',u'U'],[u'И',u'I'],[u'П',u'P'],[u'С',u'S'],[u'Д',u'D'],[u'ф',u'F'],[u'Г',u'G'],[u'Ж',u'J'],[u'К',u'K'],[u'Л',u'L'],[u'М',u'M'],[u'В',u'V'],[u'Б',u'B'],[u'Н',u'N'],[u'Й',u'Y']]


la2ru = []
for l in ru2la:
	la2ru.append([l[1],l[0]])

def latinToRus(s):
	for k in la2ru:
		s = s.replace(k[0], k[1])
	return s

def transliterateRussian(s):
	for k in ru2la:
		s = s.replace(k[0], k[1])
	return s


# ========================
ar2la=[[u'لإ',u'\'il'],[u'لأ',u'\'al'],[u'إ',u'I'],[u'أ',u'\'a'],[u'ا',u'\''],[u'ر',u'R'],[u'ز',u'Z'],[u'ش',u'Sh'],[u'س',u'S'],[u'ص',u'S'],[u'ض',u'D'],[u'ط',u'T'],[u'ظ',u'Z'],[u'ع',u'3'],[u'غ',u'Gh'],[u'ح',u'7'],[u'خ',u'Kh'],[u'ج',u'J'],[u'ت',u't'],[u'ث',u'Th'],[u'د',u'D'],[u'ذ',u'Z'],[u' و',u' W'],[u'و',u'u'],[u'ي',u'ii'],[u'ق',u'Q'],[u'ف',u'F'],[u'ة',u'a'],[u'ه',u'H'],[u'ك',u'K'],[u'ل',u'L'],[u'م',u'M'],[u'ب',u'B'],[u'ن',u'N'],[u'ى',u'aa'],[u'ُ',u'u'],[u'ِ',u'i'],[u'َ',u'a']]

def transliterateArabic_old(string):
	for k in ar2la:
		string=string.replace(k[0], k[1])
	return string

import epitran
epi = epitran.Epitran('ara-Arab')

def transliterateArabic(s):
	try:
		return epi.transliterate(s)
	except Exception as e:
		return s

from korean_romanizer.romanizer import Romanizer

def transliterateKorean(text):
	try:
		return (Romanizer(text).romanize())
	except Exception as e:
		return text

from transliterate import translit

def transliterateGreek(text):
	return translit(text, 'el', reversed=True)

import cutlet
katsu = cutlet.Cutlet()
katsu.use_foreign_spelling = False

def transliterateJapanese(phrase):
	try:
		return katsu.romaji(phrase)
	except Exception as e:
		return phrase

import MicroTokenizer
import pinyin


def transliterateChineseSub(blob):
	try:
		return pinyin.get(blob, delimiter="")
	except Exception as e:
		return blob

def isLatin(mychar):
  number=ord(mychar)
  return number < 0x80

from functools import reduce

def maFonction(acc, s):
	if(len(acc)==0):
		return s
	if(len(s)==1 and isLatin(s[0]) and isLatin(acc[-1])):
		return acc+s
	else:
		return acc+' '+s

def transliterateChinese(phrase):
	tokens = MicroTokenizer.cut(phrase)
	liste=list(map(transliterateChineseSub,tokens)) 
	result = reduce(maFonction, liste, '') #' '.join(liste)
	return result

# phrase='今天是６月１８号，也是Muiriel的生日！'
# transliterateChinese(phrase)

from indictrans import Transliterator
# https://github.com/libindic/indic-trans
trn = Transliterator(source='hin', target='eng', build_lookup=True)
def transliterateHindi(text):
	try:
		return trn.transform(text)
	except Exception as e:
		return text

from PersianG2p import Persian_g2p_converter
PersianG2Pconverter = Persian_g2p_converter()
def transliteratePersian(sentence):
	return PersianG2Pconverter.transliterate(sentence, secret = True)

from pythainlp.tokenize import word_tokenize
from pythainlp.transliterate import romanize
def transliterateThai(text):
	textList=word_tokenize(text)
	listeRomanized=[]
	for word in textList:
		listeRomanized.append(romanize(word))
	return ' '.join(listeRomanized)


he2la2 = [[u"ג'",u'j'], [u' נְ',u' ne'], [u' מְ',u' me'], [u' לְ',u' le'], [u' וְ',u' ve'],[u' יְ',u' ye'],[u' רְ',u' re'],[u' וֵּ',u've'],[u' תְּ',u'te'],[u' נְּ',u'ne'],[u' מְּ',u'me'],[u'א ',u' '], [u'א,',u','], [u'א.',u'.'], [u'א?',u'?'],[u'א!',u'!'], [u' א',u' '],[u',א',u','], [u'.א',u'.'],[u'?א',u'?'],[u'!א',u'!'], [u'א',u'\''],[u'ז',u'Z'],[u'כָל ',u'KhoL '],[u'כָּל ',u'KoL '],[u'ר',u'R'],[u'ת',u'T'],[u'יֽ',u''], [u'יי',u'Y'],[u'ִי',u'i'], [u'יִ',u'i'],[u'י',u'Y'],[u'ִ',u'i'],[u'ק',u'K'],[u'ד',u'D'],[u'ג',u'G'],[u'ל',u'L'],[u'ט',u'T'],[u'ס',u'S'],[u'מ',u'M'],[u'ם',u'M'],[u'נ',u'N'],[u'ן',u'N'],[u'צ',u'Ts'],[u'ץ',u'Ts'],[u'וו',u'V'],[u'ֹו',u'o'], [u'וֹ',u'o'],[u'וּ',u'u'],[u'וֽ',u''], [u'ון',u'on'],[u'ו',u'V'],[u'שׁ',u'Sh'],[u'שׂ',u'S'],[u'ש',u'Sh'],[u'פּ',u'P'],[u'פ',u'F'],[u'ף',u'F'],[u'כּ',u'K'],[u'כ',u'Kh'],[u'ך',u'Kh'],[u'בְּ',u'Be'],[u'בּ',u'B'],[u'ב',u'V'],[u'ה ',u' '],[u'ה,',u','],[u'ה.',u'.'],[u'ה?',u'?'], [u'ה!',u'!'], [u'ה',u'H'],[u'חַ,',u'aKh,'],[u'חַ ',u'aKh '],[u'חַ!',u'aKh!'],[u'חַ?',u'aKh?'],[u'חַ.',u'aKh.'],[u'ח',u'Kh'],[u' ע',u' '], [u',ע',u','], [u'.ע',u'.'], [u'?ע',u'?'], [u'!ע',u'!'], [u'עַ ',u'a '],[u'עַ,',u'a,'],[u'עַ.',u'a.'],[u'עַ!',u'a!'],[u'עַ?',u'a?'],[u'ע ',u""],[u'ע,',u","],[u'ע.',u"."],[u'ע?',u"?"],[u'ע!',u"!"],[u'ע',u"'"],[u'ַ',u'a'],[u'ֱ',u'e'],[u'ֲ',u'a'],[u'ֳ',u'a'],[u'ָ',u'a'],[u'ֵ',u'e'],[u'ֶ',u'e'],[u'ֻ',u'u'],[u'ֹ',u'o'],[u'ְ',u''],[u'ּ',u''],[u'\\u05bd',u'']]

def transString(langue2lat, string):
	string=' '+string+' '
	for k in langue2lat:
		string=string.replace(k[0], k[1])
	return string.strip()

def enleveNonLatin(mot):
	mot2=""
	for c in mot:
		if(ord(c)<128):
			mot2+=c
	return mot2

def lastStep(phrase):
	phrase=phrase.lower()
	phrase=phrase.replace('|', ' ')
	return phrase

def transliterateHebrew(s):
	return lastStep(enleveNonLatin(transString(he2la2, s)))




# https://www.alchemysoftware.com/livedocs/ezscript/Topics/Catalyst/Language.htm
def transliterate(phrase, language):
	if language=='ja':
		return transliterateJapanese(phrase)
	elif language=='ar':
		return transliterateArabic(phrase)
	elif language=='ko':
		return transliterateKorean(phrase)
	elif language=='el':
		return transliterateGreek(phrase)
	elif language in ['zh-CN','zh-TW','zh','zh-CHS','zh-Hans','zh-HK','zh-MO','zh-Hant','zh-CHT','zh-SG']:
		return transliterateChinese(phrase)
	elif language in ['ru','ru-MD','ru-RU']:
		return transliterateRussian(phrase)
	elif language in ['hi','hi-IN']:
		return transliterateHindi(phrase)
	elif language in ['fa','fa-IR']:
		return transliteratePersian(phrase)
	elif language in ['th','th-TH']:
		return transliterateThai(phrase)
	elif language in ['he', 'he-IL']:
		return transliterateHebrew(phrase)
	else:
		return phrase


def getCode(langue):
	dicoco={'chinese':'zh','persian':'fa','greek':'el'}
	if(langue in dicoco):
		return dicoco[langue]
	else:
		return langue[:2]


def transliterate2(word, langue):
	return transliterate(word, getCode(langue))
