# importing libraries
from bs4 import BeautifulSoup
import requests



URL= ["https://www.amazon.com/Skytech-Chronos-Mini-Gaming-Desktop/dp/B09R1V8X6F/ref=sr_1_3?crid=3SR6H1VFJ6DC&keywords=pc&qid=1674236191&sprefix=p%2Caps%2C157&sr=8-3",
	  "https://www.amazon.com/Skytech-Shadow-Gaming-PC-Desktop/dp/B09QY2PXP1/ref=sr_1_6?crid=3SR6H1VFJ6DC&keywords=pc&qid=1674238515&sprefix=p%2Caps%2C157&sr=8-6&th=1",
	  "https://www.amazon.com/HP-Processor-Bluetooth-Pre-Built-TG01-2070/dp/B09HKHDV14/ref=sr_1_12?crid=3SR6H1VFJ6DC&keywords=pc&qid=1674238660&sprefix=p%2Caps%2C157&sr=8-12"]


def main(URL):
	# opening our output file in append mode
	file = open("out.csv", "a")

	# specifying user agent, You can use other user agents
	# available on the internet
	HEADERS = ({'User-Agent':
				'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
				'(KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
				'Accept-Language': 'en-US, en;q=0.5'})

	# Making the HTTP Request
	webpage = requests.get(URL, headers=HEADERS)

	# Creating the Soup Object containing all data
	soup = BeautifulSoup(webpage.content, "lxml")
	try:
		title = soup.find("span", attrs={"id": 'productTitle'})
		title_value = title.string
		title_string = title_value.strip().replace(',', '')
	except AttributeError:
		title_string = "NA"

	print("Product Tilte= ", title_string)

	file.write(f"{title_string},")

	try:
		price = soup.find("span", attrs={'class': 'a-offscreen'}).string.strip().replace(',', '')
	except AttributeError:
		price = "NA"

	print("Product price = ", price)

	file.write(f"{price}, ")

	try:
		rating = soup.find("i", attrs={'class': 'a-icon a-icon-star a-star-4-5'}).string.strip().replace(',', '')
	except AttributeError:
		try:
			rating = soup.find("span", attrs={'class': 'a-icon-alt'}).string.strip().replace(',', '')
		except:
			rating = "NA"

	print("Overall rating = ", rating)

	file.write(f"{rating}, ")

	try:
		review_count = soup.find("span", attrs={'id': 'acrCustomerReviewText'}).string.strip().replace(',', '')
	except AttributeError:
		review_count = "NA"

	print("Total reviews = ", review_count)

	file.write(f"{review_count}, ")

	try:
		available = soup.find("div", attrs={'id': 'availability'})
		available = available.find("span").string.strip().replace(',', '')
	except AttributeError:
		available = "NA"

	print("Availability = ", available)

	file.write(f"{available},\n")

	file.close()


if __name__ == '__main__':
	for ur in URL:
		main(ur)

