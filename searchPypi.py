# This program opens the top 5 search results on pypi website, from the keywords passed through command line

#! python3
# searchpypi.py  - Opens several search results.
import requests, sys, webbrowser, bs4
print("Searching...")

# scraping the pypi website and searching for the keywords from the command line
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))

# checking if the scraping was successful
res.raise_for_status()

# parsing the html
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# getting the element using the '.package-snippet' id
linkElems = soup.select('.package-snippet')

# running the loop either 5 or less times depending on the search results returned
numOpen = min(5, len(linkElems))
for i in range(numOpen):

    # opening the top search results in new tabs
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)