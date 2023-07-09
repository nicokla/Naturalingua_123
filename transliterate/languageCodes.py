
# http://www.lingoes.net/en/translator/langcode.htm

languageToCodes={
	'arabic':['ar','ar-EG','ar-SA','ar-LB','ar-MA','ar-SY','ar-IQ','ar-JO'],
	'chinese':['zh','zh-CN','zh-TW','zh-CHS','zh-Hans','zh-HK','zh-MO','zh-Hant','zh-CHT','zh-SG'],
	'tagalog':['tl','tl-PH'],
	'french':['fr','fr-FR','fr-CA','fr-BE','fr-CH'],
	'greek':['el','el-GR'],
	'hebrew':['he','he-IL'],
	'hindi':['hi','hi-IN'],
	'italian':['it','it-IT'],
	'japanese':['ja','ja-JP'],
	'korean':['ko','ko-KR'],
	'persian':['fa','fa-IR'],
	'portuguese':['pt','pt-BR','pt-PT'],
	'russian':['ru','ru-RU'],
	'spanish':['es','es-AR','es-ES','es-MX'],
	'thai':['th','th-TH'],
	'turkish':['tr','tr-TR'],
	'vietnamese':['vi','vi-VN'],
	'english':['en','en-CA','en-US','en-GB','en-AU']
}


def getCode(langue):
	if(langue in languageToCodes):
		return languageToCodes[langue][0]
	else:
		return langue[:2]

codeToLanguage={}
for key in languageToCodes:
	value=languageToCodes[key][0][:2]
	codeToLanguage[value]=key

def getLanguage(code):
	codeSmall=code[:2]
	return codeToLanguage[codeSmall]



