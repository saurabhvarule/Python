
# Sequence Type-
#   1. bytes- Immutable
#   2. bytearray- Mutable
# This is not a bytes datatype here I have created list. 
# To create a bytes datatype, we have to create list and typecast it to the bytes

data = [10, 20, 30, 40, 255]
print(data[1])
print(data[4])
print(data[0])
print(type(data[0]))
print(type(data))

# Here is how its done.

databyte = bytes(data)

print(databyte)         # If I print like this it will print array.
print(type(databyte))
print(databyte[0])
print(type(databyte[0]))
# databyte[2] = 50      # TypeError: byte object does not support item assignment

x = 10

xdata = bytes(x)        #Even though bytes is sequence datatype, we can also store single element in it.
print(type(xdata))


