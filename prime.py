num = 10
while num<=20:
    i=2
    flag=0
    while i<num-1:
        if num%i==0:
            flag = 1
            break
        i=i+1
    if flag ==0:
        print("prime no=",num)
    else:
        print("prime not= ",num)
        
    
    num=num+1
