l=int(input("Fibanocci numbers you want:"))
fn=list()
fn=[0,1]
i=2
while i<l:
    a=fn[i-1]+fn[i-2]
    fn.append(a)
    i=i+1
print fn
