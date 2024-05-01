#實體物件的建立與使用(下)-實體方法
#實體方法：封裝在實體物件中的函式
class Point:
    def __init__(self, x, y): #定義初始化函式   #定義成員(物件)
        self.x=x
        self.y=y
    def show(self): #定義實體方法/函式,格式:方法名稱(self, 更多自訂參數): #定義成員要幹嘛
        print(self.x, self.y) #方法主體, 透過self操作實體物件
p=Point(1, 5) #建立實體物件，放入變數p中
p.show() #呼叫實體方法

#Point 實體物件的設計: 平面座標上的點
class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    #定義實體方法
    def show(self):
        print(self.x, self.y)
    def distance(self, targetx, targety): #呼叫distance要給參數targetx.y
        return (((self.x-targetx)**2+((self.y-targety)**2))**0.5)
p=Point(2, 7) #建立實體物件，呼叫初始化函式
p.show() #呼叫實體方法/函式
result=p.distance(0,0) #計算座標(2,7)和座標(0,0)之間的距離
print(result)

#File 實體物件的設計:包裝檔案讀取的程式
class File:
    #定義初始化函式
    def __init__(self, name):
        self.name=name
        self.file=None #檔案物件 #尚未開啟檔案:初期是None
    #實體方法
    def open(self): #用python內建的檔案開啟功能，得到一個檔案物件
        self.file=open(self.name, mode="r", encoding="utf-8") #並放進實體屬性file內
                      #用參數(下面呼叫有給檔案名稱)的方式給檔案名稱
    def read(self):
        return self.file.read()
#讀取第一個檔案
f1=File("data2.txt") #建立實體物件，放入變數f1
f1.open() #利用變數f1代表實體物件，呼叫實體方法
data=f1.read() #讀資料並放入變數data中
print(data)
#讀取第二個檔案
f2=File("data3.txt")
f2.open()
data=f2.read()
print(data)
