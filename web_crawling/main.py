import requests
import bs4

url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
place = "구리 잉꼬칼국수"

http = requests.get(url+place)

html = bs4.BeautifulSoup(http.text, "html.parser")
result = html.find_all("li", {"class": "pui__X35jYm place_apply_pui EjjAW"})
print(html)