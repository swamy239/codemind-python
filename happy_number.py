n=int(input())
l=[]
while(True):
    k=0
    for i in str(n):
        k+=int(i)**2
    if k==1 or k==7:
        print("True")
        break
    if k in l:
        print("False")
        break
    else:
        l.append(k)
    n=k