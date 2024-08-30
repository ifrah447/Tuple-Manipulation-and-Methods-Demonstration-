# tuples are immutable means that we can't change the value of tuple after creation
tuple=("apple","banana","cherry",2,True)

# tuple[0]="orange" we are not allowed to do this in tuples
print(type(tuple))
print(tuple[:])
print(len(tuple))
print(tuple[-1])
# tuples can be uses where you want to store data that you don't want to change and keep it constant
if (2 in tuple):
  print("yes 2 is present in tuple")
tuple2=tuple[1:3]
print(tuple2)
# tup=(1,6,7,8,9,10,2,3,4,5)
# tup.sort()
# print(tup)
# day 25 manipulating tuples
# tuple is immutable
# methods used by tuples
a=(1,2,3,3,4,5,6,7,8,9,10,3,3,3,3,3,"ali","hussain","ifrah","farwa")
print(a.count(3))
print(a.index(1))
temp=list(a)
temp.pop(2)
temp.append("faraz")
print(temp)
a=tuple(temp)
print(a)     
b1=("car","bus","train","plane")
b2=("bike","cycle","scooter","bike","skateboard")
b3=b1+b2
for k in b3:
  print(k)
# (value,start,stop)
print(b3.index("bike",5,8))
