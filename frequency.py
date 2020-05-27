def most_frequent(a):
    print( "in the function")
    b = {} 
    for i in a: 
        if i in b: 
            b[i] += 1
        else: 
            b[i] = 1
    print ("Count of all characters in the string is :\n ",str(b))
    return 
st=input("Input the String:")
print (st)
most_frequent(st)


