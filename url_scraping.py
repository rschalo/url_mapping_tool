from beautifulsoup4 import bs4
import requests

res = requests.get('https://www.thermofisher.com/us/en/home/life-science/protein-biology/protein-expression.html')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)
soup.select('ul .content')

print(soup)
