import cutlet
katsu = cutlet.Cutlet()
katsu.use_foreign_spelling = False

def transliterateJapanese(text):
  return katsu.romaji(text)