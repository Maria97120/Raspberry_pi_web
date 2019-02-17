import time
import DB_redis_web

class Rasp_number(object):

	def __init__(self):
		self.datas={
		"data":[
			{"name":"00.00","tnum":24,"hnum":4,"rnum":4,"pnum":44},
			{"name":"00.01","tnum":36,"hnum":34,"rnum":2,"pnum":4},
			{"name":"00.02","tnum":40,"hnum":24,"rnum":8,"pnum":24},
			{"name":"00.03","tnum":60,"hnum":43,"rnum":4,"pnum":4},
			{"name":"00.04","tnum":11,"hnum":42,"rnum":4,"pnum":24},
			{"name":"00.05","tnum":31,"hnum":46,"rnum":9,"pnum":4},
			{"name":"00.06","tnum":4,"hnum":4,"rnum":4,"pnum":43},
			{"name":"00.07","tnum":4,"hnum":43,"rnum":1,"pnum":4},
			{"name":"00.08","tnum":32,"hnum":4,"rnum":4,"pnum":44},
			{"name":"00.09","tnum":2,"hnum":43,"rnum":0,"pnum":4},
			{"name":"00.10","tnum":82,"hnum":4,"rnum":4,"pnum":34},
			{"name":"00.11","tnum":21,"hnum":41,"rnum":7,"pnum":94},
			{"name":"00.12","tnum":7,"hnum":4,"rnum":4,"pnum":40},
			{"name":"00.13","tnum":43,"hnum":40,"rnum":8,"pnum":49},
			{"name":"00.14","tnum":0,"hnum":4,"rnum":4,"pnum":48},
			{"name":"00.15","tnum":4,"hnum":43,"rnum":4,"pnum":104},
			{"name":"00.16","tnum":20,"hnum":4,"rnum":3,"pnum":4},
			{"name":"00.17","tnum":0,"hnum":44,"rnum":4,"pnum":43},
			{"name":"00.18","tnum":22,"hnum":44,"rnum":4,"pnum":4},
			{"name":"00.19","tnum":0,"hnum":4,"rnum":8,"pnum":43},
			{"name":"00.20","tnum":29,"hnum":49,"rnum":4,"pnum":4},
			{"name":"00.21","tnum":1,"hnum":4,"rnum":4,"pnum":24},
			{"name":"00.22","tnum":7,"hnum":0,"rnum":4,"pnum":4},
			{"name":"00.23","tnum":33,"hnum":4,"rnum":4,"pnum":34}
		]
	}
	
	def get_DB_data(self,rasp_num):
		current_time = time.strftime('%Y-%m-%d ',time.localtime(time.time()))
		'''current_time='2017-10-19 '''
		'''rasp_num='01'''
		data_all_Weather=[]
		data_all_People=[]
		i=0
		while(i<24):
			if(i<10):
				data_all_Weather.append(DB_redis_web.Weather().get_data(rasp_num,current_time+'0'+str(i)))
				data_all_People.append(DB_redis_web.People().get_data(rasp_num,current_time+'0'+str(i)))
				
			else:
				data_all_Weather.append(DB_redis_web.Weather().get_data(rasp_num,current_time+str(i)))
				data_all_People.append(DB_redis_web.People().get_data(rasp_num,current_time+str(i)))

			i=i+1
			
		return data_all_People,data_all_Weather
		
	def make_datas(self,rasp_num):
		i=0
		data_all_People,data_all_Weather=self.get_DB_data(rasp_num)
		
		for data_dict in self.datas['data']:
			for key in data_dict:
				if key=="name":
					pass
				elif key=="tnum":
					data_dict[key]=data_all_Weather[i]['temperature']
				elif key=="hnum":
					data_dict[key]=data_all_Weather[i]['humidity']
				elif key=="rnum":
					data_dict[key]=data_all_Weather[i]['rain']
				elif key=="pnum":
					data_dict[key]=data_all_People[i]['visitors flowrate']
			if i<24:
				i=i+1
			
		return self.datas
		
	def fog_data(self,rasp_num):
		'''current_time='2017-10-19 20'''
		current_time = time.strftime('%Y-%m-%d %H',time.localtime(time.time()))
		fog_dict=DB_redis_web.Weather().get_data(rasp_num,current_time)
		fog=fog_dict["mq"]
		
		return fog
		

if __name__=="__main__":

	'''Rasp_number().make_datas('01')'''
	Rasp_number().fog_data('01')
