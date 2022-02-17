from bs4 import BeautifulSoup
import requests
from datetime import datetime
import os

start_time = datetime.now()

def FindURLs(url):
	page = requests.get(url)

	soup = BeautifulSoup(page.text, 'html.parser')

	links = []

	all_p = soup.findAll('p')
	head = soup.find('h1', class_='firstHeading mw-first-heading')

	for p in all_p:
		if p.findAll('a') is not None:
			link = p.findAll('a')
			for l in link:
				if l.findAll('a') is not None:
					link_text = l.text

					is_huynia = False

					for simbol in link_text:
						if simbol == '[' or simbol == ']':
							link_text = link_text.replace(simbol, '')
					
					if len(link_text) <= 2:
						is_huynia = True
					
					try:
						if is_huynia == False:
							href = 'https://ru.wikipedia.org' + str(l.get('href'))
							links.append([head.text, href])
						else:
							...
					except:
						...

	return links

try:
	os.remove("follows.txt")
except:
	...

#url = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%B2%D0%B8%D0%BD%D1%8B%D0%B5'
url = 'https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D0%95%D0%B2%D0%BA%D0%BB%D0%B8%D0%B4%D0%B0'

links_first = []
links_second = []
links_third = []
links_forth = []

links_first = FindURLs(url)

for link in links_first:
	try:
		print(link[0] + ' - ' + link[1])
		with open("follows.txt", "a") as file:
			file.write(link[0] + ' - ' + link[1] + '\n')

		links_second = FindURLs(link[1])
	
		for link in links_second:
			print('		1|----' + str(link[0]) + ' - ' + str(link[1]))
			with open("follows.txt", "a") as file:
				file.write('		1|----' + str(link[0]) + ' - ' + str(link[1]) + '\n')

			links_third = FindURLs(link[1])
		
			for link in links_third:
				print('				2|----' + str(link[0]) + ' - ' + str(link[1]))
				with open("follows.txt", "a") as file:
					file.write('				2|----' + str(link[0]) + ' - ' + str(link[1]) + '\n')

				links_forth = FindURLs(link[1])
				
				try:
					print('					3|----' + str(links_forth[0][0]))
					with open("follows.txt", "a") as file:
						file.write('					3|----' + str(links_forth[0][0]) + '\n')
				except:
					...
	except:
		...

print(datetime.now() - start_time)

with open("follows.txt", "a") as file:
	file.write(str(datetime.now() - start_time))
