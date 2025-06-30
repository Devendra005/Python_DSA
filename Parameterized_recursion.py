# sum of 1 to N [Parameterized way]

def func(sum, i, N):
    if i > N:
        print(sum)
        return
    func(sum+i,i+1,N)
func(0,1,4)

# [Functiona recursion]
def fun(N):
    if N == 1:
        return 1
    return N+fun(N-1)
print(fun(10))

# Factorial of 5 
def fun(N):
    if N == 1:
        return 1
    return N*fun(N-1)
print(fun(5))