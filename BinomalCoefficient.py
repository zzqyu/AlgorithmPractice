import time

class Coefficient:
	def __init__(self):
		Coefficient.C = []
	def Recursion(n, r):
		if n==r or r==0:
			return 1
		return Coefficient.Recursion(n-1, r-1) + Coefficient.Recursion(n-1, r)

	def Memoization(n, r):
		Coefficient.C = [[None]*(n+1) for i in range(n+1)]
		return Coefficient.Recursion2(n, r)

	def Recursion2(n, r):
		if Coefficient.C[n][r] == None:
			if n==r or r==0:
				Coefficient.C[n][r] = 1
			else:
				Coefficient.C[n][r] = Coefficient.Recursion(n-1, r-1) + Coefficient.Recursion(n-1, r)
		
		return Coefficient.C[n][r]
	
	def DynamicPrograming(n, r):
		Coefficient.C = [[None]*(n+1) for i in range(n+1)]
		for _n in range(n+1):
			for _r in range(_n+1):
				if _n==_r or _r==0:
					Coefficient.C[_n][_r] = 1
				else:
					Coefficient.C[_n][_r] = Coefficient.C[_n-1][_r-1] + Coefficient.C[_n-1][_r]
		return Coefficient.C[n][r]
##테스트코드
if __name__ == "__main__" :
	n = 25
	r = 23
	startTime = time.time()
	print (Coefficient.Recursion(n, r))
	print ("time ", time.time()-startTime)
	startTime = time.time()
	print (Coefficient.Memoization(n, r))
	print ("time ", time.time()-startTime)
	startTime = time.time()
	print (Coefficient.DynamicPrograming(n, r))
	print ("time ", time.time()-startTime)

	
	


