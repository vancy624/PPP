#根據L16的程式碼來改(要複習前面的)
#抓取PTT八卦版的網頁原始碼 
#和電影版的差別:八卦版有多一個是否18歲的確認(為cookies)，故用L15章節教的程式碼會抓不到
#cookies是存放在瀏覽器內的，當瀏覽器跟ptt做連線時，瀏覽器會把cookies放在開發人員工具>network>index.html>request header內
#觀察cookies內的內容，找到over18(本次只需用到這個)

import urllib.request as req 
url="https://www.ptt.cc/bbs/Gossiping/index.html"

request=req.Request(url, headers={
    "cookie":"over18=1", #告訴ppt我們已經按過已滿18的確認
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
})

with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

#解析原始碼: 取得每篇文章的標題
import bs4 #beautifulsoup4
root=bs4.BeautifulSoup(data, "html.parser") #對html做解析
titles=root.find_all("div", class_="title") #找出所有符合條件的標籤
for title in titles: #篩掉已被刪除的文章
    if title.a !=None: #如果標題包含<a>標籤的就印出來
        print(title.a.string)

#利用中文字來取得超連結網址(一樣是使用bs4套件)
nextLink=root.find("a", string="‹ 上頁")   #找到內文是‹ 上頁的 a 標籤 
#print(nextLink) #取得a標籤內容
print(nextLink["href"]) #取得a標籤內我們要的屬性href(網址)
#上行取得的網址是"相對"網址(前面不會有https://www.ptt.cc/)

#包裝/簡潔程式碼 及 抓取多個頁面標題(用return的方式動態抓取上頁網址)
import urllib.request as req 
def getData(url): #為了抓取多個頁面標題
    request=req.Request(url, headers={
    "cookie":"over18=1", #告訴ppt我們已經按過已滿18的確認
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    import bs4 #beautifulsoup4
    root=bs4.BeautifulSoup(data, "html.parser") 
    titles=root.find_all("div", class_="title") 
    for title in titles: 
        if title.a !=None: 
            print(title.a.string)
    nextLink=root.find("a", string="‹ 上頁")  
    return nextLink["href"]

pageURL="https://www.ptt.cc/bbs/Gossiping/index.html" #初始網址
pageURL="https://www.ptt.cc"+getData(pageURL) #動態抓取上頁網址 #把前面少掉的https://...補給他
#上行意義:呼叫函式，(函式內有寫到印標題)會印出給的網址的標題內容，函式最後一行程式碼會把上頁網址return出來(用return的方式動態抓取)
print(pageURL) #印出上頁網址

#用迴圈連續執行
pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<3: #抓'3'頁標題
    pageURL="https://www.ptt.cc"+getData(pageURL) #把前面網址補給他
    count+=1
        