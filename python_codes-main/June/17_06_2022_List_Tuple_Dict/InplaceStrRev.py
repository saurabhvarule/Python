
def reverse(str1):

    str2 = str1[-1: : -1]

    return str2

num = int(input("Enter number of elements you want to append in the list : "))
lst = list()

for i in range(num):

    lst.append(input("Enter element : "))

for i in range(num):

    lst[i] = reverse(lst[i])

print(lst)
