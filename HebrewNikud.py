
# https://github.com/outofink/morfix-lite/blob/master/server/index.js
# https://github.com/oprogramador/most-common-words-by-language/tree/master/src/resources
# https://nakdan-3-2.loadbalancer.dicta.org.il/api
# https://nakdan.dicta.org.il/

import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


headers = {
    'authority': 'nakdan-3-2.loadbalancer.dicta.org.il',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
    'content-type': 'text/plain;charset=UTF-8',
    'accept': '*/*',
    'origin': 'https://nakdan.dicta.org.il',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://nakdan.dicta.org.il/',
    'accept-language': 'en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7,he-IL;q=0.6,he;q=0.5,zh-CN;q=0.4,zh;q=0.3',
}


def getFirstOption(object):
	if(object['sep']):
		return object['word']
	else:
		return object['options'][0][0]

import functools

he2la2 = [
[u"ג'",u'j'], 
[u' נְ',u' ne'], 
[u' מְ',u' me'], 
[u' לְ',u' le'], 
[u' וְ',u' ve'],
[u' יְ',u' ye'],
[u' רְ',u' re'],
[u' וֵּ',u've'],
[u' תְּ',u'te'],
[u' נְּ',u'ne'],
[u' מְּ',u'me'],
[u'א ',u' '], # aleph muet a la fin du mot
[u'א,',u','], # aleph muet a la fin du mot
[u'א.',u'.'], # aleph muet a la fin du mot
[u'א?',u'?'], # aleph muet a la fin du mot
[u'א!',u'!'], # aleph muet a la fin du mot
[u' א',u' '], # aleph muet au debut du mot
[u',א',u','], # aleph muet au debut du mot
[u'.א',u'.'], # aleph muet au debut du mot
[u'?א',u'?'], # aleph muet au debut du mot
[u'!א',u'!'], # aleph muet au debut du mot
[u'א',u'\''],
[u'ז',u'Z'],
[u'כָל ',u'KhoL '],
[u'כָּל ',u'KoL '],
[u'ר',u'R'],
[u'ת',u'T'],
[u'יֽ',u''], # yud silencieux
[u'יי',u'Y'],
[u'ִי',u'i'], # first nikud, then yud
[u'יִ',u'i'], # first yud, then nikud
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
[u'וו',u'V'],
[u'ֹו',u'o'], # first nikud, then vav
[u'וֹ',u'o'], # first vav, then nikud
[u'וּ',u'u'],
[u'וֽ',u''], # vav silencieux
[u'ון',u'on'],
[u'ו',u'V'],
[u'שׁ',u'Sh'],
[u'שׂ',u'S'],
[u'ש',u'Sh'],
[u'פּ',u'P'],
[u'פ',u'F'],
[u'ף',u'F'],
[u'כּ',u'K'],
[u'כ',u'Kh'],
[u'ך',u'Kh'],
[u'בְּ',u'Be'],
[u'בּ',u'B'],
[u'ב',u'V'],
[u'ה ',u' '], # he muet a la fin du mot
[u'ה,',u','], # he muet a la fin du mot
[u'ה.',u'.'], # he muet a la fin du mot
[u'ה?',u'?'], # he muet a la fin du mot
[u'ה!',u'!'], # he muet a la fin du mot
[u'ה',u'H'],
[u'חַ,',u'aKh,'],
[u'חַ ',u'aKh '],
[u'חַ!',u'aKh!'],
[u'חַ?',u'aKh?'],
[u'חַ.',u'aKh.'],
[u'ח',u'Kh'],
[u' ע',u' '], # ain muet au debut du mot
[u',ע',u','], # ain muet au debut du mot
[u'.ע',u'.'], # ain muet au debut du mot
[u'?ע',u'?'], # ain muet au debut du mot
[u'!ע',u'!'], # ain muet au debut du mot
[u'עַ ',u'a '],
[u'עַ,',u'a,'],
[u'עַ.',u'a.'],
[u'עַ!',u'a!'],
[u'עַ?',u'a?'],
[u'ע ',u""],
[u'ע,',u","],
[u'ע.',u"."],
[u'ע?',u"?"],
[u'ע!',u"!"],
[u'ע',u"'"],
[u'ַ',u'a'],
[u'ֱ',u'e'],
[u'ֲ',u'a'],
[u'ֳ',u'a'],
[u'ָ',u'a'],
[u'ֵ',u'e'],
[u'ֶ',u'e'],
[u'ֻ',u'u'],
[u'ֹ',u'o'],
[u'ְ',u''],
[u'ּ',u''],
[u'\\u05bd',u'']
]


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


