#複習前一章節decorator
#decorator factory:用來「生產」裝飾器的「函式」
# def 裝飾器工廠名稱(參數名稱, ...):
#     def 裝飾器名稱(回呼函式名稱):
#         def 內部函式名稱:
#             #裝飾器內部程式碼
#             回呼函式名稱()
#         return 內部函式名稱
#     return 裝飾器名稱

# @裝飾器工廠名稱(參數資料,...)
# def 函式名稱():  
#     #函式內部的程式碼

# 函式名稱() #呼叫帶有裝飾器的函式

#程式1
# def testFactory(base):
#     def testDecorator(callback):
#         def innerFunc():
#             result=base*3
#             callback(result)
#         return innerFunc
#     return testDecorator

# @testFactory(3)
# def decoratedFunc(result):
#     print("普通函式", result)

# decoratedFunc()


#程式2
# def myFactory():
#     def myDeco(callback):
#         def run():
#             print("裝飾器中的程式碼")
#             callback(6) 
#         return run
#     return myDeco
# #使用裝飾器
# @myFactory() #裝飾器工廠要+小括號
# def test(n):
#     print("普通函式的程式碼", n)

# test()


#程式3
# def myFactory(base):
#     def myDeco(callback):
#         def run():
#             print("裝飾器中的程式碼", base)
#             result=base*8
#             callback(result) 
#         return run
#     return myDeco 
# #使用裝飾器
# @myFactory(6) #裝飾器工廠要+小括號
# def test(result):
#     print("普通函式的程式碼", result)

# test()


#程式4 1+2+3+...+max 的裝飾器
def calculateFactory(max):
    def calculate(callback):
        def run():
            total=0
            for n in range(max+1):
                total+=n
            callback(total)
        return run  
    return calculate
    
@calculateFactory(100)
def show(result):
    print("結果是", result)
@calculateFactory(10)
def showEng(result):
    print("Result is", result)

show()
showEng()

    
