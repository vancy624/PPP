#數字運算 
#整數除法要打兩條斜線//
#小數除法一條斜線
#次方 兩個星號**
#開根號 **0.5
x=9**0.5
print(x)

#字串運算
#單引號、雙引號都可以
#斜線可跳脫 
s="Hell\"o"
print(s)

#字串串接 中間用+或空白都可以
s="hello"+"world"
print(s)
s="happy" "day"
print(s)
#換行 \n或是三個雙引號(前後各三)
s="hello\nworld"
print(s)
s="""happy


day"""
print(s)

#字串匯兌內部的字元編號(索引)，從0開始算起
s="abcdefgh"
print(s[4])
print(s[1:3]) #子字串，包含開頭不包含結尾 
print(s[1:]) #子字串，只給開頭不給結尾(開頭不輸出)
print(s[:4]) #子字串，只給結尾不給開頭(結尾不輸出)