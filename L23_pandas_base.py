#嵌入pandas模組
import pandas as pd
#建立Series 單維度資料
# data=pd.Series([20,10,15])
#print(data)
#基本series 操作
# print("Max", data.max())
# print("Median", data.median())
# data=data*2
# print(data)
# data=data==20 #比較運算:看這個資料內有沒有和20相等的
# print(data) 

#建立DataFrame 雙維度資料 要用字典格式
data=pd.DataFrame({"name":["Vancy","Kaycen","Amy"],
                   "salary":["40000","100000000","30000"]
})
print(data)
#基本DataFrame 操作
#print(data["salary"]) #取得特定欄位
print("----------------------")
print(data.iloc[2]) #取得特定列data.iloc[第幾列]