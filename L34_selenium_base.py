# 載入Selenium 相關模組
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#設定 chrome Driver 的執行檔路徑
options=Options()
options.chrome_executable_path="C:\Wenhuiii___code\PPP\chromedriver.exe"
#建立Driver 物件實體，用程式操作瀏覽器運作
driver=webdriver.Chrome(options=options)
driver.maximize_window() #視窗最大化
driver.get("https://www.google.com/") #網頁連線
driver.save_screenshot("googleweb.png") #螢幕截圖
driver.get("https://www.ntu.edu.tw/") #網頁連線
driver.save_screenshot("ntuweb.png") #螢幕截圖
driver.close()