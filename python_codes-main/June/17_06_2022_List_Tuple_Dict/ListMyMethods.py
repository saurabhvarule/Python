
country = list()

def myClear(lst):
    lst1 = []
    lst = lst1
    return lst

def myCopy(lst):
    lst1 = lst
    return lst1

def myCount(ele):
    count = 0
    for i in country:
        if(i == ele):
            count += 1
    return count

def myIndex(ele):
    count = 0
    flag = 0
    for i in country:
        if(i == ele):
            flag = 1
            return count
        count += 1
    if(flag == 0):
        print("ValueError: ", ele, " is not in list")
        return ''

def myInsert(i, ele):

    country.append(ele)
    temp = country[i]
    country[i] = country[len(country)-1]
    country[len(country)-1] = temp
    return country

def myPop():
    lst1 = country[0:len(country)-1:1]
    return lst1

num = int(input("Enter number of elements you want to append : "))

for i in range(num):
    country.append(input("Enter country name : "))

print(id(country))

#country = myClear(country)
#print(country)

#lst2 = myCopy(country)
#print(lst2)

#print(myCount("UK"))

#print(myIndex("UK"))

#print(myInsert(1, "UK"))

country = myPop()
print(country)
print(id(country))



