import urllib.request
import re

url = 'http://finance.naver.com/item/main.nhn?code = 005930'
html = urllib.request.urlopen(url)
html_contents = str(html.read().decode('ms949'))

stock_results = re.findall("(\<d1 class=\'blind'\>)([\s\S] + ?)(\<\/dI\>)", html_contents)
print(stock_results)

samsung_stock = stock_results[0]
samsung_index = samsung_stock[1]

index_list = re.findall("(\<dd\>)([\s\S] + ?)(\<\/dd\>)", samsung_index)

for index in index_list:
    print(index[1])
    


