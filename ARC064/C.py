N,x = list(map(int,input().split(" ")))
a=list(map(int,input().split(" ")))

def solve(N,x,a):
	a.insert(0,0)
	count=0
	for i in range(len(a)-1):
		if a[i]+a[i+1]>x:
			eat=a[i+1]+a[i]-x
			count+=eat
			a[i+1]-=eat
	return(count)


print(solve(N, x, a))
