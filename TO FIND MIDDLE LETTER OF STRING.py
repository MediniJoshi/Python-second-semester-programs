a=input("")
b=len(a)

if b%2==0:
    print("No middle letter")
else:
    c=(b-1)/2
    c=int(c)
    print("Middle character is")
    print(a[c:c+1])
    
