import pandas as pd
#Series篩選練習1-1 
data=pd.Series([30, 15, 20]) 
condition=[True, False, True] 
filterData=data[condition]
print(filterData)

#Series篩選練習1-2
condition=data>18 #透過比較運算來得到布林值
print(condition)
filterData=data[condition]
print(filterData)

#Series篩選練習2-1
data=pd.Series(["您好", "Python", "Pandas"])
condition=[False, True, True]
filterData=data[condition]
print(filterData)

#Series篩選練習2-2
condition=data .str.contains("P")
print(condition)
filterData=data[condition]
print(filterData)

#DataFrame篩選練習1-1
data=pd.DataFrame({
    "name":["Vancy","Kaycen", "John"],
    "salary":[40000, 100000, 35000]
})
print(data)
condition=[False, True, True]
filterData=data[condition]
print(filterData)

#DataFrame篩選練習1-2
condition=data["salary"]>=40000 
print(condition)
filterData=data[condition]
print(filterData)

#DataFrame篩選練習2 - 
condition=data["name"]=="Vancy"
print(condition)
filterData=data[condition]
print(filterData)