from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import List
import time

area = "구리"
place = "잉꼬칼국수"
n = 5
url = "https://map.naver.com/"

def switch_left():
    driver.switch_to.parent_frame()
    iframe = driver.find_element(By.XPATH, '//*[@id="searchiframe"]')
    driver.switch_to.frame(iframe)

def switch_right():
    driver.switch_to.parent_frame()
    iframe = driver.find_element(By.XPATH,'//*[@id="entryIframe"]')
    driver.switch_to.frame(iframe)

 # driver 설정
driver = webdriver.Chrome()
driver.get(url)

# search
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "input_search"))
)
search_box = driver.find_element(By.XPATH, f"//input[@class='input_search']")

search_box.send_keys(place)
search_box.send_keys(Keys.RETURN)
time.sleep(5)

switch_left()

div_tag = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@class="flicking-camera"]'))
)

div_tag.find_element(By.CLASS_NAME,'CHC5F').find_element(By.XPATH, ".//a/div/div/span").click()


print(div_tag.text)


# div_tags = WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.CLASS_NAME, 'XtBbS'))
# )

# # 각 요소의 텍스트를 출력
# for div in div_tags:
#     print(div.text)
# time.sleep(10)
# print(div_tag.get_attribute('innerHTML'))
# iframe = WebDriverWait(driver, 10).until(
#     EC.presence_of_all_elements_located((By.ID, "entryIframe"))
# )
# driver.switch_to.frame(iframe)


# def crawling_reviews(count: int, driver: webdriver.Chrome) -> List[str]:
#     data = []
#     divs = driver.find_elements(By.CLASS_NAME, review_div_class)
#     for div in divs:
#         data.append(div.text)

#     return data
