#Python VERSION:::: 3.6

#Author

#From Github account : nishu88

# pip install beautifulsoup4

#Refer ---------- https://www.youtube.com/watch?v=0snOcBQ3I0g ---------

#--------- https://pypi.org/project/BeautifulSoup/ ---------------


"""import requests
from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser(description='Get Google Count.')
parser.add_argument('word', help='word to count')
args = parser.parse_args()

r = requests.get('http://www.google.com/search',
                 params={'q':'"'+args.word+'"',
                         "tbs":"li:1"}
                )

soup = BeautifulSoup(r.text)
print soup.find('div',{'id':'resultStats'}).text
"""
import requests
from bs4 import BeautifulSoup
import lxml

search = "django framework"

r = requests.get("https://www.google.com/search", params={'q':search})

soup = BeautifulSoup(r.text, "lxml")
res = soup.find("div", {"id": "resultStats"})
print res.text