# ---------------------
# get multiple sentences, todo
# https://www.twilio.com/blog/asynchronous-http-requests-in-python-with-aiohttp

import aiohttp
import asyncio
import functools

def getData(sentence):
	sentence=sentence.replace('"','\\"')
	data = '{"task":"nakdan","data":"'+sentence+'","addmorph":true,"keepqq":false,"matchpartial":true,"nodageshdefmem":false,"patachma":false,"keepmetagim":true,"genre":"modern"}'
	return data.encode('utf-8')


def getFirstOption(object):
	if(object['sep']):
		return object['word']
	else:
		return object['options'][0][0]
	
async def getNikud2(session, sentence):
	async with session.post('https://nakdan-3-2.loadbalancer.dicta.org.il/api', headers=headers, data=getData(sentence)) as resp:
		try:
			myjson = await resp.json()
			words=list(map(getFirstOption, myjson))
			sentence2=functools.reduce(lambda a, b: a+b, words)
			return sentence2
		except Exception as e:
			return sentence

def improve(sentence):
  return sentence.replace('\n', ' ').strip()

async def getResults(sentences):
	async with aiohttp.ClientSession() as session:
		tasks = []
		for sentence in sentences:
			tasks.append(asyncio.ensure_future(getNikud2(session, improve(sentence['text']))))
		all_results = await asyncio.gather(*tasks)
		return all_results


# ----------------------------------------------
# 1) 
# https://developers.google.com/youtube/v3/docs/search/list
# https://github.com/rhayun/python-youtube-api
# https://console.cloud.google.com/apis

from youtube_api import YoutubeAPI
import os
youtubeKey=os.environ['YOUTUBE_KEY']
youtube = YoutubeAPI({'key': youtubeKey})


# https://www.youtube.com/watch?v=VIDEO_ID_HERE
def getChannelId(channelName):
  params = {
    'q':channelName,
    'part':"snippet",
    'type':"channel",
  }
  search = youtube.search_advanced(params, True)
  return search['results'][0]['id']['channelId']


def getAllVideosFromChannel(channelName):
  channelId = getChannelId(channelName)
  params = {
      'q':'',
      'part':"snippet",
      'channelId':channelId,
      'type':"video",
      'maxResults':"50"
  }
  search = youtube.search_advanced(params, True)
  results=search['results']
  myToken = search['info']
  while(True):
    canContinue = 'nextPageToken' in myToken and myToken['nextPageToken'] != None
    if(canContinue):
      params['pageToken'] = myToken['nextPageToken']
      # print(myToken)
      newVideos=youtube.search_advanced(params, True)
      myToken = newVideos['info']
      results+=newVideos['results']
      # len(results)
    else:
      break
  return results


# liste1[0]['id']['videoId']
def getVideoIdAndName(elem):
  return (elem['id']['videoId'], elem['snippet']['title'])


def getAllVideoIdsAndNames(channelName):
  liste1=getAllVideosFromChannel(channelName)
  answer=list(map(getVideoIdAndName, liste1))
  return answer

# --------------------------------------------------------------
# 2) Get transcripts (hebrew, and english)
# https://pypi.org/project/youtube-transcript-api/

