#Generator:"動態"產生可疊代的資料，搭配for迴圈使用
#定義"建立生成器"的函式
def test():
    yield 5
#呼叫並回傳生成器
gen=test() 
# print(gen) #呼叫test函式，yield 5 尚未被運作，僅產生一個生成器，print出來的是記憶體位址
#如何取得生成器裡的資料 #搭配for迴圈使用
for d in gen:
    print(d) #5

#示範一
def test():
    print("階段一")
    yield 5
    print("階段二")
    yield 66
gen=test() 
for d in gen:
    print(d) 

#示範二
def generateEven():
    number=0
    yield number
    number+=2
    yield number
    number+=2
    yield number
evenGenerator=generateEven()
for data in evenGenerator:
    print(data)

#示範三:給定最大值
def generateEven(maxNumber): 
    number=0
    while number<maxNumber:
        yield number
        number+=2
evenGenerator=generateEven(17)
for data in evenGenerator:
    print(data)