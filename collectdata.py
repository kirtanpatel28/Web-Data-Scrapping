#!/usr/bin/py
# Description: This script grab Amazon best sellers in biographies from amazon.com (top 100) and returned this in array
# Author: @kirtanpatel28
#
from urllib.request import urlopen as uRequest
from bs4 import BeautifulSoup as bSoup



def grab100():
	result = []		# For end result



	for pageCounter in range(1, 2):
		# Create url addres
		url = 'https://www.amazon.com/Best-Sellers-Books-Biographies/zgbs/books/2' + str(pageCounter)


		# Connect to page
		connect  = uRequest(url)
		response = connect.read()
		connect.close()



		# Parse response and grab data
		pRespone 		= bSoup(response, 'html.parser')
		bookContainer 	= pRespone.findAll('li', {'class':'book'})
		booksContent 	= []



		# Grab data
		for book in bookContainer:
			bookTitle 		= book.findAll('a', {'class':'bookTitle'})[0].text
			bookAuthor		= book.findAll('a', {'itemprop':'name'})[0].text
			bookRank 		= book.findAll("div", {"class":"sprite"})[0].text

			bookStatsBox 	= book.findAll("div", {"class":"book-stats"})[0].findAll("span", {"class":"font-szary-4a"})
			bookReaders 	= bookStatsBox[0].text
			bookOpinions 	= bookStatsBox[1].text
			bookRate 		= bookStatsBox[2].text


			# Delete reserved characters
			reserved_chars = ('★', '⬈', '⬊', '⬌','\'', '\"')
			reserved_list = [bookTitle, bookAuthor, bookRank]
			free_list = []

			for element in reserved_list:
				for rChar in reserved_chars:
					if rChar in element:
						element = element.replace(rChar, '')
				free_list.append(element)


			# Add to end result
			result.append((free_list[0], free_list[1], free_list[2], bookReaders, bookOpinions, bookRate))



	print('Successful download data from website\n\n')
	return result