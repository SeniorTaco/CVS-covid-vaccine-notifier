# CVS-covid-vaccine-notifier
Use this script to automatically scrape the CVS website for vaccine appointments and send push notifications via twilio to register your appointment

READ BEFORE USING SCRIPT:
This script is designed to scrape the CVS website and parse the JSON in such a manner that it can determine when new vaccine appointments are available which then triggers a push notification with Twilio.

Dependencies:
Python3
Twilio account with phone number, account-aid, and auth_token set up, see more here: https://www.twilio.com/docs/sms/quickstart/python
Properlly installed Twilio CLI, see above URL
The URL of the data table from the CVS website.

In order to get the URL from the data table, go to the main CVS website for COVID vaccines https://www.cvs.com/immunizations/covid-19-vaccine, and select your state. Right click anywhere on the data table, and click inspect element. Scroll up, and you will see a data-url= section. For California, it's /immunizations/covid-19-vaccine.vaccine-status.CA.json?vaccineinfo. Turn that into a regular URL by putting https://www.cvs.com at the front, final URL should look like https://www.cvs.com/immunizations/covid-19-vaccine.vaccine-status.CA.json?vaccineinfo, for example.
THIS PAGE WILL 403 IF YOU TRY AND ACCESS IT WITH A REGULAR BROWSER, although the script handles it just fine.

Twilio is 0.0075 cents per text message, so with the free trial of $15 worth of credit you can do 2,000 text messages, so configure it how you like. It's currently set up to just send a push notification to a single number, but feel free to modify it and please dump your code here so I can make it better for everyone.
