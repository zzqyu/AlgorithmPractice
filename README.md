<style id="jsbin-css">
    @import url(//fonts.googleapis.com/earlyaccess/jejugothic.css);
    body { font-family: 'Jeju Gothic', sans-serif;}
</style>
<body>

# Practice programming the Algorithm using Python 3.x

이 프로젝트는 3학년 1학기 전공 알고리즘을 이해하기 위해 파이썬으로 알고리즘을 짜보려고 만들었다.

## [BinomalCoefficient](https://github.com/zzqyu/AlgorithmPractice/blob/master/BinomalCoefficient.py)
* 이항계수 코드이다. 아래는 짜본 방식이다.
* 재귀(Recursion)
* 메모이제이션(Memoization)
* 동적 프로그래밍 (Dynamic Programing)
* 개념
    * C(n, 0) = 1, C(n, n) = 1
    * C(n, r) = C(n-1, r-1) + C(n-1, r)
* 시간복잡도 <br>
    n = 5, r = 3 <br>
    n\r0 &nbsp; 1 &nbsp; 2 &nbsp; 3 &nbsp; 4 <br>
    0 &nbsp; 1&nbsp;<br>
    1 &nbsp; 1 &nbsp; 1<br>
    2 &nbsp; 1 &nbsp; 2 &nbsp; 1<br>
    3 &nbsp; 1 &nbsp; 3 &nbsp; 3 &nbsp; 1<br>
    4 &nbsp; 1 &nbsp; 4 &nbsp; 6 &nbsp; 4&nbsp;<br>
    5 &nbsp; 1 &nbsp; 5&nbsp; 10 &nbsp;10&nbsp;<br>

    * n &nbsp; r<br>
      0 &nbsp; 1<br>
      1 &nbsp; 2<br>
      2 &nbsp; 3<br>
      3 &nbsp; 4<br>
      4 &nbsp; 4<br>
    ...  ...<br>
      n &nbsp; r+1<br>
    * #### 그래서 시간복잡도는 nk에 가까움.



## [Floyd's Algorithm](https://github.com/zzqyu/AlgorithmPractice/blob/master/Floyd.py)
* 동적 프로그래밍(Dynamic Programing) 소스 작성했다.
* 각 점에서 다른점에 가는 모든 최단경로 구하기
* D(k)[i][j]=세트 {V1, V2, …, Vk}의 점을 중간 경유점으로 사용하여"Vi"부터 "Vj"까지 가장 짧은 경로의 길이
* D(0)[i][j]=W[i][j]
* 재귀 경우 1
    * § D(k)[i][j]=세트 {V1, V2, …, Vk}의 점을 중간 경유점으로 사용하여"Vi"부터 "Vj"까지 가장 짧은 경로의 길이이기 때문에 D(k-1)[i][j]의 경우를 포함하고 있음
	    * § D(k)[i][j] = D(k-1)[i][j]
* 재귀 경우 2
    * § Vi부터 Vk의 경로 + Vk 부터 Vj의 경로가 Vi->Vj경로임
	    * § D(k)[i][j] = D(k-1)[i][k] + D(k-1)[k][j]
* 결과적으로 위 2가지 경우 중 길이가 짧은게 최단경로




## [BinarySearchTree](https://github.com/zzqyu/AlgorithmPractice/blob/master/BinarySearchTree.py)
* 바이너리서치트리최적구조 ... 좀더 공부를...

</body>
