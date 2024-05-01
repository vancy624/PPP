#module:獨立的程式檔案(將程式寫在一個檔案中，此檔案可重複載入使用)
#module需先載入，才可使用模組中的函式或變數
import sys #python內建的，可取得系統相關資訊
print(sys.platform)
print(sys.maxsize)

#module 別名的使用 +as
import sys as s
print(s.platform)
print(s.maxsize)

#建立geometry 模組，載入使用 (建立一個python檔案，名稱為geometry)
import modules.geometry as geometry #檔案路徑(若模組在同一個資料夾就只要寫檔案名稱就好，若不再同個資料夾就要把位置寫清楚) 
result=geometry.distance(1,1,5,5) #格式:模組名稱或別名.函式名稱(參數資料)
print(result)
result=geometry.slope(1,2,5,6)
print(result)

#搜尋python"內建"模組sys的路徑
import sys 
print(sys.path) #印出模組的搜尋路徑 
#表示我們要載入一個模組時，python會依照這些路徑把模組抓進來
#非內建模組而是自己創建的話，python依照原本搜尋路徑會找不到
#故要在模組搜尋路徑列表中手動新增路徑 sys.path.append("modules") 


import sys
sys.path.append("modules") #在模組的搜尋路徑列表中【新增路徑】
print(sys.path) #印出模組的搜尋路徑 (相對路徑)
import modules.geometry as geometry
print(geometry.distance(1,1,5,5))
