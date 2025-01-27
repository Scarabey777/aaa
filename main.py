import json
import requests

from bs4 import BeautifulSoup

# def result():
#     url = "https://health-diet.ru/table_calorie/"
#
#     headers = {
#             "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
#
#     }
#
#     response = requests.get(url,headers=headers)
#
#     src = response.text
#
#     with open('result.html','w',encoding='utf-8') as file:
#         file.write(src)
#
# result()

with open("result.html",'r',encoding='utf-8') as file:
    src = file.read()

soup = BeautifulSoup(src,"lxml")

all_gref = soup.find_all(class_="mzr-tc-group-item-href")

all_categories_dict = {}

for item in all_gref:
    item_text = item.text
    item_href = "https://health-diet.ru/" + item.get('href')
    # print(f'{item_text}: {item_href}')

    all_categories_dict[item_text] = item_href

with open("all_categories_dict.json","w",encoding='utf-8') as file:
    json.dump(all_categories_dict, file, indent=4,ensure_ascii=False)
