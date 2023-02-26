n=int(input("Enter the number of prime number sum you want "))
t=0
sum=0
d=2
while t<n:
    s=0
    for j in range(2,d):
        if d%j==0:
            s=s+1
    
    if s==0:
       sum=sum+d
       t=t+1
    d=d+1
print(sum)
