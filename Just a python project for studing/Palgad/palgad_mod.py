palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]


def sorteerimine(p:list, o:list, a:int): #0 kasvab, 1 kahaneb
    N = len(p)
    if a == 0:
        for i in range(N):
            for j in range(i+1,N):
                if p[i]<p[j]:
                    abi = p[i]
                    p[i] = p[j]
                    p[j] = abi
                    abi = o[i]
                    o[i] = o[j]
                    o[j] = abi
    else:
        for i in range(N):
            for j in range(i+1,N):
                if p[i]>p[j]:
                    abi = p[i]
                    p[i] = p[j]
                    p[j] = abi
                    abi = o[i]
                    o[i] = o[j]
                    o[j] = abi
    return p, o
sorteerimine(palgad,inimesed,1)
for i in range(len(palgad)):
    print(f"{palgad[i]} - {inimesed[i]}")
