#網頁爬蟲:使用程式爬取網頁中HTML格式資料

#取得滿足條件的"一個"標籤 (html內的一個標籤，在這裡稱webElement)
#driver.find_element(搜尋欄位, "搜尋條件")
#取得滿足條件的"所有"標籤 webElement List
#driver.find_elements(搜尋欄位, "搜尋條件")

#根據標籤的class屬性搜尋
#driver.find_element(By.CLASS_NAME, "搜尋條件")
#driver.find_elements(By.CLASS_NAME, "搜尋條件")

#根據連結標籤的文字搜尋
#driver.find_element(By.LINK_TEXT, "搜尋條件")
#driver.find_elements(By.LINK_TEXT, "搜尋條件")

#取得標籤的內部文字
#element=driver.find_element(搜尋欄位, "搜尋條件")
#element.text

#取得標籤的某個屬性
#element=driver.find_element(搜尋欄位, "搜尋條件")
#element.get_attribute("屬性名稱")

#模擬使用者點擊標籤
#element=driver.find_element(搜尋欄位, "搜尋條件")
#element.click()



# 載入Selenium 相關模組
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
#設定 chrome Driver 的執行檔路徑
options=Options()
options.chrome_executable_path="C:\Wenhuiii___code\PPP\chromedriver.exe"
#建立Driver 物件實體，用程式操作瀏覽器運作
driver=webdriver.Chrome(options=options)
#連線到ptt股票版
driver.get("https://www.ptt.cc/bbs/Stock/index.html")
# print(driver.page_source) #取得網頁原始碼
#取得股票版中的文章標題
tags=driver.find_elements(By.CLASS_NAME, "title") #搜尋class屬性是title的所有標籤 #By 是selenium類別，需引入才可使用 L28
for tag in tags: 
    print(tag.text)

#取得上一頁的文章標題
link=driver.find_element(By.LINK_TEXT, "‹ 上頁")
link.click() #模擬使用者點擊連結標籤
tags=driver.find_elements(By.CLASS_NAME, "title") #搜尋class屬性是title的所有標籤 #By 是selenium類別，需引入才可使用 L28
for tag in tags: 
    print(tag.text)

driver.close()