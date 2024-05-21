#根據標籤的ID搜尋
#driver.find_element(By.ID, "搜尋條件")
#根據標籤的任意屬性搜尋 - 透過CSS選擇器
#driver.find_element(By.CSS_SELECTOR,"[屬性名稱=屬性的值]")

#鍵盤操作
#模擬使用者輸入文字
#element=driver.find_element(搜尋欄位, "搜尋條件")
#element.send_key("輸入的文字")
#模擬使用者按下特定功能按鍵
#element.send_keys(Keys.ENTER)

#實際演練
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

#設定 chrome Driver 的執行檔路徑
options=Options()
options.add_experimental_option("detach", True) #啟動 Chrome 瀏覽器時，使瀏覽器在腳本結束後保持打開狀態。
options.chrome_executable_path="C:\Wenhuiii___code\PPP\chromedriver.exe"

#建立Driver 物件實體，用程式操作瀏覽器運作
driver=webdriver.Chrome(options=options) #顯式等待：使用 WebDriverWait 和 expected_conditions 來等待特定元素出現或變得可點擊，而不是固定的 time.sleep()，這樣可以提高代碼的可靠性和執行效率。
#連線到leetcode登入頁面
driver.get("https://leetcode.com/accounts/login/")

# 顯式等待頁面加載完成
wait = WebDriverWait(driver, 10)

#輸入帳號密碼，按下登入按鈕
#以下兩行因為無法通過人類驗證，故需改寫
# usernameInput=driver.find_element(By.ID, "id_login")
# passwordInput=driver.find_element(By.ID, "id_password")

#等待並找到指定 ID 的元素（即帳號輸入框和密碼輸入框），然後將這些元素分別賦值給 usernameInput 和 passwordInput 
usernameInput = wait.until(EC.presence_of_element_located((By.ID, "id_login")))
passwordInput = wait.until(EC.presence_of_element_located((By.ID, "id_password")))

#增加等待時間，雖然可以成功登入但仍無法通過人類驗證
time.sleep(5)
usernameInput.send_keys("vancy0624")
passwordInput.send_keys("Vancy0960")
time.sleep(5)
signinBtn=driver.find_element(By.ID, "signin_btn")
time.sleep(3)
signinBtn.send_keys(Keys.ENTER)
signinBtn.click()

#等待登入完成並連線到登入後才能取得資料的頁面
time.sleep(5)
driver.get("https://leetcode.com/problemset/")
time.sleep(3)
# 等待頁面加載完成（例如，跳轉到登錄後的首頁）
# wait.until(EC.url_changes("https://leetcode.com/accounts/login/"))

statElement=driver.find_element(By.CSS_SELECTOR,"[data-difficulty=TOTAL]")
#print(statElement.text)
columns=statElement.text.split("\n") #字串切割放入列表
print("已完成刷題數量",columns[1]) #只要第二筆資料
driver.close()