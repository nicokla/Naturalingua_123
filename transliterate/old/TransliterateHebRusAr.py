
# ----------------------

ru2la = [
[u'а',u'a'],
[u'з',u'z'],
[u'э',u'e'],
[u'р',u'r'],
[u'т',u't'],
[u'ы',u'ы'],
[u'у',u'u'],
[u'и',u'i'],
[u'о',u'o'],
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
[u'щ',u'S'],
[u'ь',u'\''],
[u'ъ',u'\"'],
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
[u'О',u'O'],
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
[u'Щ',u'S'],
[u'Ь',u'\''],
[u'Ъ',u'\"'],
[u'В',u'V'],
[u'Б',u'B'],
[u'Н',u'N'],
[u'Я',u'Ia'],
[u'Е',u'Ie'],
[u'Ю',u'iu'],
[u'Й',u'y'],
[u'Ё',u'Io'],
[u'Ч',u'Tsh'],
[u'Ц',u'ts']]


# ----------------------------

he2la = [
[u'א',u'\''],
[u'ז',u'Z'],
[u'ר',u'R'],
[u'ת',u'T'],
[u'יי',u'Y'],
[u'יִ',u'I'],
[u'י',u'Y'],
[u'ִ',u'i'],
[u'ק',u'K'],
[u'ד',u'D'],
[u'ג',u'G'],
[u'ל',u'L'],
[u'ט',u'T'],
[u'ס',u'S'],
[u'מ',u'M'],
[u'ם',u'M'],
[u'נ',u'N'],
[u'ן',u'N'],
[u'צ',u'Ts'],
[u'ץ',u'Ts'],
[u'וֹ',u'o'],
[u'וּ',u'u'],
[u'וו',u'V'],
[u' ו',u' [Ve/U]'], # space then vet : v
[u'ון',u'on'],
[u'ו',u'[u/o]'],
[u'שׁ',u'Sh'],
[u'שׂ',u'S'],
[u'ש',u'[Sh/S]'], # Sh in most places
[u'פּ',u'P'],
[u' פ',u' [P/F]'], # space then fé : P
[u'פ',u'[F/P]'], # fé middle of the word
[u'ף',u'F'],
[u'כּ',u'K'],
[u' כ',u' K'], # space then kaf : K
[u'כ',u'[K/Kh]'],
[u'ך',u'Kh'],
[u'בּ',u'B'],
[u' ב',u' B'], # space then bet : B
[u'ב ',u'V '], # bet then space : V
[u'ב.',u'V.'], # bet then . : V
[u'ב,',u'V,'], # bet then . : V
[u'ב',u'[B/V]'], # bet middle of the word
[u'ה',u'H'],
[u'ח ',u'aKh '], # khet then space : akh
[u'ח,',u'aKh,'], # khet then space : akh
[u'ח.',u'aKh.'], # khet then space : akh
[u'ח',u'Kh'],
[u'ע ',u'3a '], # 3ain then space : 3a
[u'ע,',u'3a,'], # 3ain then space : 3a
[u'ע.',u'3a.'], # 3ain then space : 3a
[u'ע',u'3'],
[u'ַ',u'a'],
[u'ָ',u'a'],
[u'ֵ',u'e'],
[u'ֶ',u'e'],
[u'ֻ',u'u'],
[u'ֹ',u'o'],
[u'ְ',u''],
[u'ּ',u'']
]

# ------------------

ar2la=[
[u'لإ',u'\'il'],
[u'لأ',u'\'al'],
[u'إ',u'I'],
[u'أ',u'\'a'],
[u'ا',u'\''],
[u'ر',u'R'],
[u'ز',u'Z'],
[u'ش',u'Sh'],
[u'س',u'S'],
[u'ص',u'S'],
[u'ض',u'D'],
[u'ط',u'T'],
[u'ظ',u'Z'],
[u'ع',u'3'],
[u'غ',u'Gh'],
[u'ح',u'7'],
[u'خ',u'Kh'],
[u'ج',u'J'],
[u'ت',u't'],
[u'ث',u'Th'],
[u'د',u'D'],
[u'ذ',u'Z'],
[u' و',u' W'],
[u'و',u'u'],
[u'ي',u'ii'],
[u'ق',u'Q'],
[u'ف',u'F'],
[u'ة',u'a'],
[u'ه',u'H'],
[u'ك',u'K'],
[u'ل',u'L'],
[u'م',u'M'],
[u'ب',u'B'],
[u'ن',u'N'],
[u'ى',u'aa'],
[u'ُ',u'u'],
[u'ِ',u'i'],
[u'َ',u'a'],
]

def transString(langue2lat, string):
	for k in langue2lat:
	#string = string.replace(k[0], unicode(k[1]))
		string=string.replace(k[0], k[1])
	return string

def transliterateRussian(s):
    return transString(ru2la, s)
    
def transliterateArabic(s):
    return transString(ar2la, s)

def transliterateHebrew(s):
    return transString(he2la, s)


# transliterateArabic(u'هذا البرنامج يعطينا نطق الحروف')
# transliterateRussian(u'я говорю')
# print(transliterateHebrew(u'שׁמע '))


