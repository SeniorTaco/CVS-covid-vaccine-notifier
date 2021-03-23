import requests
import json
import os
import time
from twilio.rest import Client
sentrecently = 0

while True:

	if sentrecently == 1:
		print("Waiting 15 minutes after sending text message...")
		time.sleep(900)
		sentrecently = 0
		#makes sure your phone doesn't get spammed when there are vaccines
		
	print("Waiting 5 minutes between CVS requests...")
	time.sleep(300)
	#without this delay you can get blacklisted
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
	#pull down the JSON with the table of all vaccines
	account_sid = 'replaceMe'
	auth_token = 'replaceMe'
	client = Client(account_sid, auth_token)
	#twilio stuff
	data = vaccineRequest.json()
	stores = (str(vaccineRequest.json()["responsePayloadData"]["data"]["replaceme"]))
	#cuts out the metadata and other parts of the JSON that you don't need, make sure to replace "replaceme" with your state code, for example, MA
	numberBooked = stores.count("Fully Booked")
	numberStores = stores.count("city")
	#make sure that if they add stores it doesn't think there are vaccines
	if numberBooked == numberStores:
		print("No vaccines")
		#simply compare the number of stores to the number of stores that are fully booked, if unequal, there are stores that aren't fully booked, therefore vaccines.
	else:
		message = client.messages \
                .create(
                     body="Vaccine appointments! Go Go Go! https://www.cvs.com/immunizations/covid-19-vaccine",
                     from_='replaceMe',
                     to='replaceMe'
                 )

		print(message.sid)
		#twilio message sending, POST request to the twilio servers
		sentrecently = 1
		#flag set that a message was recently sent
