#실행 테스트케이스 참고 사이트: http://cometouniverse.tistory.com/m/43
#알고리즘은 강의자료 토대로 짬
def optimalBST(bstSize, keyP):
    #초기화 시작
    i, j ,k , diagonal = 0, 0, 0, 0
    #[행][열] = [bs+2][bs+1]
    A = [[None]*(bstSize+1) for i in range(bstSize+2)]  
    #R리스트는 루트 노드의 인덱스
    R = [[None]*(bstSize+1) for i in range(bstSize+2)]    
    for i in range(1, bstSize+1):
        A[i][i-1] = 0
        A[i][i] = keyP[i]
        R[i][i] = i
        R[i][i-1] = 0
    A[bstSize+1][bstSize] = 0
    R[bstSize+1][bstSize] = 0
    #초기화 끝
    #계산 시작
    for diagonal in range(1, bstSize): #dia는 1부터 bs-1까지의 행에서 출발
        for i in range(1, bstSize-diagonal+1): # i는 1부터 bs-dia-1 행까지
            j = i + diagonal #j는 행인덱스 + 1 만 확인

            #minA함수는 길이 2의 리스트로 결과를 넘겨줌
            #결과 형태 [min(A[i][k-1]+A[k+1][j]), min일 경우의 k]
            minResult = minA(A, i, j) 
            A[i][j] = minResult[0] + sumP(keyP, i, j)
            R[i][j] = minResult[1]

    #return A[1][n]
    return A, R


def minA(A, i, j):
    answer = 0.0
    answerK = i+1
    answer = A[i][answerK-1]+A[answerK+1][j]
    for k in range(i+2, j+1):
        temp = A[i][k-1]+A[k+1][j]
        if answer > temp:
            answer = temp
            answerK = k
    return (answer, answerK)

def sumP(keyP, i, j):
    answer = 0.0
    for m in range(i, j+1):
        answer += keyP[m]
    return answer
        
                  


##테스트코드
if __name__ == "__main__" :
    P = [0 , 3.0/16, 4.0/16, 5.0/16, 3.0/16, 1.0/16]
    result = optimalBST(5, P)
    A = result[0]
    R = result[1]
    for i in range(1, 6):
        for j in range(i, 6):
            print("A[%d][%d] = %lf" % (i, j, A[i][j]))
    for i in range(1, 6):
        for j in range(i, 6):
            print("R[%d][%d] = %d" % (i, j, R[i][j]))

'''실행결과
P_1, P_2, P_3, P_4, P_5 = 3/16, 4/16, 5/16, 3/16, 1/16
A[1][1] = 0.187500
A[1][2] = 0.625000
A[1][3] = 1.250000
A[1][4] = 1.750000
A[1][5] = 2.062500
A[2][2] = 0.250000
A[2][3] = 0.812500
A[2][4] = 1.187500
A[2][5] = 1.500000
A[3][3] = 0.312500
A[3][4] = 0.812500
A[3][5] = 0.937500
A[4][4] = 0.187500
A[4][5] = 0.437500
A[5][5] = 0.062500
R[1][1] = 1
R[1][2] = 2
R[1][3] = 2
R[1][4] = 3
R[1][5] = 3
R[2][2] = 2
R[2][3] = 3
R[2][4] = 3
R[2][5] = 3
R[3][3] = 3
R[3][4] = 4
R[3][5] = 4
R[4][4] = 4
R[4][5] = 5
R[5][5] = 5
'''
