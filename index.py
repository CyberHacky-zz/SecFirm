#!/usr/bin/env python3

import requests 
import urllib.request
import json                                # To use request package in current program 
import sys
import os
import csv
import webbrowser 
from urllib.parse import urlparse
import threading
import time
import socket, subprocess,sys
import _thread
import collections
from datetime import datetime
import shelve
from queue import Queue
from bs4 import BeautifulSoup



#Title print

logo = ('''
       ██████╗███████╗ █████╗ ███████╗██╗██████╗ ███╗  ███╗
     ██╔════╝██╔════╝██╔══██╗██╔════╝██║██╔══██╗████╗ ████║
     ╚█████╗ █████   ██║  ╚═╝█████╗  ██║██████╔╝██╔████╔██║
      ╚═══██╗██╔══╝  ██║  ██╗██╔══╝  ██║██╔══██╗██║╚██╔╝██║
     ██████╔╝███████╗╚█████╔╝██║     ██║██║  ██║██║ ╚═╝ ██║
     ╚═════╝ ╚══════╝ ╚════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[!] This Tool Must Run As ROOT [!]         Created By : SecFirm Team\n\n''')


# Provide Custom Browser headers
headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'

# Print Logo on startup
print(logo)


#Main Menu

def mainmenu():
    print ("""
   {1}--Web Pentesting
   {2}--Network Pentesting
   {3}--Wireless Pentesting
   {4}--Malware Analysis
   {5}--DoS & DDoS
   {6}--Security Hardening
   {0}--Exit
 """)
    choice = input("SecFirm~# ")
    if choice == "1":
        webmenu()
    elif choice == "2":
        networkmenu()
    elif choice == "3":
        wifimenu()
    elif choice == "4":
        malwaremenu()
    elif choice == "5":
        dosmenu()
    elif choice == "6":
        hardeningmenu()
    elif choice == "0":
        print("Thanks for Using SecFirm")
        os.system('clear'), sys.exit()
    elif choice == "":
        print(logo)
        print("\033[1m [+] Kindly Choose One Option \033[0m")
        apimenu()
    else:
        print(logo)
        mainmenu()

# Run Website Pentesting HERE


def webmenu():
    

    print ("""
   {1}--Web Crawler
   {2}--TCP Scan
   {3}--Port Scan
   {0}--Back to Main Menu
   {99}--Exit
 """)
    choice = input("SecFirm~# ")
    if choice == "1":
        webcrawlerfun()
    elif choice == "2":
        tcpscanfun()
    elif choice == "3":
        portscanfun()
    elif choice == "4":
        malwaremenu()
    elif choice == "5":
        dosmenu()
    elif choice == "6":
        hardeningmenu()
    elif choice == "0":
        os.system('clear')
        print(logo)
        mainmenu()
    elif choice == "99":
        print("Thanks for Using SecFirm")
        os.system('clear'), sys.exit()
    elif choice == "":
        print("\033[1m [+] Kindly Choose One Option \033[0m")
        webmenu()
    else:
        print(logo)
        webmenu()

# Web Crawler | Website Pentesting | Webserver Security Testing

def webcrawlerfun():

    os.system('clear')
    print(logo)
    print ("[+] Website Pentesting | Web Crawler : \n")
    url = input("Enter a website to extract the URL's from: ")
    r  = requests.get("http://" +url)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    for link in soup.find_all('a'):
        print(link.get('href'))
        
    webmenu()
# Run Netowrk Pentesting here

def networkmenu():

    print ("""
   {1}--Ping Sweep
   {2}--TCP Scan
   {3}--Port Scan
   {0}--Back to Main Menu
   {99}--Exit
 """)
    choice = input("SecFirm~# ")
    if choice == "1":
        pingsweepfun()
    elif choice == "2":
        tcpscanfun()
    elif choice == "3":
        portscanfun()
    elif choice == "4":
        malwaremenu()
    elif choice == "5":
        dosmenu()
    elif choice == "6":
        hardeningmenu()
    elif choice == "0":
        os.system('clear')
        print(logo)
        mainmenu()
    elif choice == "99":
        print("Thanks for Using SecFirm")
        os.system('clear'), sys.exit()
    elif choice == "":
        print("\033[1m [+] Kindly Choose One Option \033[0m")
        networkmenu()
    else:
        print(logo)
        networkmenu()

