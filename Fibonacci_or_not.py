n=int(input())
if n==0 or n==1:
    print("True")
else:
    x=0
    y=1
    while(x+y<=n):
        if x+y==n:
            print("True")
            break
        z=x+y
        x=y
        y=z
    else:
        print("False")