import redisco
import redis
from redisco.containers import Hash

import urllib2
import time
import json

import Queue
from threading import Thread
import threading 

import pingip

class Database(threading.Thread):

	def __init__(self,thread_number):
		threading.Thread.__init__(self)
		self.thread_number=thread_number
	
		self.Raspberry_run_weather = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
		self.Raspberry_run_people = [1,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]
		
		self.Raspberryname = [
			'01',
			'02',
			'03',
			'04',
			'05',
			'06',
			'07',
			'08',
			'09',
			'10',
			'11',
			'12',
			'13',
			'14',
			'15',
			'16',
			'17',
			'18',
			'19',
			'20'
		]
		
		self.Raspberry_ip={
			'01' : '192.168.137.159',
			'02' : '192.168.137.159',
			'03' : '192.168.137.159',
			'04' : '192.168.137.159',
			'05' : '192.168.137.159',
			'06' : '192.168.137.159',
			'07' : '192.168.137.159',
			'08' : '192.168.137.159',
			'09' : '192.168.137.159',
			'10' : '192.168.137.159',
			'11' : '192.168.137.159',
			'12' : '192.168.137.159',
			'13' : '192.168.137.159',
			'14' : '192.168.137.159',
			'15' : '192.168.137.159',
			'16' : '192.168.137.159',
			'17' : '192.168.137.159',
			'18' : '192.168.137.159',
			'19' : '192.168.137.159',
			'20' : '192.168.137.159',
		}
		
		self.tornado_port="8000"

	def run(self):#threading run

		if self.thread_number==1:
			self.Weather_run()
		elif self.thread_number==2:
			self.People_run()

	def Weather_run(self):
	
		current_time = time.localtime(time.time())#the first time you run to
		self.Raspberry_running(current_time,'W')
		
		while True:
			current_time = time.localtime(time.time())
			if	time.localtime(time.time())[3] != current_time[3]:
				self.Raspberry_running(current_time,'W')
			else:
				continue
				
	def People_run(self):
	
		current_time = time.localtime(time.time())#the first time you run to
		self.Raspberry_running(current_time,'P')
		
		while True:
			current_time = time.localtime(time.time())
			if	time.localtime(time.time())[3] != current_time[3]:
				self.Raspberry_running(current_time,'P')
			else:
				continue

	def Raspberry_running(self,current_time,W_or_P):
			
        #weather_data = Weather().get_weather()
		wcount = 0 #index
		weather_or_people = W_or_P
		if weather_or_people == 'W':
			for run in self.Raspberry_run_weather:
				if run == 1: #running now
					true_run_name = self.Raspberryname[wcount] 
					now_run_ip = self.Raspberry_ip[true_run_name]
					
					self.weather(now_run_ip,true_run_name,self.tornado_port,current_time)
				wcount=wcount+1
				
		pcount = 0
		if weather_or_people == 'P':
			dict_people = {}
			for run in self.Raspberry_run_people:
				if run == 1: #running now
					true_run_name = self.Raspberryname[pcount] 
					now_run_ip = self.Raspberry_ip[true_run_name]
					
					dict_people[true_run_name]=now_run_ip
					pcount=pcount+1
					self.people_set_data(true_run_name,now_run_ip,self.tornado_port,current_time)
			print dict_people
			#self.people(dict_people,self.tornado_port,current_time)
	
	'''for CLASSS'''
	#def people(self,dict_people,port,current_time):
		
		#for peo_name in dict_people:
		#	peo_name = People_threading_run(peo_name,dict_people[peo_name],port,current_time)
		#	peo_name.start()
			
	def people_set_data(self,people_name,people_ip,port,current_time):
	
			#url = "http://"+people_ip+":"+port+"/RPI"
			
			#visitors_perhor=0
			#while time.localtime(time.time())[3] == current_time[3]:
			#	visitors_onesec = urllib2.urlopen(url).read()
			#	visitors_perhor = visitors_perhor + int(visitors_onesec)
			#	time.sleep(2.5)
			
			visitors_perhor=pingip.find_ip('10.204.16')
			print visitors_perhor
			visitors_key  = people_name+"."+'rpi.' + time.strftime('%Y-%m-%d %H',current_time)
			visitors_hash = Hash(visitors_key)
			visitors_hash.hset ("visitors flowrate" , visitors_perhor) 
			
		
	def weather(self,ip,name,port,current_time):
		
		now_url = "http://"+ip+":"+port
		
		url_dict = {

            "TM"   : now_url+"/TM",

            "Rain" : now_url+"/Rain",

            "MQ"   : now_url+"/MQ-2"

        }
		
		which_Raspberry = name
		
		self.get_weather_data(url_dict,which_Raspberry,current_time)
		
		
		
	def get_weather_data(self,url_dict,which_Raspberry,current_time):
	
		weatherdata = [0,0,0,0,0]
		weatherdata[0] = which_Raspberry
	
		TMdata = json.loads(urllib2.urlopen(url_dict['TM']).read())
		weatherdata[1] = TMdata[0]
		weatherdata[2] = TMdata[1]
		
		Raindata = json.loads(urllib2.urlopen(url_dict['Rain']).read())
		weatherdata[3] = Raindata
		
		MQdata = json.loads(urllib2.urlopen(url_dict['MQ']).read())
		weatherdata[4] = MQdata
		
		self.set_weather_data(weatherdata,current_time)
		
	def set_weather_data(self,weatherdata,current_time):
		
		weather_key = weatherdata[0]+'.'+'weather.' + time.strftime('%Y-%m-%d %H',current_time)

		weather_hash = Hash(weather_key)

		weather_hash.hmset(

            { "temperature" : weatherdata[1],

              "humidity"    : weatherdata[2],

              "rain"        : weatherdata[3],

              "mq"          : weatherdata[4]

            }

        )
		
class People_threading_run(threading.Thread):
	def __init__(self,people_name,people_ip,port,current_time):
		threading.Thread.__init__(self)
		self.people_name=people_name
		self.people_ip=people_ip
		self.port=port
		self.current_time=current_time
		
	def run(self):
		self.people_set_data()
		
	def people_set_data(self):
		url = "http://"+self.people_ip+":"+self.port+"/RPI"
		print url
			
		visitors_perhor=0
		while time.localtime(time.time())[3] == self.current_time[3]:
			visitors_onesec = urllib2.urlopen(url).read()
			visitors_perhor = visitors_perhor + int(visitors_onesec)
			time.sleep(2.5)
			
		visitors_key  = self.people_name+"."+'rpi.' + time.strftime('%Y-%m-%d %H',self.current_time)
		visitors_hash = Hash(visitors_key)
		visitors_hash.hset ("visitors flowrate" , visitors_perhor) 
			
def mythread():
	DB_thread_weather = Database(1)
	DB_thread_people = Database(2)
	
	#DB_thread_weather.start()
	DB_thread_people.start()
	
if __name__=="__main__":

	mythread()
    