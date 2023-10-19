n=int(input("donner le premier nombre : "))
m=int(input("donner le deuxieme nombre : "))
sn=0
for i in range(2,n):
    if n%i==0 :
        sn=sn+i

sm=0
for i in range(2,m):
    if m%i==0 :
        sm=sm+i

if n==sm and m==sn :
    print("sont amis")
else :
    print("non amis")
