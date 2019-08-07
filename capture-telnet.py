import sys
import time
import telnetlib
import re
import paramiko

username = "m.yasin"
password = "M.Y4s1n!@#2019"
state = None
a=0
errorDev = []

hosts_file = open("list-ip.txt", "rt")
hosts_list = hosts_file.readlines()
hosts_file.close()
for i in range(0, len(hosts_list)):
 hosts_list[i]=hosts_list[i].rstrip()

for x in hosts_list:
	host = x
	try:
		tn = telnetlib.Telnet(host, 23, timeout=3)
		state=True
		
		if state:
			tn.read_until("username: ")
			tn.write(username + "\n")
			tn.read_until("password: ")
			tn.write(password + "\n")
			tn.write("enable\n")
			tn.write("terminal length 0\n")
			tn.write("show processes memory sorted\n")
			tn.write("show environment temperature\n")
			tn.write("show processes cpu sort\n")
			tn.write("show logging\n")
			tn.write("exit\n")
			hostname = tn.read_some()
			all_capture = tn.read_all()
			
			hostname = hostname.lstrip()
			hostname = hostname[:-1]
			print hostname
			capture_file = open(hostname+".txt", "w")
			capture_file.write(all_capture)
			capture_file.close()
	except:
		print('Error telnet : '+host)
		errorDev.append(host)

err_file = open("errordevice.txt","w")		
err_file.writelines("%s\n" % dev for dev in errorDev)
err_file.close()		