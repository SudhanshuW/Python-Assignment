#program to check armstrong number

num=int(input("enter the no="))
sum=0
temp=num
while temp>0:
    d=temp%10
    sum+=d**3
    temp//=10
if num==sum:
    print("the no is armstrong")
else:
    print("the no is not armstrong")