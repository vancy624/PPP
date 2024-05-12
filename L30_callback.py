#回呼函式 callback:透過參數傳遞函式到另一個函式中
def test(arg):
    print(arg) #印出記憶體位址
def handle():
    print(100)
test(handle)

def test(arg):
    arg() #呼叫回呼函式"handle"
def handle():
    print(100)
test(handle) #把handle函式傳遞到test內

def test(arg):
    arg("^_^") 
    arg("ccc")
def handle(data):
    print(data)
test(handle) 

def add(n1, n2, cb):
    cb(n1+n2)
def handle1(result):
    print("結果是", result)
def handle2(result):
    print("Result of Add is", result)
add(3,9, handle1)
add(7,11,handle2)