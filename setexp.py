import time
fruit={"apple","Grpaes"}
print(fruit)
fruit.add("orange")
print(fruit)
animals=frozenset(["tiger","lion"])
print(animals)
#animals.add("cat")
#print(animals)
list=[]
print(list)
emptyset={}
print(type(emptyset))

#create an empty set
newemptyset=set()
print(type(newemptyset))

num={1,2,3,4,5,6}
#copy one set value to another set
num2=set(num)
print(num2)
#membership operation
print(6 in num)
print(111 in num)
#add operation
num.add('111')
print(num)
#remove operation
num.remove(2)
print(num)
#union operation in set
s1={1,5,3,8,9}
s2={"apple",1,2,8,"tiger"}
print(s1|s2)
#intersection operation in set
print(s1&s2)

#Difference operation in set
print(s1-s2)
print(s2-s1)#which are in s2 but not in s1
#symmetric Difference
print(s1^s2)#which are not common in both
print(len(s1))
#copy operation
c=s1.copy()
print(c)
#clear operation
num.clear()
print(num)
for i in s1:
    time.sleep(2)
    print(i)