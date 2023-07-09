

ru2la = [
[u"о'",u'OO'],
[u"о",u'a'],
[u"OO",u'o'],
[u"О'",u'OO'],
[u"О",u'A'],
[u"OO",u'O'],
[u"'",u''],
[u'а',u'a'],
[u'з',u'z'],
[u'э',u'e'],
[u'р',u'r'],
[u'т',u't'],
[u'ы',u'ы'],
[u'у',u'u'],
[u'и',u'i'],
[u'п',u'p'],
[u'ш',u'sh'],
[u'с',u's'],
[u'д',u'd'],
[u'Ф',u'f'],
[u'г',u'g'],
[u'х',u'kh'],
[u'ж',u'j'],
[u'к',u'k'],
[u'л',u'l'],
[u'м',u'm'],
[u'щ',u'shtsh'],
[u'ь',u'ь'],
[u'ъ',u'ъ'],
[u'в',u'v'],
[u'б',u'b'],
[u'н',u'n'],
[u'я',u'ia'],
[u'е',u'ie'],
[u'ю',u'iu'],
[u'й',u'y'],
[u'ё',u'io'],
[u'ч',u'tsh'],
[u'ц',u'ts'],
[u'А',u'A'],
[u'З',u'Z'],
[u'Э',u'E'],
[u'Р',u'R'],
[u'Т',u'T'],
[u'Ы',u'Ы'],
[u'У',u'U'],
[u'И',u'I'],
[u'П',u'P'],
[u'Ш',u'Sh'],
[u'С',u'S'],
[u'Д',u'D'],
[u'ф',u'F'],
[u'Г',u'G'],
[u'Х',u'Kh'],
[u'Ж',u'J'],
[u'К',u'K'],
[u'Л',u'L'],
[u'М',u'M'],
[u'Щ',u'Shtsh'],
[u'Ь',u'Ь'],
[u'Ъ',u'Ъ'],
[u'В',u'V'],
[u'Б',u'B'],
[u'Н',u'N'],
[u'Я',u'Ia'],
[u'Е',u'Ie'],
[u'Ю',u'Iu'],
[u'Й',u'y'],
[u'Ё',u'Io'],
[u'Ч',u'Tsh'],
[u'Ц',u'Ts']]


# https://stackoverflow.com/questions/483666/reverse-invert-a-dictionary-mapping/483833#483833


from russtress import Accent
accent = Accent()

def transliterateRussian(s):
	s = accent.put_stress(s)
	for k in ru2la:
		s = s.replace(k[0], k[1])
	return s

# transliterateRussian(u'я говорю')


