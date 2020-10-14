from .amazon import scrap_amazon
from .mediamarkt import scrap_mediamarkt
from .pccomponentes import scrap_pccomponentes

__services = {
	'amazon.es': scrap_amazon,
	'amazon.com': scrap_amazon,
	'mediamarkt.es': scrap_mediamarkt,
	'pccomponentes.com': scrap_pccomponentes
}

def scrap(url):
	for key in __services.keys():
		if key in url:
			return __services[key](url)
		# else:
		# 	print(key, url)

	return None
