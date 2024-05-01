#定義函式
def multiply(n1,n2): #函式僅被定義，後面若沒呼叫，就不會執行
    print(n1*n2)
#呼叫1
multiply(6,8) #印出48
multiply(9,6) #印出54

#呼叫2
def multiply(n1,n2): 
    print(n1*n2)
    #return 後面沒+東西都是none，這裡有+沒+結果一樣
value=multiply(3,4) #呼叫mul會先print 12出來
print(value) #回傳none，這裡是印出none

#呼叫3
def multiply(n1,n2): 
    return(n1*n2)
value=multiply(3,4)+multiply(4,9) #呼叫兩次，在程式外做加法
print(value) 

#函式可用來做程式的包裝: 同樣的邏輯可重複利用
def calculate(n):
    sum=0
    for x in range(n+1):
        sum=sum+x
    print(sum)

calculate(10)
calculate(20)
calculate(100)

