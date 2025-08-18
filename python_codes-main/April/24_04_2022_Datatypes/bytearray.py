
data = [10,20,30,40,50]
dataArray =  bytearray(data)
print(dataArray)    #Print address of bytearray
print(dataArray[1])
print(type(dataArray))
print(type(dataArray[1]))

print(dataArray[2])
dataArray[2] = 100
print(dataArray[2])

#data1 = [10, 20, 30, 40, "Harsh"]
#data1Array = bytearray(data1)       #TypeError: 'str' object cannot be interpreted as an integer
