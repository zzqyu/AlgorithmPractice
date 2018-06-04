import sys
def Kruskal(W):
    n = len(W)-1
    E=[]
    F=[]
    UsingE=[]
    for i in range(1, n+1):
        for j in range(i, n+1):
            if W[i][j] != sys.maxsize:
                E.append([W[i][j], i, j])
    E = sorted(E, key = lambda x: x[0])
    for e in E:
        i, j = e[1], e[2]
        if not IsCycle(UsingE, i, j):
            UsingE.append(e)
            F.append([e[1],e[2]])
        if len(F)==n-1:
            break
    return F
def IsCycle(F, i, j):
    f = F.copy()
    a = [i, j]
    while True:
        b = list(filter(lambda x : x[1]==a[0] ,f))
        if len(b) > 0:
            a.insert(0, b[0][2])
            f.remove(b[0])
            continue
        b = list(filter(lambda x : x[2]==a[0] ,f))
        if len(b) > 0:
            a.insert(0, b[0][1])
            f.remove(b[0])
            continue
        b = list(filter(lambda x : x[1]==a[-1] ,f))
        if len(b) > 0:
            a.append(b[0][2])
            f.remove(b[0])
            continue
        b = list(filter(lambda x : x[2]==a[-1] ,f))
        if len(b) > 0:
            a.append(b[0][1])
            f.remove(b[0])
        else :
            break;
    return a.count(i)==2 or a.count(j)==2

        
m = sys.maxsize;
W = [
    [m, m, m, m, m, m],
    [m, m, 1, 3, m, m],
    [m, 1, m, 3, 6, m],
    [m, 3, 3, m, 4, 2],
    [m, m, 6, 4, m, 5],
    [m, m, m, 2, 5, m]
    ]
print(Kruskal(W))