from youtube_transcript_api import YouTubeTranscriptApi


def getTimeString(number):
  numberDixiemes = int((number%1)*10)%10
  numberInt = int(number)
  numberSec = numberInt%60
  numberMinutes = int(numberInt/60)%60
  numberHours = int(numberInt/3600)
  s=''
  if(numberHours>0):
    s+=format(numberHours, '02d')+':'
  s+=format(numberMinutes, '02d')+':'
  s+=format(numberSec, '02d')+','
  s+=format(round(numberDixiemes), '01d')
  return s


def isLatin(mychar):
  number=ord(mychar)
  return number < 0x80


def phraseRemoveHebrewCharacters(sentence):
  newSentence=''
  for c in sentence:
    if(isLatin(c)):
      newSentence+=c
  return newSentence


def myCondition1(hebStart, hebDuration, angStart, angDuration):
  return (hebStart < angStart + angDuration)


def myCondition2(hebStart, hebDuration, angStart, angDuration):
  return (hebStart - 0.3 < angStart)


def myCondition3(hebStart, hebDuration, angStart, angDuration):
  return (hebStart - 0.3 < angStart) or\
    ((hebStart > angStart) and (hebStart + hebDuration - 0.3 < angStart + angDuration))


def writeFileGeneral(transcriptHebreu, transcriptAnglais, file1, videoId, videoTitle):
	file1.write('\n-------------------------\n')
	file1.write(videoTitle+'\n')
	file1.write(videoId+'\n')
	file1.write('-------------------------\n')
	i = 0
	j = 0
	phraseHeb = transcriptHebreu[i]
	phraseAng = transcriptAnglais[j]
	while (True):
		if((i>=len(transcriptHebreu)) and (j>=len(transcriptAnglais)) ):
			break
		if((j >= len(transcriptAnglais) or myCondition3(phraseHeb['start'], phraseHeb['duration'], phraseAng['start'], phraseAng['duration'])) and (i < len(transcriptHebreu)) ):
			phraseRomaji=phraseHeb['romanized']
			# phraseHebText=phraseHeb['text']
			# file1.write(f"- {phraseHebText}\n" )
			file1.write(f"- {phraseRomaji} [{getTimeString(phraseHeb['start'])}]\n")
			i += 1
			if(i < len(transcriptHebreu)):
				phraseHeb = transcriptHebreu[i]
		elif j < len(transcriptAnglais):
			phraseAng2 = improve(phraseRemoveHebrewCharacters(phraseAng['text']))
			file1.write('     '+phraseAng2+ ' ['+getTimeString(phraseAng['start'])+']'+'\n')
			j += 1
			if(j < len(transcriptAnglais)):
				phraseAng = transcriptAnglais[j]


# he, en
def getManualSub(transcriptList, language):
  hebrewOk=True
  try:
    transcriptHebreuFetchable=transcriptList.find_manually_created_transcript([language])
  except Exception as e:
    hebrewOk=False
    transcriptHebreuFetchable = {}
  return hebrewOk, transcriptHebreuFetchable


