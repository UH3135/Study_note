from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import re
import time

df = pd.DataFrame(columns=['name', 'naverURL'])
keyword = "구리 잉꼬칼국수"

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 로그 비활성화
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) # 드라이버 실행

naver_map_search_url = f'https://map.naver.com/v5/search/{keyword}/place'  
driver.get(naver_map_search_url)
time.sleep(2) 
# 검색 프레임 변경
# driver.switch_to.frame("searchIframe")
# time.sleep(1) 

driver.close()

# res = driver.page_source  # 페이지 소스 가져오기
# soup = BeautifulSoup(res, 'html.parser')  # html 파싱하여  가져온다

# # frame 변경 메소드
# def switch_frame(frame):
#     driver.switch_to.default_content()  # frame 초기화
#     driver.switch_to.frame(frame)  # frame 변경
#     res
#     soup

    # 검색 url 만들기
    
     
    
    # try:     
    #     #식당 정보가 있다면 첫번째 식당의 url을 가져오기
        
    #     if len(driver.find_elements(By.XPATH, '//*[@id="_pcmap_list_scroll_container"]/ul/li')) != 0:   
    #         #식당 정보 클릭        
    #         driver.execute_script('return document.querySelector("#_pcmap_list_scroll_container > ul > li:nth-child(1) > div.ouxiq > a:nth-child(1) > div").click()')
    #         time.sleep(2)
            
    #         # 검색한 플레이스의 개별 페이지 저장
    #         tmp = driver.current_url  
    #         res_code = re.findall(r"place/(\d+)", tmp)
    #         final_url = 'https://pcmap.place.naver.com/restaurant/'+res_code[0]+'/review/visitor#' 
        
    #         print(final_url)
    #         df['naverURL'][i]=final_url 
        
    # except: 
    #     df['naverURL'][i]= ''
    #     print('none') 
    
