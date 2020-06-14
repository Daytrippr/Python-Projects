#1 calculates the year you turn 100
"""def aging(age, current_year):
	year100 = int(current_year) - int(age) + 100
	print(year100)

aging(24, 2020)
"""




#2 Determines if a number is odd, even, or divisible by 4

"""def odd_or_even(num):
	if num % 2 == 0:
		print("The number you gave is even!")
	elif num % 2 == 1:
		print("The number you gave is odd!")
	if num % 4 == 0 and num != 0:
		print("The number us also divisible by 4!")


odd_or_even(4)"""

#2.1 determines odd or even with an input!!!
"""start = True
while start == True:
	num = int(input("Pick a number!:"))

	if num % 2 == 0:
		print("The number you gave is even!")
	elif num % 2 == 1:
		print("The number you gave is odd!")
	if num % 4 == 0 and num != 0:
		print("The number us also divisible by 4!")"""


#3 # user gives a number, the program returns a list of a seperate list
#containing all numbers below that number
"""a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []
repeat = True
while repeat == True:
	num1 = int(input("Pick a number between 1 and 100:"))
	for i in a:
		if num1 > i:
			new_list.append(i)
	print(new_list)
	new_list = []"""

#4 the user gives a number, and the program retuns all
#   divisors of that number
"""repeat = True
while repeat == True:
	num = int(input("Pick a number:"))
	divisors = []

	for nums in range(1, num + 1):
		if num % nums == 0:
			divisors.append(nums)
	print(divisors)"""

#5 compare two lists and print all common numbers in the list
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for item in a:
	for items in b:
		if item == items:
			c.append(item)
print(c)
