n=int(input())
k1=n+1
k2=n-1
while(True):
    if str(k1)==str(k1)[::-1]:
        break
    k1+=1
while(True):
    if str(k2)==str(k2)[::-1]:
        
       break
    k2-=1
if abs(n-k1)==abs(n-k2):
    print(k2,k1)
elif abs(n-k1)<abs(n-k2):
    print(k1)
else:
    print(k2)