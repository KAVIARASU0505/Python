list=[2,4,6,8,10,12,8,14,16,18,20]
list.append(14)
print(list)
list.remove(8)
print(list)
list1=[10,20,30,40]
list.extend(list1)
print(list)
list.insert(6,9)
print(list)
list.pop(11); #It will delete the index what we given in the pop
print(list)
a=list.pop() #If value is not given it will delete the last element in the item.
print(list) 
print(a)   #We can store the Pop Value in another declaration.
#list.clear() -->Removes all the items in the list.
#del list[:]  -->It will also Clear the list.
#print(list)
list1=list.index(16,2,100);
print(list1)
list.append(16)
print(list)
list2=list.index(16,2,30)
print(list2)
print(list.count(20))
list.reverse();
print(list)
list.sort(reverse=True);
print(list)
list.sort();
print(list);
list2=(list.copy());
print(list2)
#Using list as queue
from collections import deque
list3=deque(list2)
list3.appendleft(765)
print(list3)
list3.popleft()
print(list3)
list3.reverse();
print(list3)
list3.extendleft([1,2,3])
print(list3)
list3.rotate(5)  # The rotation take from right
print(list3)
list3.rotate(-5)  # The rotation take from left
print(list3)
#list3.clear();
#print(list3)
print(10 in list3);
list4=deque(reversed(list3))
print(list4)
#list Comprehensions
Array = [x**4 for x in range(8)]
print(Array)
array1=Array.copy();
print(array1)
arr=[[x,y] for x in [1,2,3] for y in [3,1,4]]
print(arr);
arr1=[x*2 for x in list]
print(arr1)
arr2=[x for x in list if(x<18)]
print(arr2)
list4=[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13]
arr3=[abs(x) for x in list4]
print(arr3)
animal=[" Dog","Monkey    ","Ca   t","snake                    ","Ele  phant"]
arr4=[str.strip(" ") for str in animal] # we can use strip for only removing the specified case if the word it contains in the last or first continuosly.
print(arr4)
#create 2 tubles
arr5=[(x,x**2) for x in [1,2,3,4,5,6,7,8,9]]  #if paranthesis is not given it will show as Invalid syntax error.
print(arr5)
#To flatten a list
list5=[[2,4,5,3,4],[6,7,8,9],[3,6,3,1,6,7]]
arr6=[new for nil in list5 for new in nil]
print(arr6)
arr6.sort();
print(arr6)
from math import pi
arr7=[round(pi,i) for i in range(1,7)]
print(arr7)
#Nested list Comprehensions
#Transpose Matrix
Matrix1=[[1,2,3],
        [4,5,6],
        [7,8,9]]
arr7=[[row[i] for row in Matrix1]for i in range(3)]
print(arr7)
x=[1,2,4,5,6,7,8,9,10,12]
del x[3];
print(x)
del x[4:]
print(x);
#Tuples and Sequences
y=245345,'Hello','Everyone'
print(y)
p=y,('Kavi',"Arasu","c") #
print(p)
Raw='Name',"New"
print(type(Raw))
print(Raw)
print(len(Raw))
#Sets
animal={"dog","cat","Girafee","Monkey","cat","dog","Kangaroo"};
print(animal);# sets will show random values everytime running
# We can also define the input as set
str=set('1234561489');
str1=set('adfgvbhjnhjnkm')
print(str)
print(str1)
print(str-str1) # It will show output of the first declared str only
print(str|str1) # It will result as str or str1
print(str&str1) #& symbol will show same values between them
print(str^str1)
