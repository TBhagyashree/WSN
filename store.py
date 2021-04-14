import requests
def send():
	n={'card':'B566YT'}
	requests.post('http://192.168.0.4:8000/attendence/attendence_save/',data=n)

send()