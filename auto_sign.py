from requests import post
from time import sleep

sleep(3)
file = open('C:/autosign_log.txt', 'w')
header = {'content-type': 'application/json;charset=UTF-8'}
port = ''	# 填入clash中的端口号
cookie = {'koa:sess': '', 'koa:sess.sig': ''}	# 填入GLaDOS网页对应的cookie
proxy = {'http': '127.0.0.1:' + port, 'https': '127.0.0.1:' + port}
try:
	x = post('https://glados.rocks/api/user/checkin', cookies=cookie, headers=header, data='{"token":"glados.network"}')
except:
	try:
		x = post('https://glados.rocks/api/user/checkin', cookies=cookie, headers=header, data='{"token":"glados.network"}', proxies=proxy)	# 防止开了系统代理
	except:
		file.write('fail')
		input('断网了！')
		exit(1)
file.write(x.text)
if not (("Checkin! Get 1 Day" in x.text) or ('Please Try Tomorrow' in x.text)):
	print(x.text)
	input('签到失败！')
