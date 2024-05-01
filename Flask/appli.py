#網站程式:24小時運作(不能中斷)，程式若中斷，網站就不能使用
from flask import Flask
app=Flask(__name__) #__name__為python內建的變數，用來儲存某程式在哪個模組下執行

#函式的裝飾(Decorator): 以函式為基礎，提供附加的功能
@app.route("/")  #當網站連到根目錄 http://127.0.01:5000 
def home(): #交給此函式處理
    return "Hello Flask22"
#要處理的網站路徑
@app.route("/test") #代表我們要處理的網站路徑 http://127.0.0.1:5000/test
def test():
    return "This is Test" 

if __name__=="__main__": #如果以主程式執行
    app.run() #立刻啟動伺服器