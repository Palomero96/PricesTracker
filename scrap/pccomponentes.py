import requests

from datetime import date

from scrap.common import parse_page

def scrap_pccomponentes(url):
	def find_name(page):
		name = page.find('div', { 'class': 'articulo' })

		if name is not None:
			name = name.find('strong').get_text()

		return name

	def find_price(page):
		price = page.find('div', id='precio-main')

		if price is not None:
			price = price['data-price']
		# else:
		# 	price = page.find(id='precio-main').get_text()

		return price

	page_fields = parse_page(url, fields=[
		('name', find_name),
		('price', find_price)
	])

	return {
		'name': page_fields['name'],
		'kind': '',
		'shop': 'PC Componentes',
		'url': url,
		'price': page_fields['price'],
		'date': date.today().strftime('yyy-mm-dd')
	}
