sum=0
x=int(input('enter the TOTAL NO.s you need to find the mean of:'))
r=x
while x>0:
    a=int(input('enter the no. :'))
    sum=sum + a
    mean=sum/r
    x=x-1  
print("MEAN=",mean)
