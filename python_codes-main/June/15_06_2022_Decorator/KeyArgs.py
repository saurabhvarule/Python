
def keyArgs(**args):

    #print(args)

    for x,y in args.items():
        print(x, '=', y)

keyArgs(a = 10, b = 20)
keyArgs(a = 10, b = 20, c = 30)
keyArgs(a = 10)
