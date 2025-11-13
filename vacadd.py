def dotProduct(l1, l2):
    len1 = len(l1)
    len2 = len(l2)
    
    if(len1 > len2):
        Minimum = len2
    else:
        Minimum = len1  
          
    sum = 0
    for i in range (0,Minimum):
        sum+=l1[i]*l2[i]
        
    return sum

n=int(input("Enter vector size:"))
print("Enter v1")
for i in range(n):
	a=float(input())
	v1.append(a)
print("Enter v2")
for i in range(n):
	a=float(input())
	v2.append(a)

print("Dot product: ",dotProduct(v1,v2))
