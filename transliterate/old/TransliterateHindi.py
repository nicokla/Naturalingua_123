# -*- coding: UTF-8 -*-

import re

conversiontable = {
    u'ॐ' : u'oṁ',
    u'ऀ' : u'ṁ',
    u'ँ' : u'ṃ',
    u'ं' : u'ṃ',
    u'ः' : u'ḥ',
    u'अ' : u'a',
    u'आ' : u'ā',
    u'इ' : u'ui',
    u'ई' : u'ī',
    u'उ' : u'u',
    u'ऊ' : u'ū',
    u'ऋ' : u'r̥',
    u'ॠ' : u' r̥̄',
    u'ऌ' : u'l̥',
    u'ॡ' : u' l̥̄',
    u'ऍ' : u'ê',
    u'ऎ' : u'e',
    u'ए' : u'e',
    u'ऐ' : u'ai',
    u'ऑ' : u'ô',
    u'ऒ' : u'o',
    u'ओ' : u'o',
    u'औ' : u'au',
    u'ा' : u'ā',
    u'ि' : u'i',
    u'ी' : u'ī',
    u'ु' : u'u',
    u'ू' : u'ū',
    u'ृ' : u'r̥',
    u'ॄ' : u' r̥̄',
    u'ॢ' : u'l̥',
    u'ॣ' : u' l̥̄',
    u'ॅ' : u'ê',
    u'े' : u'e',
    u'ै' : u'ai',
    u'ॉ' :u'ô',
    u'ो' : u'o',
    u'ौ' : u'au',
    u'क़' : u'q',
    u'क' : u'k',
    u'ख़' : u'x',
    u'ख' : u'kh',
    u'ग़' : u'ġ',
    u'ग' : u'g',
    u'ॻ' : u'g',
    u'घ' : u'gh',
    u'ङ' : u'ṅ',
    u'च' : u'c',
    u'छ' : u'ch',
    u'ज़' : u'z',
    u'ज' : u'j',
    u'ॼ' : u'j',
    u'झ' : u'jh',
    u'ञ' : u'ñ',
    u'ट' : u'ṭ',
    u'ठ' : u'ṭh',
    u'ड़' : u'ṛ',
    u'ड' : u'ḍ',
    u'ॸ' : u'ḍ',
    u'ॾ' : u'd',
    u'ढ़' : u'ṛh',
    u'ढ' : u'ḍh',
    u'ण' : u'ṇ',
    u'त' : u't',
    u'थ' : u'th',
    u'द' : u'd',
    u'ध' : u'dh',
    u'न' : u'n',
    u'प' : u'p',
    u'फ़' : u'f',
    u'फ' : u'ph',
    u'ब' : u'b',
    u'ॿ' : u'b',
    u'भ' : u'bh',
    u'म' : u'm',
    u'य' : u'y',
    u'र' : u'r',
    u'ल' : u'l',
    u'ळ' : u'ḷ',
    u'व' : u'v',
    u'श' : u'ś',
    u'ष' : u'ṣ',
    u'स' : u's',
    u'ह' : u'h',
    u'ऽ' : u'\'',
    u'्' : u'',
    u'़' : u'',
    u'०' : u'0',
    u'१' : u'1',
    u'२' : u'2',
    u'३' : u'3',
    u'४' : u'4',
    u'५' : u'5',
    u'६' : u'6',
    u'७' : u'7',
    u'८' : u'8',
    u'९' : u'9',
    u'ꣳ' : u'ṁ',
    u'।' : u'.',
    u'॥' : u'..',
    u' ' : u' ',
    }
	
	
consonants = u'\u0915-\u0939\u0958-\u095F\u0978-\u097C\u097E-\u097F'
vowelsigns = u'\u093E-\u094C\u093A-\u093B\u094E-\u094F\u0955-\u0957'
nukta = u'\u093C'
virama = u'\u094D'

devanagarichars = u'\u0900-\u097F\u1CD0-\u1CFF\uA8E0-\uA8FF'





def deva_to_latn(text):
    word = text.strip()
    # define a buffer to store the transliteration
    curr = ''
    for index, char in enumerate(word):
        # check if char is a Devanagari character. if true then continue processing.
        # otherwise, output char to curr
        if re.match('[' + devanagarichars + ']', char):
            # if char = consonant, then its transliteration is dependent upon various
            # factors. need to check if next char = nukta, virama, vowel sign.
            if re.match('[' + consonants + ']', char):
                # check next char
                nextchar = word[(index + 1) % len(word)]
                if nextchar:
                    # if next char = nukta, then add present char and nukta 
                    # to 'cons'. else just add present char. set variable
                    # to test for nukta when processing next char
                    if re.match('[' + nukta + ']', nextchar):
                        cons = char + nextchar
                        nukta_present = 1
                    else:
                        cons = char
                        nukta_present = 0
                    # if present char is nukta, then check next char
                    if nukta_present:
                        nextchar = word[(index + 2) % len(word)]
                    # if next char = combining sign or virama, convert consonant 
                    # without "a". else if next char != combining sign or virama, 
                    # add "a" to consonant
                    if re.match('[' + vowelsigns + virama +']', nextchar):
                        trans = conversiontable.get(cons, '')
                        curr = curr + trans
                    else:
                        trans = conversiontable.get(cons, '')
                        trans = trans + "a"
                        curr = curr + trans
            # transliterate all other chars
            else:
                trans = conversiontable.get(char, '')
                curr = curr + trans
        # char is not Devanagari. output char to curr
        else:
             curr = curr + char
    return curr

	
def transliterateHindi(text):
    all_words = []
    for word in text.split():
        latin_output = deva_to_latn(word)
        all_words.append(latin_output)
        joined_all_words = ' '.join(all_words)
    return joined_all_words


# text = u"अ॒ग्निमी॑ळे पु॒रोहि॑तं य॒ज्ञस्य॑ दे॒वमृ॒त्विज॑म्। होता॑रं रत्न॒धात॑मम्॥"
# print(transliterateHindi(text))
# text = u"This is in the देवनागरी script"
# print(transliterateHindi(text))
