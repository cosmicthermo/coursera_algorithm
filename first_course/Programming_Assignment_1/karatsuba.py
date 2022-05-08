import math as math
def karat(num_1, num_2):
	lenth = len(str(num_1))
	a, b = divide(num_1)
	c, d = divide(num_2)
	#Step 1: compute a*c 
	ac = a * c
	#Step 2: compute b*d
	bd = b * d
	#Step 3: compute the distributed rule
	abcd = (a + b) * (c + d)
	#4: Compute the last minus
	step_4 = abcd - ac - bd
	
	result = (10**lenth)*ac + step_4*10**(lenth/2) + bd
	return result

def divide(number):
	length = int(len(str(number))/2)
	print(length)
	num_arr = str(number)	
	A = num_arr[:length]
	B = num_arr[length:]
	return int(A), int(B)
# Reference answer

def karatsuda(num1, num2):
	num1Str = str(num1)
	num2Str = str(num2)
	if (num1 < 10) or (num2 < 10):
		return num1 * num2

	maxLenth = int(max(len(num1Str), len(num2Str)))
	print(maxLenth)
	split = math.ceil(maxLenth / 2)
	print(split)
	high1, low1 = int(num1Str[:-split]), int(num1Str[-split:])
	high2, low2 = int(num2Str[:-split]), int(num2Str[-split:])
	z0 = karatsuda(low1, low2)
	z1 = karatsuda((low1 + high1), (low2 + high2))
	z2 = karatsuda(high1, high2)
	return (z2*10**(2*split)) +(z1-z0-z2)*10**(split) + z0
	
def karatsuba_1(num1, num2):
    num1Str = str(num1)
    num2Str = str(num2)
    if (num1 < 10) or (num2 < 10):
        return num1*num2

    maxLength = max(len(num1Str), len(num2Str))
    splitPosition = maxLength / 2
    high1, low1= int(num1Str[:-splitPosition]), int(num1Str[-splitPosition:])
    high2, low2= int(num2Str[:-splitPosition]), int(num2Str[-splitPosition:])
    z0 = karatsuba_1(low1, low2)
    z1 = karatsuba_1((low1 + high1), (low2 + high2))
    z2 = karatsuba_1(high1, high2)

    return (z2*10**(2*splitPosition)) + ((z1-z2-z0)*10**(splitPosition))+z0
	
	
