#滾動視窗
# 載入Selenium 相關模組
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
#設定 chrome Driver 的執行檔路徑
options=Options()
options.chrome_executable_path="C:\Wenhuiii___code\PPP\chromedriver.exe"
#建立Driver 物件實體，用程式操作瀏覽器運作
driver=webdriver.Chrome(options=options)
#連線到LinkedIn 工作搜尋網頁
driver.get("https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0")
#捲動視窗並等待瀏覽器載入更多內容
n=0
while n<3:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #捲動視窗到底部
    time.sleep(5) #等待5秒鐘
    n+=1
#取得網頁中工作的標題
titleTags=driver.find_elements(By.CLASS_NAME, "base-search-card__title")

#for迴圈將標題一個一個印出
for titleTag in titleTags:
    print(titleTag.text)

#driver.close() #沒有此行瀏覽器也會自動關閉，可能是vscode本身程式執行完就會關掉