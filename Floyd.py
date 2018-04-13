import time

class Floyd:
	def __init__(self, W):
		self.W = W

	def Min(a, b):
		if a== None:
			return b
		return a <= b and a or b


	def Dynamic(self, n):
		self.P = [[0]*(len(self.W)) for i in range(len(self.W))]
		D = self.W;
		for k in range(1, n+1):
			for i in range(1, n+1):
				for j in range(1, n+1):
					if D[i][k]!=None and D[k][j]!=None :
						D[i][j] = Floyd.Min(D[i][j], D[i][k] + D[k][j])
						# k -> j 가는 경로가 기록이 없다면 신규 경로 이고, 있다면 경유지의 경유지이다.
						if self.P[k][j] == -1:
							self.P[i][j] = k
						else:
							self.P[i][j] = self.P[k][j];
				
		return D
	
##테스트코드
if __name__ == "__main__" :
	W = [[],
		[None, 0, 4, -1, 8],
		[None, None, 0, -2, -10],
		[None, None, None, 0, 3],
		[None, None, None, None, 0]
		]
	'''W = [[],
		[None, 0, 1, None, 1, 5],
		[None, 9, 0, 3, 2, None],
		[None, None, None, 0, 4, None],
		[None, None, None, 2, 0, 3],
		[None, 3, None, None, None, 0],
		]'''
		
	for i in range(len(W)):
		f = Floyd(W)
		for row in f.Dynamic(i):
			for item in row:
				print("%5s" % str(item), end=" ")
			print()

	
	


