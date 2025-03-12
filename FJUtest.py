#反轉字串
# 使用 Python 的簡單方法來反轉句子並插入逗號
str_input = input("請輸入: ")

# 反轉句子並用逗號將每個字符連接，保留空格
result = ",".join(str_input[::-1])

# 輸出結果
print("結果:", result)





#-----------------------------------------------


#補數(2補)
def binary_to_twos_complement(binary_str):
    # 取得原始輸入的長度
    original_length = len(binary_str)

    #轉成1補數
    ones_complement = ''.join('1' if bit == '0' else '0' for bit in binary_str)

    # 一補數加1，限制為原始位數範圍
    twos_complement_decimal = int(ones_complement, 2) + 1 

    # 回到二進制格式並去除'0b'前綴，使用zfill補足原長度
    twos_complement_binary = bin(twos_complement_decimal)[2:].zfill(original_length)
    
    print(twos_complement_binary)

n = int(input("請輸入幾組測資:"))
for i in range(n):
    binary_str = input("請輸入2進制數值:")
    binary_to_twos_complement(binary_str)

#-----------------------------------------------

#補數(1補)
def binary_to_ones_complement(binary_str):
    original_length = len(binary_str)
    
    ones_complement = ''.join('1' if bit == '0' else '0' for bit in binary_str) 

    return ones_complement

n = int(input("請輸入測資組數:"))
for i in range(n):
    binary_str = input("請輸入2進制數值:")
    result = binary_to_ones_complement(binary_str)
    print(result)

#-----------------------------------------------

#ISBN-10
def ISBN(x):
    total = 0
    for i in range(9):
        # 將每個字元轉為整數，並乘上其加權值
        result = int(x[i])*(i+1) #從[0]開始，所以後面的i要+1
        total += result
    # 計算檢查碼
    check = total %11
    # 若檢查碼為 10，返回 'X'，否則返回檢查碼本身
    return 'X' if check == 10 else str(check)

while True:
    k = int(input("請輸入幾組測資(1-100): "))
    if 1 <= k <= 100:
        break  # 如果 k 在有效範圍，則結束迴圈
    else:
        print("組數範圍錯誤，請重新輸入。")

# 逐組輸入資料並計算 ISBN
for i in range(k):
    x = input("請輸入9碼ISBN: ")
    d10 = ISBN(x)
    print(x + d10)

#-----------------------------------------------


#反轉字串
while True:
    k = int(input("請輸入幾組測資:"))
    if 1<=k<=100:
        break
    else:
        print("範圍輸入錯誤，請重新輸入。")      


for i in range(k):
    n, str_input = input("請輸入要分成幾群以及被分配的字串，中間以空格隔開: ").split()
    n= int(n)

    group_len=len(str_input) // n

    result=""
    
    for j in range(n):
        # 計算每組的起始索引
        start_index = j * group_len 
        # 計算每組的結束索引
        end_index = start_index + group_len #起始位置+每組長度就是最終位置
        # 反轉每組內字元
        result += str_input[start_index:end_index][::-1]

    print("結果:", result)


#豹子
k = int(input("how much\n"))
for i in range(k):
    nums = input('enter 3 nums\n')
    num1, num2, num3 = nums.split()
    
    if num1 == num2 == num3:
        print("yes")
    else:
        print('no')


#-----------------------------------

#間隔數
N = int(input("how much"))
if N <0 or N>20:
    print("enter error")
else:
    for i in range(N):
        num = int(input("plz enter"))
        if num<=1000 or num>=9999:
            print("enter error")
        else:
            a = num//1000
            b = (num//100)%10
            c = (num//10)%10
            d = num%10
            if a == c :
                if b==d :
                    if a != b:
                        if c != d:
                            print("yes")
                            print(a, b, c, d)
                        else:
                            print("no1")
                            print(a, b, c, d)
                    else:
                        print("no2")
                        print(a, b, c, d)
                else:
                    print("no3")
                    print(a, b, c, d)
            else:
                print("no4")
                print(a, b, c, d)


#---------------------------
複利
k = int(input("plz enter"))
if k<1 or k>100:
    print("enter error")
else:
    for i in range(k):
        nums = input("plz enter")
        p, r, t = nums.split()
        p = int(p)
        r = float(r)
        t = int(t)
        f = p*(1+(r/100)/12)**(12*t)
        print(round(f))


#---------------------------
#539
num=[]
nums = input("plz enter 5 nums")
num = nums.split()
k = int(input("how much"))
price=0
guess= []
if k<1 or k>100:
    print("enter error")
else:
    for i in range(k):
        mynum = input("plz enter 5 nums")
        guess = mynum.split()
        # print(guess)
        for j in range(len(guess)):
           if guess[j]  in num:
                price+=1
                # print(guess[j])
        print(price)
        price=0
        guess.clear()

#---------------------------
#愛找麻煩的老師
k = int(input("how much"))
num=[]
for i in range(k):
    num = input("plz enter 10 nums").split()
    num = list(map(int, num))
    
    for i in range(10):
        for j in range(i+1,10):
            if num[i]<=num[j]:
                tf=True
            else:
                tf=False
                break
    if tf==True:
        print("yes")
    else:
        print("no")

#---------------------------
#樂透
N = int(input("how much"))

if N <=1 or N>100:
    print("enter error")
else:
    for i in range(N):
        num = (input("plz enter 7 nums")).split()
        num = list(map(int, num))
        
        if len(num) !=7:
            print("No")
        else:
            for j in range(7):
                if num[j]>49 or num[j]<1:
                    print("No")
                    break
                elif len(set(num))!=7:
                    print("No")
                    break
                else:
                    print("Yes")
                    break
#---------------------------

#找零機器
while True:
    money = int(input("how much money:"))
    if money ==0:
        break
    else:
        a = money//50
        b = (money-50*a)//10
        c = (money-50*a-10*b)//5
        d = money%10
        print(a, b ,c ,d)

#---------------------------
#ISBN-10
k = int(input("how much:"))
for i in range(k):
    sum=0
    num=input('enter number')
    num_list = list(num)
    for i in range(len(num_list)):
        sum+= int(num_list[i])*(i+1)
    if (sum%11)==10:
        sum='X'
        num_list.append(sum)
    else:
        sum=sum%11

        num_list.append(str(sum))

    ans=''.join(num_list)
    print(ans)


#---------------------------
#兩數相加
k = int(input("how much"))
for i in range(k):
    num_count = int(input("enter arr len"))
    target = int(input("enter target"))
    num_list = input("arr nums").split()
    num_list = list(map(int, num_list))
    for j in range(num_count):
        for a in range(j+1, num_count):
            if num_list[j]+num_list[a] == target:
                print(j, a)
                break

#---------------------------
#完全平方數
n = int(input("how much:"))
for i in range(n):
    num = input("plz enter a b").split()
    a=int(num[0])
    b=int(num[1])
    sum=0
    if a>b:
        a,b=b,a
    for i in range(1,b+1):
        if a<i**2<b+1:
            sum+=i**2
    print(sum)

#---------------------------
#時分秒
k = int(input("how much:"))
for i in range(k):
    sec=int(input("enter sec"))
    min=sec//60
    sec=sec%60
    hour=min//60
    min=min%60
    print("%02d:%02d:%02d"%(hour,min,sec))