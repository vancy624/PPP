#定義類別、與類別屬性(封裝在類別中的變數和函式)
class IO: #定義一個類別IO，其內有兩個屬性 supportedSrcs 及 read
    supportedSrcs=["console", "file"] #屬性1
    def read(src): #屬性2
        if src not in IO.supportedSrcs:
            print("Not Supported")
        else:
            print("Read form", src)
#使用類別
print(IO.supportedSrcs)
IO.read("file") #格式:類別.屬性("")
IO.read("internet")
