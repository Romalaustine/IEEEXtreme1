n,a,b=map(int,input().split(" "))
if 2*a>n:
    print("NO")
else:
    print("YES")
    for i in range(b,a-1,-1):
        r=n%i
        if a<=r<=b:
            f=[i]*(n//i)
##              for j in range(n//i):
##                  f.append(i)
            if r!=0:
                f.append(r)
                break
        elif(n%i)==0:
            f=[i]*(n//i)
            break
    for m in sorted(f):
        print(m," " ,end="")
    
