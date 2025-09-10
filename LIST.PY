a=[]
n=int(input("enter the number of elements:"))
for i in range(0,n):
   m=int(input("enter the element:"))
   a.append(m)
   a.extend([8,9,10])
   a.insert(0,1)
print(a)
print("element in first position:",a[0])
print("element in last position:",a[-1])
print("elements in middle position:",a[4:7])
print("element in last 3 positions:",a[-3:])
 
