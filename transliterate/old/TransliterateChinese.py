import pinyin

def transliterateChinese(blob):
  return pinyin.get(blob, delimiter=" ")

# class TransliterateChinese:
#   def transliterate(blob):
#     return pinyin.get(blob, delimiter=" ")

# print(pinyin.get(u'你好', delimiter=" "))
#nǐ hǎo

# print(pinyin.get(u'你好', format="strip", delimiter=" "))
#ni hao

#print pinyin.get('你好', format="numerical")
#ni3hao3

