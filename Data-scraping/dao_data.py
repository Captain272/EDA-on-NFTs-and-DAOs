# import requests

# x = requests.get('https://www.daohq.co/daos/yog8-dao')

# print(x.json)
# print(x.status_code)
# print(x.headers)
# print(x.content)
# print(x.headers)

from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://daodao.io/api/v0/top-daos?limit={a}&offset={b}&order=most_raised_all_time'

print(url.format(a=2,b=0))

page = urlopen(url.format(a=2,b=0))
# html = page.read().decode("utf-8")
# print(html.json())



# soup = BeautifulSoup(html, "html.parser")

# div_bs4 = soup.find('div', class_ = "flex w-full mt-4 py-6 border-y border-gray-300")
  
# print(div_bs4.string)
# print(soup.get_text())
