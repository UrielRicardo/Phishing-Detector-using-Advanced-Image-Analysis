import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import re
import os
import sys
import requests
import subprocess
from bs4 import BeautifulSoup

site = str(sys.argv[1])

if not (re.search('http', site, re.IGNORECASE)):
        site = 'http://'+site
response = requests.get(site)

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')

urls = [img['src'] for img in img_tags]


for url in urls[0:5]:
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
    if 'http' not in url:
        url = '{}{}'.format(site, url)
    print(url)
    response = requests.get(url)
    print(url)
    os.system('python Aplicacoes/ProjectSharingan/detect.py web-uri ' +url)
