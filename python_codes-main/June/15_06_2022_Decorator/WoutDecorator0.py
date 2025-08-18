
def mult(fun):

    def inner(x):
        ans = fun(x)
        return ans * x

    return inner

def sqr(x):

    return x * x

num = int(input("Enter number : "))
retFun = mult(sqr)
print(retFun(num))
