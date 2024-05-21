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
driver.get("https://www.chingoods.co/users/sign_in")

# 顯式等待頁面加載完成
wait = WebDriverWait(driver, 10)

#輸入帳號密碼，按下登入按鈕
usernameInput=driver.find_element(By.ID, "field-1")
passwordInput=driver.find_element(By.ID, "field-2")

#等待並找到指定 ID 的元素（即帳號輸入框和密碼輸入框），然後將這些元素分別賦值給 usernameInput 和 passwordInput 
# usernameInput = wait.until(EC.presence_of_element_located((By.ID, "login-email_input")))
# passwordInput = wait.until(EC.presence_of_element_located((By.ID, "login-password_input")))

#增加等待時間，雖然可以成功登入但仍無法通過人類驗證
usernameInput.send_keys("bright_62_53@yahoo.com.tw")
passwordInput.send_keys("Vancy0624")
time.sleep(5)
# 按鈕元素並沒有 id 屬性，而是有一個 data-e2e-id 屬性。 find_element 方法不能直接使用 By.ID 定位 data-e2e-id 屬性。
# signinBtn=driver.find_element(By.ID, "login-submit_button")
# signinBtn.send_keys(Keys.ENTER)
# signinBtn.click()

#應該使用 By.CSS_SELECTOR #driver.find_element(By.CSS_SELECTOR,"[屬性名稱=屬性的值]")
signinBtn = driver.find_element(By.CSS_SELECTOR, "[data-e2e-id=login-submit_button]")
signinBtn.click()



# time.sleep(3)
# 等待頁面加載完成（例如，跳轉到登錄後的首頁）
# wait.until(EC.url_changes("https://www.chingoods.co/orders"))