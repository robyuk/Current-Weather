import requests
from os import getenv
# Get 5-day weather forcast for {city} and append to data.txt file
city='Boston,uk'

# Get API key by signing up at openweathermap.org
def getWeather(cityname, apiKey=getenv('apiKey')):
  url=f'https://api.openweathermap.org/data/2.5/forecast?q={cityname}&appid={apiKey}&units=metric'
  r=requests.get(url)
  content=r.json()
  
  result=content['cod']
  if not result == '200':
    print(f"HTML code {result} was returned")
    exit(1)
    
  forcasts=content['list']
  return forcasts
              
forcasts=getWeather(cityname=city)
f=open('data.txt','a')
  
city=city.split(',')[0]  #Get just the city name
for forcast in forcasts:
  temp=forcast['main']['temp']
  dt=forcast['dt_txt']
  condition=forcast['weather'][0]['description']
  f.write(f"{city}, {dt}, {temp}, {condition}\n")

f.close()



#print(getNews(topic='space',fromDate='2022-4-12',toDate='2022-4-13'))
