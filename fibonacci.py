def fib(num):
    if(num==0)or(num==1):
        return num;
    fib1=fib(num-1)
    fib2=fib(num-2)
    return fib1+fib2
num=int(input("enter a number:"))
for num in range(0,num):
    print(fib(num))        