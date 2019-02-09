#增加檢查檔案功能
import os#operating system
products = []
if os.path.isfile('products.csv'):
	print('找到檔案 ')
	with open('products.csv','r',encoding='utf-8')as f:
		for line in f:
			if '商品,價格' in line:
				continue 
			name,price = line .strip().split(',')  #字串可以用.split來切割
			products.append([name,price])         #.strip來去掉換行符號(\n)
	print(products)
else:
	print('找不到檔案') 
# 讀取檔案

#讓使用者輸入
while True:
	name = input('請輸入商品名稱')
	if name == 'q':
		break
	price = input('請輸 入價格')
	price = int(price)
	products.append([name,price])

print(products)
#印出所有購買紀錄
for p in products:
	print(p[0],'的價格是',p[1]) #小清單裡面第0格是..
#寫入檔案
with open('products.csv','w',encoding='utf-8 ')as f: #r為讀取,w為寫入模式，就算沒有txt檔,仍然可以寫入,也可寫成.csv的excel檔,utf-8為最廣泛使用的編碼
	f.write('商品,價格\n')
	for p in products: 
		f.write(str(p[0])+','+str(p[1])+'\n')#字串可以做合併