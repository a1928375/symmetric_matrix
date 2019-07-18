def symmetric(x):

    i=0
    while i<len(x):
        j=0
        L=[]
        while i<len(x):
            if j<len(x):
                L.append(x[j][i])
                j=j+1
            else:
                if L==x[i]:
                    break
                else:
                    return False
        i=i+1
               
    return True

print (symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]]))

print (symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]]))
    
print (symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]]))
                
print (symmetric([[1, 2],
                [2, 1]]))
    
print (symmetric([[1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6]]))  
                
print (symmetric([[1,2,3],
                 [2,3,1]]))
    
