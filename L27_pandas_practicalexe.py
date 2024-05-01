import pandas as pd
#讀取資料
data=pd.read_csv("googleplaystore.csv") #把csv格式的檔案讀取成一個DataFrame
#觀察資料
#print(data)
print("資料數量", data.shape) 
print("資料欄位", data.columns)
print("----------------------")
#分析資料:評分的各種統計數據
print(data["Rating"])
print("平均數", data["Rating"].mean())
print("中位數", data["Rating"].median())
print("取得評分前100名的應用程式平均", data["Rating"].nlargest(100).mean()) 
#上行的平均>5分(不合理) 以下做分析
condition=data["Rating"]>5
data=data[condition]
print(data) #發現真的有>5的資料
#改寫程式
condition=data["Rating"]<=5
data=data[condition]
print("取得評分前100名的應用程式平均", data["Rating"].nlargest(100).mean()) #100筆資料母數不夠大，改成1000筆平均會較合理
print("取得評分前1000名的應用程式平均", data["Rating"].nlargest(1000).mean())
# 也可以寫成下面這行
print("取得評分前100名的應用程式平均", data[condition]["Rating"].nlargest(100).mean())

#分析資料:"安裝數量"的各種統計數據
print(data["Installs"]) #觀察後發現資料為"字串"格式而非"數字"
data["Installs"]=pd.to_numeric(data["Installs"].str.replace("[,+]","")) #字串轉換成數字 #把資料內的,+替換成空
#上面那行無法跑，改用下面的函式
def clean_installs(installs):
    # 去掉逗號和加號
    installs = installs.replace(",", "").replace("+", "").replace("Free", "0")
    # 轉換為整數
    return int(installs)
# 將函式應用到Installs列
data["Installs"] = data["Installs"].apply(clean_installs)

print("平均數", data["Installs"].mean())

#篩選資料來應用
condition=data["Installs"]>100000
print("安裝數量大於100,000的應用程式有幾個:", data[condition].shape) #.shape 資料數量, 格式[資料數, 欄] 
print("安裝數量大於100,000的應用程式有幾個:", data[condition].shape[0]) # 僅保留資料數

#基於資料的應用: 關鍵字搜尋應用程式名稱
keyword=input("請輸入關鍵字：")
condition=data["App"].str.contains(keyword, case=False) #應用程式名稱(字串)是否有包含使用者輸入的關鍵字,並忽略大小寫之別(case) 
print(data[condition]["App"])
print("包含關鍵字的應用程式數量", data[condition].shape[0])