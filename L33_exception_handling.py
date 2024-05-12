#錯誤、例外處理
#syntax error：語法寫錯，程式無法執行
#exception：程式可以執行，但在某些狀況下會出現錯誤

#範例一:看似正常的程式
# data=input("請輸入數字：") #若使用者輸入abc
# number=int(data) #型態轉換失敗，發生例外，程式會強制中斷
# number=number*2
# print(number)

#例外處理：事先預想、處理可能發生的例外，讓程式能順利進行下去
#例外處理語法：
# try:
#     可能會發生例外的程式區塊
# except Exception:
#     若上述try區塊程式發生例外
#     跳進此區塊中的程式，繼續執行

#範例一:改寫程式
# data=input("請輸入數字：")

# try: 
#     number=int(data)
# except Exception:
#     number=0

# number=number*3
# print(number)

#範例一:使用者輸入的資料格式無法被轉換成數字，請他重新輸入直到成功為止
while True:
    data=input("請輸入數字：")
    try:
        number=int(data)
        break
    except Exception:
        print("輸入格式錯誤，請重新輸入")

number=number*3
print(number)