import requests

from bs4 import BeautifulSoup

__default_header = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}

def parse_page(url, fields=[], header=None, parser='html.parser'):
	if header is None:
		header = __default_header

	# Getting the page
	page = requests.get(url, headers=header)

	# Creating BeautifulSoup Object
	soup = BeautifulSoup(page.content, parser)

	# Get fields
	return_fields = {}

	for element_name, element_query in fields:
		return_fields[element_name] = element_query(soup)

	return return_fields
