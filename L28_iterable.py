#Iterable 疊代資料:能回傳其包含的所有元素，但它不必是資料結構。
#字串、列表、集合、字典 皆是可疊代的資料

#for迴圈
#for 變數名稱 in 可疊代的資料:
# dic={"a":3, "test":5}
# for key in dic:
#     print(key)
#     print(dic[key]) #印出value

#內建函式    
#max(可疊代資料)
# result=max([10, 5, 88, 35])
# print(result)
# result=max("xaz") #得z
# print(result)
# result=max({10, 200, 1, 30}) #得200
# print(result)
# result=max({"x":8, "y":222}) #得y
# print(result)

#sorted(可疊代資料) #會用list方式回傳
result=sorted("cba")
print(result)
result=sorted([90, 180, 22]) 
print(result)
result=sorted({90, 180, 22}) 
print(result)