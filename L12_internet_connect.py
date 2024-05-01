#網路連線
import urllib.request as request 
src="https://www.ntu.edu.tw/" #網路連線語法(以下三行)
with request.urlopen(src) as response:
    #data=response.read() #取得台灣大學網站的"原始碼" (HTML、CSS、JS)
    #要解讀把原始碼轉成中文改寫成下面
    data=response.read().decode("utf-8")
print(data)

#取得台北市政府公開資料
import urllib.request as request #step1:載入模組
import json #step2:為了做json資料解析，載入json資料模組
src="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire" 
with request.urlopen(src) as response:
    data=json.load(response) #利用json模組處理json資料格式
# print(data)
#解讀資料欄位(要先自己觀察資料畫面)-將公司名稱列表出來
clist=data["result"]["results"] #此寫法來自程式桿(前面一兩行有架構)
print(clist)
for company in clist:
    print(company["公司名稱"])
#將讀出的資料(公司名稱)寫入自己的文件中
clist=data["result"]["results"] 
with open("data1.txt", "w", encoding="utf-8") as file: #整合上一章節的功能
    for company in clist:
        file.write(company["公司名稱"]+"\n") 



