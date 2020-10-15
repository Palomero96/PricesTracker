import requests

from datetime import date

from .common import parse_page

def scrap_mediamarkt(url):
	def find_name(page):
		name = page.find('h1', itemprop='name')

		if name is not None:
			name = name.get_text()

		return name

	def find_price(page):
		price = page.find('meta', itemprop='price')

		if price is not None:
			price = price['content']

		return price

	page_fields = parse_page(url, fields=[
		('name', find_name),
		('price', find_price)
	])

	return {
		'name': page_fields['name'],
		'kind': '',
		'shop': 'Mediamarkt',
		'url': url,
		'price': page_fields['price'],
		'date': date.today().strftime("%Y-%m-%d")
	}