# Ping SWEEP | Network Pentesting | Network Machine Detection
def pingsweepfun():

    os.system('clear')
    print(logo)
    print ("[+] Netowrk Pentesting | Ping Sweep : \n")

    ''' section 1 '''

    net = input("Enter the Network Address ")
    net1= net.split('.')
    a = '.'
    net2 = net1[0]+a+net1[1]+a+net1[2]+a
    st1 = int(input("Enter the Starting Number "))
    en1 = int(input("Enter the Last Number "))
    en1 =en1+1
    dic = collections.OrderedDict()
    oper = platform.system()

    if (oper=="Windows"):
        ping1 = "ping -n 1 "
    elif (oper== "Linux"):
        ping1 = "ping -c 1 "
    else :
        ping1 = "ping -c 1 "
    t1= datetime.now()

    '''section 2'''
    class myThread (threading.Thread):
        def __init__(self,st,en):
            threading.Thread.__init__(self)
            self.st = st
            self.en = en
        def run(self):
            run1(self.st,self.en)

    '''section 3''' 
    def run1(st1,en1):
    #print "Scanning in Progess"
        for ip in xrange(st1,en1):
            #print ".",
            addr = net2+str(ip)
            comm = ping1+addr
            response = os.popen(comm)
        for line in response.readlines():
            if(line.count("TTL")):
                break
            if (line.count("TTL")):
            #print addr, "--> Live"
                dic[ip]= addr

    ''' Section 4  '''
    total_ip =en1-st1
    tn =20  # number of ip handled by one thread
    total_thread = total_ip/tn
    total_thread=total_thread+1
    threads= []
    try:
        for i in xrange(total_thread):
            en = st1+tn
            if(en >en1):
                en =en1
                thread = myThread(st1,en)
                thread.start()
                threads.append(thread)
                st1 =en
    except:
        print("Error: unable to start thread")
        print("\t Number of Threads active:", threading.activeCount())


    for t in threads:
        t.join()
        print ("Exiting Main Thread")
        dict = collections.OrderedDict(sorted(dic.items()))

    for key in dict:
        print (dict[key],"-->" "Live")
        t2= datetime.now()
        total =t2-t1
        print ("scanning complete in " , total)

        networkmenu()

# TCP Scan | Network Pentesting

def tcpscanfun():

    os.system('clear')
    print(logo)
    print ("[+] Netowrk Pentesting | TCP Scan : \n")

    '''section 1''' 
    net = input("Enter the Network Address : ")
    st1 = int(input("Enter the starting Number  : "))
    en1 = int(input("Enter the last Number : "))
    en1=en1+1
    dic = collections.OrderedDict()
    net1= net.split('.')
    a = '.'
    net2 = net1[0]+a+net1[1]+a+net1[2]+a
    t1= datetime.now()

    '''section 2'''
    class myThread (threading.Thread):
        def __init__(self,st,en):
            threading.Thread.__init__(self)
            self.st = st
            self.en = en
        def run(self):
            run1(self.st,self.en)
    
    '''section 3'''
    def scan(addr):
        sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((addr,135))
        if result==0:
            sock.close()
            return 1
        else :
            sock.close()
    
    def run1(st1,en1):
        for ip in xrange(st1,en1):
            addr = net2+str(ip)
        if scan(addr):
            dic[ip]= addr

    '''section 4'''
    total_ip =en1-st1
    tn =20  # number of ip handled by one thread
    total_thread = total_ip/tn
    total_thread=total_thread+1
    threads= []
    try:
        for i in xrange(total_thread):
            #print "i is ",i
            en = st1+tn
            if(en >en1):
                en =en1
                thread = myThread(st1,en)
                thread.start()
                threads.append(thread)
                st1 =en
    except:
        print ("Error: unable to start thread")
        print ("\t Number of Threads active:", threading.activeCount())

        for t in threads:
            t.join()
            print ("Exiting Main Thread")
            dict = collections.OrderedDict(sorted(dic.items()))

        for key in dict:
            print (dict[key],"-->" "Live")
            t2= datetime.now()
            total =t2-t1
            print ("scanning complete in " , total)

            networkmenu()

# PORT SCANNING | Network Pentesting

def portscanfun():

    os.system('clear')
    print(logo)
    print ("[+] Netowrk Pentesting | Port Scan : \n")
    
    socket.setdefaulttimeout(0.25)
    print_lock = threading.Lock()

    target = input('Enter the host to be scanned: ')
    t_IP = socket.gethostbyname(target)
    print ('Starting scan on host: ', t_IP)

    def portscan(port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            con = s.connect((t_IP, port))
            with print_lock:
                print(port, 'is open')
            con.close()
        except:
            pass

    def threader():
        while True:
            worker = q.get()
            portscan(worker)
            q.task_done()
    
    q = Queue()
    startTime = time.time()
   
    for x in range(100):
        t = threading.Thread(target = threader)
        t.daemon = True
        t.start()
   
    for worker in range(1, 500):
        q.put(worker)
    
    q.join()
    print('Time taken:', time.time() - startTime)

    networkmenu()

# Call main menu to run program
mainmenu()