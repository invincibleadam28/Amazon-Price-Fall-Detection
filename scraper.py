import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/ASUS-GeForce-Graphics-Fortress-FX566LI-HN025T/dp/B08CY7DQH8/ref=sr_1_3?dchild=1&keywords=gaming+laptop&qid=1618063985&sr=8-3'

headers = {'User-Agents': '#Your_user_agents'}

def check_price():
	page = requests.get(URL, headers= headers)
	soup =  BeautifulSoup(page.content, 'html.parser')

	title = soup.find(id='productTitle').get_text().strip()
	price = soup.find(id='priceblock_ourprice').get_text().strip()

	price = price[2:]
	cnvt_price = ""
	for dig in price:
		if dig=='.':
			break
		if dig!=',':
			cnvt_price+=dig	
	cnvt_price = float(cnvt_price)

	if cnvt_price<50000:
		send_mail()

def send_mail():
	server =  smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('#Username','#Passoword')

	subject = 'Price fell Down!'
	body =  'Check the Amazon Link: https://www.amazon.in/ASUS-GeForce-Graphics-Fortress-FX566LI-HN025T/dp/B08CY7DQH8/ref=sr_1_3?dchild=1&keywords=gaming+laptop&qid=1618063985&sr=8-3'

	msg = f"Subject: {subject} \n \n {body}"

	server.sendmail(
		'#From_Email',
		'#To_Email',
		msg
		)
	print("Email has been sent!")

	server.quit()


while(True):
	check_price()
	sleep(60)