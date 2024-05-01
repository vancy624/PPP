#載入 pandas 模組
import pandas as pd
#資料索引
data=pd.Series([5, 4, -2, 3, 7], index=["a", "b", "c", "d", "e"])

#觀察資料
print("資料型態", data.dtype)
print("資料數量", data.size)
print("資料索引", data.index)

#取得資料: 根據順序、根據索引
print(data[2]) #根據順序取得資料:第三筆資料
print(data["d"], data["a"]) #根據索引取得資料:第四筆資料、第一筆資料

#數字運算: 基本、統計、順序
print("最大值", data.max())
print("加法總和", data.sum())
print("乘法總和", data.prod())
print("算術平均數", data.mean())
print("標準差", data.std())
print("中位數", data.median())
print("最大的三個數", data.nlargest(3))
print("最小的兩個數", data.nsmallest(2))

#字串運算: 基本、串接、搜尋、取代
data=pd.Series(["您好","Python","Pandas"])
print(data.str.lower()) #將英文全部變小寫(大寫為upper)
print(data.str.len()) #算出字串長度
print(data.str.cat(sep=",,")) #把三個字串串起來(sep="字串中間要用甚麼串起來")
print(data.str.contains("P")) #判斷字串中是否有包含特定字元
print(data.str.replace("您好","Hello")) #取代
