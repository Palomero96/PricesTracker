import os

import pandas as pd
import numpy as np
from controllers.scrap import scrap

__csv_dir = 'csv/'
__products_file = 'csv/products.csv'
__prices_file = 'csv/prices.csv'

def main():
	# Create csv dir if not present

	# Create dataframe to save all the collected data
	if os.path.isfile(__prices_file) and not os.stat(__prices_file).st_size == 0:
		prices_df = pd.read_csv(__prices_file)
	else:
		prices_df = pd.DataFrame(
			columns=['name', 'kind', 'shop', 'url', 'price', 'date']
		)
	prices_df.set_index(['url','date'])
	prices_df["price"].replace('????',np.nan, inplace=True)


	# Get dataframe to read products to search; exit if not exists
	if os.path.isfile(__products_file):
		products_df = pd.read_csv(__products_file)
	else:
		print('File csv/products.csv missing! Can\'t search products if you don\'t provide any :(')
		exit()

	# Iterate products
	for index, row in products_df.iterrows():
		kind = row['kind']
		url = row['url']

		info = scrap(url)

		if info is not None:
			# Add kind
			info['kind'] = kind

			# Clean name
			info['name'] = info['name'] if info['name'] is not None else 'NaN'
			info['name'] = info['name'].replace('\n', '')
			info['name'] = info['name'].replace('"', '\'')

			# Clean price
			info['price'] = info['price'] if info['price'] is not None else 'NaN'
			info['price'] = info['price'].replace('€', '')
			info['price'] = info['price'].replace(' ', '')
	
			prices_df = prices_df.append(info, ignore_index=True)

	#Change price column type
	prices_df["price"] = prices_df["price"].astype(float)
	# Save prices
	prices_df = prices_df.drop_duplicates()
	prices_df.to_csv(__prices_file, index=False)

if __name__ == '__main__':
	main()
