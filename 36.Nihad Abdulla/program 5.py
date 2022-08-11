def largest(a,b):
    bool=False
    for i in a:
        for j in b:
            if i==j:
                result=True
                return result
a=[1,2,3,4]
b=[8,6,7,9,1]
print(largest(a,b))
