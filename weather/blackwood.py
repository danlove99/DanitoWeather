from bs4 import BeautifulSoup
import requests


source = requests.get('https://www.bbc.co.uk/weather/3345317').text
soup = BeautifulSoup(source, 'lxml')

tempget = soup.find('span', {"class": "wr-value--temperature--c"})
temp = tempget.text

c = int(temp.replace('°', ''))
fah = (c * 9/5) + 32

fah = str(fah)
fah = fah + "°"

# sky

skysource = requests.get('https://weather.com/en-GB/weather/today/l/51.67,-3.20?par=google').text
skysoup = BeautifulSoup(skysource, 'lxml')

skytempget = skysoup.find('div', {"class": "today_nowcard-phrase"})
skytemp = skytempget.text