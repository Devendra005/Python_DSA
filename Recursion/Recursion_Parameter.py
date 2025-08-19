# Print x , N times 
def func(x,n):
    if n == 0:
        return    
    print(x)
    func(x,n-1)
func(15,4)

# Print 1 to N using recursion 
def fun(i,N):
    if i>N:
        return
    print(i)
    fun(i+1,N)
fun(1,4)

# N to 1 using tail recursion [backtracking]
def tail(i,N):
    if i > N:
        return
    tail(i+1,N)
    print(i)
tail(1,4)

# N to 1 don't use i+1 (head recursion)
def head(N):
    if N == 0:
        return
    print(N)
    head(N-1)
head(4)

# 1 to N using tail recursion {backtracking}
def back(i,N):
    if i > N:
        return
    print(i)
    back(i+1,N)
back(1,4)