import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get(
    'https://forecast.weather.gov/MapClick.php?lat=35.07486000000006&lon=-90.52145999999999#.YHaLUxLBXb0')
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.find_all('img'))

week = soup.find(id='seven-day-forecast-body')
items = (week.find_all(class_='tombstone-container'))

# print(items[0])

period_names = [item.find(class_='period-name').get_text() for item in items]
print(period_names)
shortDesc = [item.find(class_='short-desc').get_text() for item in items]
print(shortDesc)
temp = [item.find(class_='temp').get_text() for item in items]
print(temp)

weather = pd.DataFrame({
    'period': period_names,
    "short-desc": shortDesc,
    'temp': temp
})

print(weather)
weather.to_csv('resultweather.csv')
