from bs4 import BeautifulSoup
import requests
# Celsius and Fahrenheit
source = requests.get('https://www.bbc.co.uk/weather/0/2643743').text
soup = BeautifulSoup(source, 'lxml')

tempget = soup.find('span', {"class": "wr-value--temperature--c"})
temp = tempget.text

c = int(temp.replace('°', ''))
fah = (c * 9/5) + 32

fah = str(fah)
fah = fah + "°"

# sky

skysource = requests.get('https://weather.com/en-GB/weather/today/l/51.51,-0.13?par=google').text
skysoup = BeautifulSoup(skysource, 'lxml')

skytempget = skysoup.find('div', {"class": "today_nowcard-phrase"})
skytemp = skytempget.text

