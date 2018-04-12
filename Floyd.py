import time

class Floyd:
	def __init__(self):
		Floyd.W = [[],
				[None, 0, 1, -1, 1, 5],
				[None, 9, 0, 3, 2, -1],
				[None, -1, -1, 0, 4, -1],
				[None, -1, -1, 2, 0, 3],
				[None, 3, -1, -1, -1, 0],
				]
		'''self.D = [[None]*(i+1) for n in range(j+1)]
		self.i = i
		self.j = j'''

	

	def Min(a, b):
		if a==-1:
			a=100
		return a<=b and a or b

	def Recursion(self, k, i, j):
		if k==0 and Floyd.W[i][j] >= 0:
			return Floyd.W[i][j]
		return Floyd.Min(self.Recursion(k-1, i, j), self.Recursion(k-1, i, k) + self.Recursion(k-1, k, i))
		
	
##테스트코드
if __name__ == "__main__" :
	f = Floyd()
	print(f.Recursion(4, 1, 3))

	
	


