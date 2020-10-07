import requests

from datetime import date

from scrap.common import parse_page

def scrap_amazon(url):
	def find_name(page):
		name = page.find('span', id='productTitle')

		if name is not None:
			name = name.get_text()

		return name

	def find_price(page):
		price = page.find('span', id='priceblock_ourprice')

		if price is not None:
			price = price.get_text()

		return price

	page_fields = parse_page(url, fields=[
		('name', find_name),
		('price', find_price)
	], parser='lxml')

	return {
		'name': page_fields['name'],
		'kind': '',
		'shop': 'Amazon',
		'url': url,
		'price': page_fields['price'],
		'date': date.today().strftime('yyy-mm-dd')
	}
