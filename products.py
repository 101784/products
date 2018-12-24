import os

#　讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue # 跳過他們,執行下一個
			name, price = line.strip().split(',')
			products.append([name, price])
	return products	
		
# 輸入資料
def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入商品價格: ')
		price = int(price)
		products.append([name, price])
	return products

# 印出所有商品
def print_products(products):
	for p in products:
		print('商品:', p[0], '商品的價格:', p[1])

# 寫入檔案
def write_file(filename, products):
	with open(filename,'w', encoding = 'utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')


def main():
	filename = 'products.csv'
	if os.path.isfile(filename): # 檢查檔案在不在裡面
		print('找到檔案')
		products = read_file(filename)
	else:
		print('找不到歐!')

	products = user_input(products)
	print_products(products)
	write_file(filename, products)

main()