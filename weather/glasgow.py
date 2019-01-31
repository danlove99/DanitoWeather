from bs4 import BeautifulSoup
import requests


source = requests.get('https://www.bbc.co.uk/weather/0/2648579').text
soup = BeautifulSoup(source, 'lxml')

tempget = soup.find('span', {"class": "wr-value--temperature--c"})
temp = tempget.text

c = int(temp.replace('°', ''))
fah = (c * 9/5) + 32

fah = str(fah)
fah = fah + "°"

# sky

skysource = requests.get('https://weather.com/en-GB/weather/today/l/d9c3fa2c79668c489b8481d623991bdda4253177a2789d05a13dde82eadac46a').text
skysoup = BeautifulSoup(skysource, 'lxml')

skytempget = skysoup.find('div', {"class": "today_nowcard-phrase"})
skytemp = skytempget.text