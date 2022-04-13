import requests

def getNews(country, apiKey='034e0474006b4cc6b67c8809ee9d8ba2'):
  url=f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={apiKey}'
  r=requests.get(url)
  content=r.json()
  articles=content['articles']
  return articles
              
articles=getNews(country='gb')
results=[]
for article in articles:
  print(f"TITLE: '{article['title']}\nDESCRIPTION: {article['description']}")


#print(getNews(topic='space',fromDate='2022-4-12',toDate='2022-4-13'))
