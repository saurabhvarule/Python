
def mult(fun):

    print("Start : In mult")
    
    def inner(x):
        print("Start : In inner before function call")
        ans = fun(x)
        print("End : In inner before function call")
        return ans * x

    print("End : In mult")
    return inner

@mult
def sqr(num):
        
    print("Start : In sqr")
    
    return num * num

print("Start")
num = int(input("Enter the number : "))
print(sqr(num))