# 'piece of hebrew', ...
channels = ['piece of hebrew']
for channelName in channels:
	fileName="/Users/nicolas/Desktop/"+channelName+".txt"
	myVideoIdsAndNames = getAllVideoIdsAndNames(channelName)
	file1 = open(fileName,"w+")
	aaa=-1
	for videoId, videoTitle in myVideoIdsAndNames:
		aaa+=1
		try:
			transcriptList = YouTubeTranscriptApi.list_transcripts(videoId)
		except Exception as e:
			print(str(aaa)+'/'+str(len(myVideoIdsAndNames))+', no subs')
			continue
		hebrewOk, transcriptHebreuFetchable = getManualSub(transcriptList, 'iw')
		englishOk, transcriptAnglaisFetchable = getManualSub(transcriptList, 'en')
		if(englishOk and hebrewOk):
			try:
				transcriptAnglais = transcriptAnglaisFetchable.fetch()
				transcriptHebreu = transcriptHebreuFetchable.fetch()
			except Exception as e:
				print(str(aaa)+'/'+str(len(myVideoIdsAndNames))+', erreur bizarre')
				continue
		else:
			print(str(aaa)+'/'+str(len(myVideoIdsAndNames))+', snif: ' + videoId)
			continue
		print(str(aaa)+'/'+str(len(myVideoIdsAndNames))+', youpi: ' + videoId)
		nikuds=asyncio.run(getResults(transcriptHebreu))
		romanized=list(map(transliterateHebrew, nikuds))
		for i in range(len(transcriptHebreu)):
			transcriptHebreu[i]['text']=nikuds[i]
			transcriptHebreu[i]['romanized']=romanized[i]
		writeFileGeneral(transcriptHebreu, transcriptAnglais, file1, videoId, videoTitle)
	file1.close()


def postProcessing(fileName):
  replacements = {'khakha':'kakha', ' beli ':' bli ', "ha '":"ha ", "ka'n":'kan', "she '":'she ', "ve '":'ve ', "be '":"be ", "yay":"ya", 'layv':'lav', ' k ze':' ka ze',' k ':' ke '}
  lines = []
  with open(fileName) as infile:
    for line in infile:
      for src, target in replacements.items():
        line = line.replace(src, target)
      lines.append(line)
  with open(fileName, 'w') as outfile:
    for line in lines:
      outfile.write(line)

fileName="/Users/nicolas/Desktop/piece of hebrew.txt"
postProcessing(fileName)


# ----------------
# todo (?) : utiliser la mm structure que pour les films

# class Phrase:
#   def __init__(self, start, text, end, romanized='', style=''):
#     self.start = start
#     self.end = end
#     self.text = text
#     self.romanized = romanized
#     self.style = style
#   def __str__(self) -> str:
#     debut = getTimeString(self.start)
#     fin = getTimeString(self.end)
#     return (f'[{debut} --> {fin}] : {self.text} ({self.romanized}) [style:{self.style}]')




# def getRomanized(sentence):
# 	sentence2=getNikud(sentence)
# 	romanized=transliterateHebrew(sentence2)
# 	return sentence2,romanized

# s='וְכָכָה יָכְלוּ לְהַבְדִּיל בֵּין הַמִּיֽלִּים הַשּׁוֹנוֹת'
# transliterateHebrew(s)

# sentence=['הדבר הזה לא מובן מאליו']
# sentence2,romanized=getRomanized(sentence)


# def getNikud(sentence):
# 	sentence=sentence.replace('"','\\"')
# 	data = '{"task":"nakdan","data":"'+sentence+'","addmorph":true,"keepqq":false,"matchpartial":true,"nodageshdefmem":false,"patachma":false,"keepmetagim":true,"genre":"modern"}'
# 	response = requests.post('https://nakdan-3-2.loadbalancer.dicta.org.il/api', headers=headers, data=data.encode('utf-8'))
# 	try:
# 		myjson=response.json()
# 		words=list(map(getFirstOption, myjson))
# 		sentence2=functools.reduce(lambda a, b: a+b, words)
# 	except Exception as e:
# 		print(e) # response.status_code
# 	return sentence2

# sentence='ובעברית מהירה בעברית מדוברת זה יהפוך להיות "תה" בא אליי אם שמתם לב גם במקום להגיד'
# nikud=getNikud(sentence)
# sentence=sentence.replace('"','\\"')
# nikud=getNikud(sentence)



# sentences=[{'text':'הדבר הזה לא מובן מאליו'} ,
# {'text':'תנסה עוד פעם'},
# {'text':'למה אמרת לי את זה?'},
# ]
# # start_time = time.time()
# results=asyncio.run(getResults(sentences))
# # print("--- %s seconds ---" % (time.time() - start_time))

