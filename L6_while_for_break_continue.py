#while 迴圈
n=1
sum=0 #用來記錄累加的結果
while n<=10:
    sum=sum+n
    n+=1
print(sum)

#for迴圈
for x in [3, 5, 1]: #一個一個換行印出
    print(x)
for x in "HELLO":
    print(x)
for x in range(8): #0~7
    print(x)
for x in range(5, 11): #5~10
    print(x)

#1+2+3+...+10
sum=0 #sum寫在迴圈裡就會一直歸零重算，不會累加
for x in range(1,11):
    sum=sum+x
print(sum) #寫在迴圈裡就會把每次相加的結果都印出 1.3.6.10...

#break的使用(一定要寫在迴圈的裡面) 會跳出迴圈
n=0
while n<5:
    if n==3:
        break #當n==3時跳出迴圈
    print(n) #印出迴圈中的n
    n+=1
print("最後的n:",n) 

#continue 不會跳出迴圈
n=0
for x in [0,1,2,3]:
    if x%2==0: #x是偶數
        continue #0跟2不會被印出來(被跳過)
    print(x) #印出1跟3
    n+=1 #n也只被印了兩次(因為1跟3)
print("最後的n:",n)

#else 迴圈結束前，執行此命令
sum=0
for n in range(11):
    sum+=n
else: 
    print(sum) #印出0+1+2+3+...+10的結果

#綜合範例: 找出數字平方根 (輸入9，得到3; 輸入11，得到【沒有整數的平方根】)
n=input("輸入一個正整數:")
n=int(n) #將輸入值轉成數字!!!! #也可合併成n=int(input("輸入一個正整數:"))
for i in range(n): #i的範圍從0~n-1
    if i*i==n:
        print("整數平方根:", i)
        break #用break強制結束迴圈，不會執行else區塊
else:
    print("沒有整數平方根")