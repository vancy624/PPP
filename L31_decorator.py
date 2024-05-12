#Decorator:特殊設計的函式，用來輔助其他函式的運作
def testDecorator(callback): #裝飾器
    def innerFunc(): #裝飾器裡的函式
        print("裝飾器")
        callback() 
    return innerFunc

@testDecorator #帶有裝飾器的函式
def decoratedFunc():
    print("普通函式") 

decoratedFunc() #呼叫"帶有裝飾器的函式"

#執行流程如下: 
#呼叫"帶有裝飾器的函式"，不會正常往下執行，而是將decoratedFunc丟到callback中
#先執行裝飾器內部程式碼(執行innerFunc函式)L2-4，print"裝飾器"後，執行L5呼叫callback回呼函式
#就式執行decoratedFunc，print普通函式



#定義裝飾器
def myDeco(callback):
    def run():
        print("裝飾器中的程式碼")
        callback(6) #此回呼函式，其實就是被裝飾的普通函式
    return run
#使用裝飾器
@myDeco
def test(n):
    print("普通函式的程式碼", n)

test()

#定義一個裝飾器，計算1+2+3+...+50的總和
def calculate(cb):
    def run():
        #裝飾器想要執行的程式碼
        result=0
        for n in range(51):
            result+=n
        print(result) #印出1+2+3+...+50
        cb()
    return run

#使用裝飾器
@calculate
def show():
    print("普通函式的程式碼")

show()




#裝飾器內部不要印出結果，只做運算
def calculate(cb):
    def run():
        #裝飾器想要執行的程式碼
        result=0
        for n in range(51):
            result+=n #印出1+2+3+...+50
        #把計算結果透過參數傳到被裝飾的普通函式中
        cb(result)
    return run

@calculate
def show(result):
    print("計算結果是", result)

@calculate
def showEnglish(result):
    print("Result is", result)

show()
showEnglish()