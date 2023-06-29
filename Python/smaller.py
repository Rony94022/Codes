small=0
smaller=0
for i in range(10):
    a=int(input("enter your no:"))
    if i == 0:
        small=b
        
    elif i == 1:
        if b<=small:
            smaller=b
            
        else:
            smaller=small
            small=b
    else:
        if b <smaller:
            small=smaller
            smaller=b
        elif b<small:
            smaller=b					
            
print("smlaller no :",smaller)
print("second smallest no:",small)
          
