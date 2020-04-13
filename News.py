# importing requests package
# newsAPI key: 2ca69046270d47dd9594e150f9698bc1
# swe = https://newsapi.org/s/sweden-business-news-api
# uk = https://newsapi.org/s/uk-business-news-api
# us = https://newsapi.org/s/us-business-news-api

import requests
from datetime import date

print("Here's today's business news.")

today = date.today()
print("Date:", today, "\n")

def UsaNews():

	# Usa news api
	usa_main_url = "http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=2ca69046270d47dd9594e150f9698bc1"

	# fetching data in json format
	open_usa_page = requests.get(usa_main_url).json()

	# getting all articles in a string article
	usa_article = open_usa_page["articles"]

	# empty list which will
	# contain all trending news
	usa_results = []

	for ar in usa_article:
		usa_results.append(ar["title"])

	for i in range(len(usa_results)):

		# printing all trending news
		print(i + 1, usa_results[i])

def SweNews():

	# Swe news api
	swe_main_url = "http://newsapi.org/v2/top-headlines?country=se&category=business&apiKey=2ca69046270d47dd9594e150f9698bc1"

	# fetching data in json format
	open_swe_page = requests.get(swe_main_url).json()

	# getting all articles in a string article
	swe_article = open_swe_page["articles"]

	# empty list which will
	# contain all trending news
	swe_results = []

	for ar in swe_article:
		swe_results.append(ar["title"])

	for i in range(len(swe_results)):

		# printing all trending news
		print(i + 1, swe_results[i])

def UkNews():

	# Uk news api
	uk_main_url = "http://newsapi.org/v2/top-headlines?country=gb&category=business&apiKey=2ca69046270d47dd9594e150f9698bc1"

	# fetching data in json format
	open_uk_page = requests.get(uk_main_url).json()

	# getting all articles in a string article
	uk_article = open_uk_page["articles"]

	# empty list which will
	# contain all trending news
	uk_results = []

	for ar in uk_article:
		uk_results.append(ar["title"])

	for i in range(len(uk_results)):

		# printing all trending news
		print(i + 1, uk_results[i])

# Driver Code
if __name__ == '__main__':

# function call
	#print(UsaNews(), SweNews(), UkNews())
	print("US HEADLINES")
	print(UsaNews())
	print("\n")
	print("SWE HEADLINES")
	print(SweNews())
	print("\n")
	print("UK HEADLINES")
	print(UkNews())
