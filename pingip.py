import platform 
import sys 
import os 
import time 
import thread 

count_ip=0
def get_os():
	os = platform.system() 
	if os == "Windows": 
		return "n"
	else: 
		return "c"

def ping_ip(ip_str):
	global count_ip
	cmd = ["ping", "-{op}".format(op=get_os()), 
		"1", ip_str] 
	output = os.popen(" ".join(cmd)).readlines() 
	
	flag = False
	for line in list(output): 
		if not line: 
			continue
		if str(line).upper().find("TTL") >=0: 
			flag = True
			break
	if flag: 
		print "ip: %s is ok ***"%ip_str
		count_ip=count_ip+1
	
def find_ip(ip_prefix):
	global count_ip
	for i in range(1,256): 
		ip = '%s.%s'%(ip_prefix,i) 
		thread.start_new_thread(ping_ip, (ip,))
		time.sleep(0.3)
	print count_ip
	return count_ip
	
if __name__ == "__main__":
	print "start time %s"%time.ctime() 
	commandargs = sys.argv[1:]
	if commandargs:
		args = "".join(commandargs)
	else:
		args='10.204.16.1'
	ip_prefix = '.'.join(args.split('.')[:-1])
	find_ip(ip_prefix)
	print "end time %s"%time.ctime()