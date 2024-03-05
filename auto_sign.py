from requests import post
import re

header = {'content-type': 'application/json;charset=UTF-8'}
cookie = {'koa:sess': '', 'koa:sess.sig': ''}
proxy = {'http': '127.0.0.1:7890', 'https': '127.0.0.1:7890'}
try:
	x = post('https://glados.rocks/api/user/checkin', cookies=cookie, headers=header, data='{"token":"glados.one"}')
except:
	try:
		x = post('https://glados.rocks/api/user/checkin', cookies=cookie, headers=header, data='{"token":"glados.one"}', proxies=proxy)	# 防止开了系统代理
	except:
		input('断网了！')
		exit(1)

if not (("Checkin!" in x.text) or ('Please Try Tomorrow' in x.text)):
	print(x.text)
	input('签到失败！')
else:
    print(re.search('Got [0-9]* Points', x.text).group())
    input()
