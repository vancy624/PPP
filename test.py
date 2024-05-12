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