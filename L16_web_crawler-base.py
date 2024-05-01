#抓取ppt電影版的網頁原始碼 
#需要讓自己像一個正常的使用者，換句話說，要讓ptt伺服器認為我們是正常的使用者
#故程式碼與之前教的網路連線不同(要多加Request)
import urllib.request as req 
url="https://www.ptt.cc/bbs/movie/index.html" #網路連線語法(以下三行)
#建立一個Request物件，附加Request headers的資訊
#headers怎麼找:開啟網頁>開發人員工具>找到index.html>requests>User-Agent

request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
#解析原始碼: 取得每篇文章的標題
#要使用第三方套件:beautifulsoup4
import bs4 #beautifulsoup4
root=bs4.BeautifulSoup(data, "html.parser") #對html做解析
#print(root.title) #root代表整份網頁,title代表網頁的標題
#print(root.title.string) #title+string 標籤裡的文字
titles=root.find("div", class_="title") #尋找class="title"的div標籤 #find只會幫我們找到一個符合條件的標籤
#print(titles) 
#print(titles.a.string) #標籤內又被一個標籤<a>包住，想要只抓取<a>裡面的文字時
titles=root.find_all("div", class_="title") #找出所有符合條件的標籤
print(titles) 
for title in titles: #篩掉已被刪除的文章
    if title.a !=None: #如果標題包含<a>標籤的就印出來
        print(title.a.string)
    