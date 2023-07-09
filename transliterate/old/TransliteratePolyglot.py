
from polyglot.text import Text
from unidecode import unidecode

def transliteratePolyglot(blob):
    text = Text(blob)
    l=text.transliterate()
    if len(l) == 0:
        return ''
    t=l[0]
    for i in range(len(l)-1):
        t=t+' '+l[i+1]
    return t












