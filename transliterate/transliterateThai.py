from pythainlp.tokenize import word_tokenize
from pythainlp.transliterate import romanize

def transliterateThai_temp(text):
	textList=word_tokenize(text)
	listeRomanized=[]
	for word in textList:
		listeRomanized.append(romanize(word))
	return ' '.join(listeRomanized)

# phrase1='votre {m} {f} vos {m-p} {f-p} [formal]'
# phrase2='[generic] (discourteous if used for a superior)'
def transliterateThai(phrase):
	currentJapanese=''
	result=''
	try:
		for c in phrase:
			if (c >= 'A' and c <= 'z') or (c in ' [].!?,;}{()'):
				if(currentJapanese!=''):
					result += transliterateThai_temp(currentJapanese)
					currentJapanese=''
				result += c
			else:
				currentJapanese+=c
		if(currentJapanese!=''):
			result += transliterateThai_temp(currentJapanese)
			currentJapanese=''
		return result
	except Exception as e:
		return phrase
