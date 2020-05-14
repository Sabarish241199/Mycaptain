l=input("input the length of the list:")
a=list()
b=list()
print("Enter the list")
for i in range(l):
    x=int(input())
    a.append(int(x))
for i in range(l):
    if a[i]>0:
        b.append(a[i])
print b