import sys
def Prim(W):
    size = len(W)-1 #행렬의 사이즈
    vNear = 0 # 각 경우에서 거리가 가장 짧은 vertice의 번호
    #nearest = [1] * (size+1) 
    #각 경우의 거리 리스트
    distance = [sys.maxsize, sys.maxsize]
    F = [] #경유 순서 저장하는 리스트

    # 1번vertice와 연결과 각 vertice와의 거리 설정
    for i in range(2, size+1):
        distance.append(W[1][i])

    #다음에 가야할 vertice 구하는 부분
    for i in range(size-1):
        #최소값을 int의 최대수로 설정
        _min = sys.maxsize;
        # 이미 경유 했던 곳(-1)
        # 최소 길이인 경우 구하기
        for j in range(2, size+1):
            if(0<= distance[j] < _min):
                _min = distance[j] #최소 거리
                vNear = j # 최소거리인 vertice 번호
        F.append(vNear) # 다음에 경유할 vertice를 넣는다.
        distance[vNear] = -1 #이미 경유한 곳을 -1로 바꾼다.
        #경유하지 않았던 곳에 대한 거리를 가져온다. 
        for j in range(2, size+1):
            if(W[j][vNear] < distance[j]):
                distance[j] = W[j][vNear]
                #nearest[j] = vNear
    return F;
m = sys.maxsize;
W = [
    [m, m, m, m, m, m],
    [m, m, 1, 3, m, m],
    [m, 1, m, 3, 6, m],
    [m, 3, 3, m, 4, 2],
    [m, m, 6, 4, m, 5],
    [m, m, m, 2, 5, m]
    ]
print(Prim(W))