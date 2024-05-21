#寫入csv格式檔案
# import csv
# with open("data.csv", mode="w", newline="") as file:
#     writer=csv.writer(file)
#     writer.writerow([1,2,3])
#     writer.writerow([4,5,6])
#     writer.writerow([7,8,9])

#讀取csv格式檔案
import csv
with open("data.csv", mode="r", newline="") as file:
    reader=csv.reader(file)
    #逐"列"讀取資料 讀出的結果會以list方式呈現，且讀出的資料內容為"字串"型式
    # for row in reader: 
    #     print(row)
    
    #把資料加總之簡單程式範例
    total=0
    for row in reader:
        for data in row:
            total=total+int(data) #data本身讀出是"字串"格式，要做處理
    print(total)