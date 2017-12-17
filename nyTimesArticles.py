# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 12:41:56 2017

@author: cwickham
"""
''' Find all articles home page NYT'''

import requests
from bs4 import BeautifulSoup as bsoup

url = 'https://www.nytimes.com/'
s = requests.Session()
page = s.get(url)

bs = bsoup(page.text, 'lxml')

for x in bs.findAll('h2',{'class':'story-heading'}):
    print(x.text.strip())