
def varArgs(*args):

    for x in args:
        print(x)

varArgs(10,20,30)
varArgs(10,20,'A')
varArgs(10,20)
varArgs(10)

