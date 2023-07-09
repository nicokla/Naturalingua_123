
import cutlet
katsu = cutlet.Cutlet()
katsu.use_foreign_spelling = False

# phrase1='votre {m} {f} vos {m-p} {f-p} [formal]'
# phrase2='[generic] (discourteous if used for a superior) 貴方達'
def transliterateJapanese(phrase):
	currentJapanese=''
	result=''
	try:
		for c in phrase:
			if (c >= 'A' and c <= 'z') or (c in ' [].!?,;}{()'):
				if(currentJapanese!=''):
					result += katsu.romaji(currentJapanese).lower()
					currentJapanese=''
				result += c
			else:
				currentJapanese+=c
		if(currentJapanese!=''):
			result += katsu.romaji(currentJapanese).lower()
			currentJapanese=''
		return result
	except Exception as e:
		return phrase
