# -*- coding: utf-8 -*-

# from hangul import translit
# translit.test()
# translit.romanize('누구')
#translit.romanize('사람들', 'cp949', 'cp949')  


# pip3 install korean_romanizer
from korean_romanizer.romanizer import Romanizer

def transliterateKorean(text):
  r = Romanizer(text)
  return r.romanize() 
