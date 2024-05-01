#隨機模組
import random
data=random.choice([1,5,6,10,20]) #隨機選取1個數字
print(data)
data=random.sample([2,6,8,22,100,112,200],3) #隨機選取3個數字
print(data)

#隨機調換順序 (就是洗牌)
import random
data=[1,6,8,9,21]
random.shuffle(data) #對data本身做調換
print(data)

#隨機取得亂數
import random
data=random.random() #取得0.0-1.0間的隨機亂數
#data=random.uniform(0.0, 1.0) #與上行意義相同
print(data)

data=random.uniform(60.0, 100.0) #自行設定範圍
print(data)

#取得常態分配亂數
#格式：data=random.normalvariate(平均數,標準差)
import random
data=random.normalvariate(100,10) #得到的資料【多數】在90-110之間
print(data)

data=random.normalvariate(0,5) #得到的資料【多數】在-5-5間
print(data)

#統計模組
import statistics as stat
data=stat.mean([1,4,5,8,12,88,999]) #mean 平均數
print(data)
data=stat.median([1,4,5,8,12,88,999]) #median 中位數(會自行砍掉極端值)
print(data)
data=stat.stdev([1,4,5,8,12,88,999]) #stdev 標準差
print(data)



