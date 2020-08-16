def xor(vl , xorvl):
    if vl == xorvl:
        return 0
    else:
        return vl^xorvl

def query(lts , vl1 , vl2):
    if vl1==0:
        lts.append(vl2) 
        return lts
    else:
        newlts =[]
        for x in lts:
            xorki = xor(x ,vl2)
            newlts.append(xorki)    
        return newlts

test_case =  int(input())
while test_case:
    test_case-=1
    hplts =[0]
    no_of_queries = int(input())
    for i in range(no_of_queries):
        a,b = input().split( )  
        a = int(a)
        b=int(b)   
        nayalist = query(hplts , a , b)
        hplts = nayalist
    nayalist.sort()
    print(*nayalist)
    
