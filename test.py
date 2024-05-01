import pandas as pd
#資料索引: pd.DataFrame{字典, index=索引列表}
data=pd.read_csv("googleplaystore.csv") #把csv格式的檔案讀取成一個DataFrame
#分析資料:評分的各種統計數據
# print(data["Rating"])
# print("平均數", data["Rating"].mean())
# print("中位數", data["Rating"].median())
# print("取得評分前100名的應用程式平均", data["Rating"].nlargest(100).mean()) 
#上行的平均>5分(不合理) 以下做分析
condition=data["Rating"]<=5
data=data[condition]
print("取得評分前100名的應用程式平均", data["Rating"].nlargest(1000).mean())
