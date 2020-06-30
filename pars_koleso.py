from bs4 import BeautifulSoup
import requests
import json


def parse():
	URL = 'https://kolesa.kz/cars/mercedes-benz/?page='
	HEADERS = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36' , 'accept': '*/*'
	}
	

	response = requests.get(URL, headers = HEADERS)
	soup = BeautifulSoup(response.content, 'html.parser')
	items = soup.findAll('div', class_ ='row vw-item list-item blue a-elem')
	cars = []


	for item in items:
		cars.append({
			'title': item.find('span', class_ = 'a-el-info-title').get_text(),
			'price': item.find('span', class_ = 'price').get_text(strip = True),
			'region': item.find('div', class_ = 'list-region').get_text(strip = True),
			'link': item.find('a', class_ = 'list-link ddl_product_link').get('href'),

		})
		
		
		for car in cars:
			print(f'{car["title"]} -> Price: {car["price"]} -> Region:{car["region"]} -> Link:{car["link"]}')
			
	with open ('parser.json', 'w', encoding='utf8') as json_file:
		json.dump(cars, json_file, ensure_ascii=False, indent = 2)
		
parse()
