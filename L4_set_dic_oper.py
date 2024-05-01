# Set:集合，用大括號表示
s1={3, 4, 5}
print(3 in s1) #判斷3是否在s1集合內
print(4 not in s1) #判斷4是否不在s1內)

#交集&(取兩個集合中相同的資料) 
#聯集|(兩個資料中全部的資料但不重複)
#差集-(集合資料作減法)
#反交集^(取兩個集合中不重疊的部分)
s1={1,2,3,4}
s2={3,4,5,6}
s3=s1&s2 #交集
print(s3)
s3=s1|s2 #聯集
print(s3)
s3=s1-s2 #差集(從s1中減去和s2重疊的部分)
print(s3)
s3=s2-s1
print(s3) #(從s2中減去和s1重疊的部分)
s3=s1^s2
print(s3)

#set字串 把字串拆解成集合，輸出時會去掉重複值且無順序輸出
s=set("hello") 
print(s) 
print("h" in s) #測試字母是否有在字串內

# 字典 Dictionary、key-value配對
dic={"apple":"蘋果", "data":"資料","your":"你的"}
dic["apple"]="小蘋果"
print(dic["apple"])
print("蘋果"in dic) #判斷是否在dictionary中的是以key來判斷
print("test" not in dic)
print(dic)
del dic["apple"] #刪除字典中的key-value pair
print(dic)

#用列表的資料當基礎來產生字典
dic={x:x*2 for x in [3,4,5]} #for...in用法是固定的
print(dic)