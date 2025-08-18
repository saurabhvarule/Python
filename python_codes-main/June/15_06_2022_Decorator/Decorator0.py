
def mult(fun):

    def inner(x):
        ans = fun(x)
        return ans * x
    return inner

@mult
def sqr(num):
    
    return num * num

num = int(input("Enter the number : "))
print(sqr(num))
