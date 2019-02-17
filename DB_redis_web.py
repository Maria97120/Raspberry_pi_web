import redis
import time

r=redis.Redis(host="127.0.0.1")

class Weather(object):

	def __init__(self):
	
		r=redis.Redis(host="127.0.0.1")
		
	def get_data(self,which_rasp,string_time):
	
		'''current_time = time.strftime('%Y-%m-%d %H',time.localtime(time.time()))'''
		
		wetherkey = which_rasp+".weather."+string_time
		data = r.hgetall(wetherkey)
		
		if len(data)==0:
			data['mq']=0
			data['temperature']=0
			data['rain']=0
			data['humidity']=0
			

		return data
		
	def test(self,rasp_test_num,test_time):
	
		test_data = self.get_data(rasp_test_num,test_time)
		
		
class People(object):

	def __init__(self):
	
		r=redis.Redis(host="127.0.0.1")
		
	def get_data(self,which_rasp,string_time):
	
		peoplekey = which_rasp+".rpi."+string_time
		data = r.hgetall(peoplekey)
		
		if len(data)==0:
			data["visitors flowrate"]=0
			

		return data
		
	def test(self,rasp_test_num,test_time):
	
		test_data = self.get_data(rasp_test_num,test_time)

if __name__=="__main__":

	People().test('01','2017-10-19 20')
	Weather().test('01','2017-10-19 20')