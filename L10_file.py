# 儲存檔案 打開->執行操作->關閉
#格式：file=open("檔案路徑",mode="開啟模式")(檔案不存在沒關係，此方式會直接建檔)
file=open("data.txt", mode="w") #開啟：打開檔案，執行write 
file.write("hello file\nSecond Line") #操作：寫入文字 
file.close() #關閉

#寫入中文會出現亂碼，如何解決 
#格式：file=open("檔案路徑",mode="開啟模式",encoding="指定編碼")
file=open("data.txt", mode="w", encoding="utf-8") 
file.write("測試中文\n成功") #操作：寫入文字 
file.close() #關閉

#最佳實務 with open 不用寫關閉，此寫法可自動建立及關閉
with open("data.txt", mode="w", encoding="utf-8") as file:
    file.write("測試中文\n成功")

#讀取檔案 (讀取"已存在"的檔案)
with open("data.txt", mode="r", encoding="utf-8") as file:
    data=file.read()
print(data)

#讀取檔案(要把檔案中的數字，一行一行讀取後再全部加起來)
with open("data.txt", mode="w", encoding="utf-8") as file:
    file.write("5\n3")
sum=0
with open("data.txt", mode="r", encoding="utf-8") as file:
    for line in file: #一行一行讀取
        sum+=int(line) #把字串轉換成整數型態 
print(sum)

#Json:JavaScript Object Notation (JavaScript物件表示法
#使用Json格式讀取、複寫檔案
import json
with open("config.json", mode="r") as file:
    data=json.load(file)
print(data) #data是一個字典資料
print("name: ", data["name"])
print("version: ", data["Version"])

#(續)從檔案中讀取json，讀取後放入變數，再改變變數資料
import json
with open("config.json", mode="r") as file: #讀取
    data=json.load(file)
print(data) 
data["name"]="New Name" #改變變數中資料
print(data)
#最後把最新資料複寫回檔案中 dump(用於json)
with open("config.json", mode="w") as file:
    json.dump(data, file)
    