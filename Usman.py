#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\33[1;96m[!] \1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\33[%s;1m'%str(31+j))
    x += '\33[0m'
    x = x.replace('!0','\33[0m')
    sys.stdout.write(x+'\')


def jalan(z):
	for e in z + '\':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)


##### LOGO #####
logo = """
\33[1;91m       ♦♦♦———————————————————————————————♦♦♦
\33[1;91m  ♦♦♦CONTACT FACEBOOK /Usman khokhar♦♦♦
jalan("\33[1;96m•◈•██╗░░░██╗░██████╗███╗░░░███╗░█████╗░███╗░░██╗
jalan("\33[1;96m•◈•██║░░░██║██╔════╝████╗░████║██╔══██╗████╗░██║
jalan("\33[1;97m•◈•██║░░░██║╚█████╗░██╔████╔██║███████║██╔██╗██║
jalan("\33[1;96m•◈•██║░░░██║░╚═══██╗██║╚██╔╝██║██╔══██║██║╚████║
jalan("\33[1;96m•◈•╚██████╔╝██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
jalan("\33[1;96m•◈•░╚═════╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
                
\33[1;96m                  ༆Usman khokhar°᭄ Updated 0.4                 
\33[1;91m      ♦♦♦———————————————————————————————♦♦♦
"""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\\1b[1;93mPlease Wait \1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\33[31mNot Vuln"
vuln = "\33[32mVuln"

os.system("clear")
print  """ 
      
\33[1;92m          🎃🐤  𝕌ˢＭ卂𝐍 ᛕħＯкʰ𝕒я  🍓👑


                                                               

"""

jalan("\33[1;97m•◈•───────•◈  •◈•───────•◈•")  



jalan("\33[1;96m•◈•██╗░░░██╗░██████╗███╗░░░███╗░█████╗░███╗░░██╗
jalan("\33[1;96m•◈•██║░░░██║██╔════╝████╗░████║██╔══██╗████╗░██║
jalan("\33[1;97m•◈•██║░░░██║╚█████╗░██╔████╔██║███████║██╔██╗██║
jalan("\33[1;96m•◈•██║░░░██║░╚═══██╗██║╚██╔╝██║██╔══██║██║╚████║
jalan("\33[1;96m•◈•╚██████╔╝██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
jalan("\33[1;96m•◈•░╚═════╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
 
jalan("   \33[1;91m USMAN KHOKHAR ༆°᭄ ")
jalan("   \33[1;91m THIS IS ILLEGAL IM NOT RESPONSIBLE FOR THIS ")	
jalan("   \33[1;91m WIFI AND LOW SINGNAL USERZ USE ANY PROXY ")	

jalan("   \33[1;93m Welcome To ༆°᭄Usman khokhar tool ")

jalan("\33[1;97m•◈•──────────•◈•\33[1;96mUsman khokhar\33[1;96m•◈•──────────•◈•")

CorrectUsername = "Uk"
CorrectPassword = "Uk"


loop = 'true'
while (loop == 'true'):
    username = raw_input("\33[1;96m[☆] \1b[1;97mUSER ID \1b[1;96m>>>> ")
    if (username == CorrectUsername):
    	password = raw_input("\33[1;96m[☆] \1b[1;97mPASWORD \1b[1;96m>>>> ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username
            loop = 'false'
        else:
            

    else:
        print "Wrong Username"
        os.system('xdg-open https://www.facebook.com/sarfaraz.shar.1

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print 50*"\33[1;96m▪"
		
		
		print('          \33[1;97m[◉] \1b[1;96mLogin New Fresh Account \33[1;97m[◉]' )
		id = raw_input('          \33[1;97m[◉] \33[1;97mID/Email \1b[1;91m: \1b[1;92m')
		pwd = raw_input('          \33[1;97m[◉] \33[1;97mPassword \1b[1;91m: \1b[1;92m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\\33[1;96m[!] \1b[1;91mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:

				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\\1b[1;36;40
