from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

from collections import defaultdict

class Billboard:

	URL = {'greatest_women': 'https://www.billboard.com/charts/greatest-billboard-200-women-artists',
			'greatest_country_artists': 'https://www.billboard.com/charts/greatest-country-artists',
			'greatest_hot_100': 'https://www.billboard.com/charts/greatest-hot-100-artists',
			'greatest_pop_artists': 'https://www.billboard.com/charts/greatest-of-all-time-pop-songs-artists',
			'greatest_hot_latin': 'https://www.billboard.com/charts/greatest-hot-latin-songs-artists',
			'greatest_hiphop': 'https://www.billboard.com/charts/greatest-r-b-hip-hop-artists'}

	def __init__(self):

		self.ARTISTS = set()

	def get(self, what):
		"""
		got to the right page on the RIAA web site and grab all artist names
		"""

		# ChromeDriver is 2.38 available at https://chromedriver.storage.googleapis.com/2.38/chromedriver_mac64.zip
		self.DRIVER = webdriver.Chrome('webdriver/chromedriver')

		self.DRIVER.get(Billboard.URL[what])

		WebDriverWait(self.DRIVER, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "copyright__paragraph")))

		for _ in self.DRIVER.find_elements_by_class_name('chart-row__artist'):
			self.ARTISTS.add(_.text.lower().strip())

		self.DRIVER.close()

		return self

if __name__ == '__main__':

	b = Billboard()
	b.get('greatest_women')
	b.get('greatest_country_artists')
	b.get('greatest_hot_100')
	b.get('greatest_pop_artists')
	b.get('greatest_hot_latin')
	b.get('greatest_hiphop')

	with open('billboard_artists.txt','w') as f:
		for a in b.ARTISTS:
			f.write(f'{a}\n')



	