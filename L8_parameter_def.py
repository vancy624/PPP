#參數預設值、名稱對應任意長度參數
#參數的預設資料
def power(base,exp=0):
    print(base**exp)
power(3,2) #呼叫若有給值，就會把原本的exp=0壓過去
power(4) #exp若有給值，此呼叫才可成立(使用預設值0)

#使用參數名稱對應
def divide(n1, n2):
    print(n1/n2)
divide(2,4) #0.5
divide(n2=2,n1=4) #2.0

#無限/不定 參數資料 會用Tuple(不可更動之有序列表)的方式運作
def data(*ns):
    print(ns)
data(3,4)
data(3,5,10)
data(1,4,-1,-8)

def avg(*ns):
    sum=0
    for n in ns:  #有序列表一個一個拿出來用
        sum=sum+n
    print(sum/len(ns))
avg(1,4,-1,-8)
avg(333,666)

