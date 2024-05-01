# List:有順序、可動的列表，用中括號[]
grades=[12, 60, 70, 90, 60]
grades[0]=55 #把55放到列表中第一個位置
print(grades)

grades=[1, 9, 7, 5, 3, 2]
grades[1:4]=[] #連續刪除列表中編號1-4(4不包含)的資料
print(grades)
grades=grades+[8, 4] #增加資料在列表後方
print(grades)
print(len(grades)) #列表長度

#巢狀列表
data=[[2, 4, 6],[1, 3, 5]] #兩層列表，第一層列表中第一個資料也是列表
print(data[0]) #第一層的第一個元素
print(data[0][0]) #2
print(data[0][1]) #4
print(data[1][2]) #5
data[0][0:2]=[7, 9, 8] #把第一層第一個元素中編號0-2(不包含2)資料更動成7,9,8
print(data[0])




# Tuple:有順序、不可動的列表，用小括號()
data=(3, 4, 5)
data[0]=5 #錯誤，Tuple不可以更動