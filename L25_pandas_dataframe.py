import pandas as pd
#資料索引: pd.DataFrame{字典, index=索引列表}
data=pd.DataFrame({
    "name":["Vancy","Kaycen", "John"],
    "salary":[40000, 100000, 35000]
}, index=["i", "ii", "iii"])
print(data)
print("----------------------")
print("資料數量", data.size)
print("資料形狀(列,欄)",data.shape)
print("資料索引", data.index)

#取得列(row/橫向)的Series資料:根據順序、根據索引
print("取得第二列", data.iloc[1])
print("取得第二列", data.iloc[1], sep="\n") #sep=把資料串起來中間的符號
print("----------------")
print("取得第ii列",data.loc["ii"],sep="\n")

#取得欄(column/直向)的Series資料:根據欄位的名稱
print("取得name欄位",data["name"], sep="\n")

#結合上一章節教的 單維度資料處理
#name轉大寫
names=data["name"] #取得單維度Series資料
print("把name全部轉大寫", names.str.upper(), sep="\n")
#計算薪水平均值
salaries=data["salary"]
print("薪水平均值",salaries.mean())

#建立新的欄位(多增加一個Series/單維度資料) 2種寫法
data["revenue"]=[500000, 1500000, 150000] #data["新欄位名稱"]=[列表資料]
print(data)
print("                      ")
#較正式寫法 要給跟上面一樣的index
data["rank"]=pd.Series([5, 1, 9], index=("i", "ii", "iii")) #data["新欄位名稱"]=pd.Series(資料), index=["索引"]
print(data)
print("                      ")
#根據現有欄位來增加新的欄位
data["cp"]=data["revenue"]/data["salary"]
print(data)
print("                      ")