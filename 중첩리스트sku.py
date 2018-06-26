##중첩리스트 축약
# 방법1
sku = [(gender + size + color)
	   for gender in 'FM'
	   for size in 'SMLX' if not(gender == 'F' and size == 'X')
	   for color in 'WGRB']

sku


# 방법2
sku = [gender + size + color
	   for gender in 'FM'
	   for size in 'SMLX' 
	   for color in 'WGRB'
	   if not(gender == 'F' and size == 'X')]

sku
