#實體物件的建立與使用(上)-實體屬性
#實體屬性：封裝在實體物件中的變數
#定義類別 -> 透過類別建立實體物件 -> 建立實體物件後才可使用實體屬性
class point: #class 類別名稱
   def __init__(self): #定義初始化函式 (def後面要空一格)
       self.x=3 #透過操作self來定義"實體屬性"
       self.y=4
p=point() #格式: 變數=類別名稱()   
#上行解釋:建立實體物件(point())，放入變數p中，故使用p即可取得實體屬性的資料。

class point:
    def __init__(self):
        self.x=3
        self.y=4
p1=point() #建立第一個實體物件放入p1
print(p1.x, p1.y)
p2=point() #建立第二個實體物件放入p2
print(p2.x, p2.y)


class point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
p=point(1,5) #建立時可直接傳入參數資料 1放入x 5放入y
print(p.x+p.y) #如何取得資料:實體物件.實體屬性名稱

class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
p1=point(3,4)
print(p1.x, p1.y)
p2=point(1,9)
print(p2.x, p2.y)

# FullName 實體物件的設計: 分開紀錄姓、名資料的全名
class FullName: #給定初值，透過name1來使用實體物件
    def __init__(self):
        self.first="W.H"
        self.last="Wu"
name1=FullName()
print(name1.first, name1.last)

class FullName: #用引數方式傳值
    def __init__(self, first, last):
        self.first=first
        self.last=last
name1=FullName("W.H", "Wu")
print(name1.first, name1.last)
name2=FullName("T.H", "Lee")
print(name2.first, name2.last)