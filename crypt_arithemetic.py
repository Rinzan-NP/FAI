from itertools import permutations as p

w1 = "send"
w2 = 'more'
w3 = "money"

l1 = list(w1)
l2 = list(w2)
l3 = list(w3)
dt = dict()
x =list(set(l1+l2+l3))

for i in p(range(0,10),len(x)):
    count = 0
    for j in i:
        dt[x[count]] = j
        count+= 1
    # print(dt)
    if dt[l1[0]] == 0 or  dt[l2[0]] == 0 or dt[l3[0]] == 0 or dt[l3[0]] != 1: 
        continue
    else:
        n1 = ""
        for wd in  l1:
            n1 += str(dt[wd])    
        n1 = int(n1)

        n2 = ""
        for wd in  l2:
            n2 += str(dt[wd])    
        n2 = int(n2)

        n3 = ""
        for wd in  l3:
            n3 += str(dt[wd])    
        n3 = int(n3)

        if  n1+n2 == n3:
            print("Found")
            print(dt)
            break



