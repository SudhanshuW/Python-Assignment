#python program to check a prime number

num=int(input("enter the no= "))
if num>1:
	for i in range(2,num):
		if num%i==0:
			print("the no is not prime")
			break
	else:
		print("the no is prime")
else:
	print("number is not prime")