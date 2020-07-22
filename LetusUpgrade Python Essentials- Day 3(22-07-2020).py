# Take an integer and find prime or not

num=int(input("Enter a number: "))
if(num > 1):
	for i in range(2,num):
		if(num%i)==0:
			print(num,"is not a prime number")
			break
	else:
		print(num,"is a prime number")
		
		
#Sum of n numbers with help of while loop

number=int(input("Enter the Number : "))

total=0
value=1

while (value<=number):
	total = total + value
	value = value +1
	
print("The Sum of N Numbers from 1 to {0} =  {1}".format(number, total))