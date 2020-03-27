
def getMinSteps(n, memo):

	if (n == 1):
		return 0
	if (memo[n] != -1):
		return memo[n]

	res = getMinSteps(n-1, memo)

	if (n%2 == 0):
		res = min(res, getMinSteps(n//2, memo))
	if (n%3 == 0):
		res = min(res, getMinSteps(n//3, memo))

	# store memo[n] and return
	memo[n] = 1 + res
	return memo[n]

# This function mainly
# initializes memo[] and
# calls getMinSteps(n, memo)
def getsMinSteps(n):

	memo = [0 for i in range(n+1)]

	for i in range(n+1):
		memo[i] = -1

	return getMinSteps(n, memo)

n = 10
print(getsMinSteps(n))
