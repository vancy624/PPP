#AJAX : 又稱XHR，網頁前端的JavaScript的程式技術 
#用L16的程式碼為基礎
#使用AJAX技術的網頁 > 開發人員工具+重整 > network > Fetch/XHR > 重整 > 許多檔案會跑出來
#跑出的檔案之意義:此網站有跑一些JavaScript的程式，去跟網站伺服器做連線(AJAX技術)
#此章為教學如何找出文章標題
#點跑出的檔案>用preview(整理過的) or response(原始的)確認好是我們要找的資料>Headers>request URL複製網址

#抓取pchome文章標題
import urllib.request as req 
url="https://ecapi-cdn.pchome.com.tw/fsapi/ecshop/composition/sign/v1/food/data" #網路連線語法(以下三行)
#建立一個Request物件，附加Request headers的資訊

request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
})

with req.urlopen(request) as response:
    data=response.read().decode("utf-8") #根據觀察該網址，取得的網址資料是JSON格式
#解析原始碼: 取得每篇文章的標題
#不使用第三方套件:beautifulsoup4 ->BS4是解html的格式文件的
#解析json格式資料，取得每篇文章標題
import json
#data=data.replace("要被換的字串","替換的字串") #替換字串
data=json.loads(data) #把原始的資料解析成字典/列表的表示形式

#取得json檔之標題之列表 
flist = data["brand1"]["Blocks"][0]["Nodes"] #key key key key
# print(flist[0].keys()) #測試到Nodes這層的value有哪些
#print((data["brand1"]["Blocks"][0]["Nodes"])[0].keys()) #與上行意義相同
# print(flist[0]["Link"].keys()) #nodes內的value"Link"也是一個字典，測試Link內的key有哪些
# print(flist[1]["Link"].keys())
# print(flist[2]["Link"].keys())
# for post in flist: 
#     print(post["Link"].keys()) 

# for goods in flist:
#     print(goods["Link"]["Text"])#link已經算是nodes內的value，故不能寫在上面[Nodes]後

# print(flist[2]["Link"]["Text"],"$"+flist[2]["Link"]["Text1"])
# print(flist[0]["Link"]["Text"],"$"+flist[0]["Link"]["Text1"]) #error 因為flist[0]沒有test1
# n=2

# while n<18: #在知道有幾筆資料的情況下
#     print(flist[n]["Link"]["Text"],"$"+flist[n]["Link"]["Text1"])
#     n+=1

for x in flist[2:]: #可以不用知道資料有幾筆
    print(x["Link"]["Text"],"$"+x["Link"]["Text1"])




