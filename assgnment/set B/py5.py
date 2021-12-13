#python program to find factorial of a number

num=int(input("enter the no="))
fact=1
if num<0:
    print("please enter a positive no")
elif num==0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fact*=i
    print(f"the factorial of {num} is {fact}")