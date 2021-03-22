import requests
import json
import os
import time
from twilio.rest import Client
sentrecently = 0

while True:

	if sentrecently == 1:
		print("Waiting 5 minutes after sending text message...")
		time.sleep(300)
		sentrecently = 0
		
	print("Waiting 5 seconds between CVS requests...")
	time.sleep(5)
	
	genInfo = requests.get("replaceMe")
	
	cookieinfo = genInfo.headers['Set-Cookie']
	
	vaccineRequest = requests.get("replaceMe", headers={
	    'cookie': cookieinfo,
	    'authority': 'www.cvs.com',
	    'accept': '*/*',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'referer': 'https://www.cvs.com/immunizations/covid-19-vaccine',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
	})
	
	account_sid = 'replaceMe'
	auth_token = 'replaceMe'
	client = Client(account_sid, auth_token)
	
	data = vaccineRequest.json()
	stores = (str(vaccineRequest.json()["responsePayloadData"]["data"]["MA"]))
	
	numberBooked = stores.count("Fully Booked")
	numberStores = stores.count("city")
	
	if numberBooked == numberStores:
		print("No vaccines")
	else:
		message = client.messages \
                .create(
                     body="Vaccine appointments! Go Go Go! https://www.cvs.com/immunizations/covid-19-vaccine",
                     from_='replaceMe',
                     to='replaceMe'
                 )

		print(message.sid)
		sentrecently = 1
