my_set = {1, 2, 3, 4,5}
my_set.remove(4)
print(my_set) #{1, 2, 3, 5}
# checking if an element is in a set
print(3 in my_set) #True
print(4 in my_set) # False
#length 
my_set = {1, 2, 3, 5}
print(len(my_set)) #4
# copy
my_set = {1, 2, 3, 5}
new_set = my_set.copy()
print(new_set) #{1, 2, 3, 5}
# clear
my_set = {1, 2, 3, 5}
my_set.clear()
print(my_set) #set()
#union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set) #{1, 2, 3, 4, 5}
#intersection
intersection_set = set1.intersection(set2)
print(intersection_set) # prints {3}
# difference
difference_set = set1.difference(set2)
print(difference_set) # prints {1, 2}
#symmetric difference(omits intersection)
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set) #{1, 2, 4, 5}
# checking if a set is a subset of another 
#issubset
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set={1, 2, 3, 4, 5}
print(set1.issubset(union_set)) #True
print(set2.issubset(union_set)) #True
# checking if a set is a superset of another set
#issuperset
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set={1, 2, 3, 4, 5}
print(union_set.issuperset(set1)) #True
print(union_set.issuperset(set2)) #True
# checking if two sets have any elements in common
#returns True if none of the items are present in both sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.isdisjoint(set2)) #False
print({6, 7, 8}.isdisjoint(set2)) #True
# adding all elements of another set to a set
my_set=()
set2=(3,4,5)
my_set.update(set2)
print(my_set) #{3, 4, 5}
#File Manuplation
#shutil(module)
#shutil.copy()
import shutil
source_file = 'path/to/source/file'
destination_file = 'path/to/destination/file'
shutil.copy(source_file, destination_file)
#ex 2
import shutil
source = "/home/User/Documents/file.txt"
destination = "/home/User/Documents/file.txt"
try:
    shutil.copy(source, destination)
    print("File copied successfully.")
except shutil.SameFileError:
    print("Source and destination represents the same file.")
except PermissionError:
    print("Permission denied.")
except:
    print("Error occurred while copying file.")
#shutil.move()
import shutil
source_file = 'path/to/source/file'
destination_file = 'path/to/destination/file'
shutil.move(source_file, destination_file)
#os.reomve
import os
file_path = 'path/to/file'
os.remove(file_path)
# Close the file
file_path.close()
#Open a file for read
f = open('myfile.txt', 'r')
# Read the entire contents of the file
content = f.read()
print(content)
# Read a single line from the file
line = f.readline()
print(line)
# Read all lines from the file and print them
lines = f.readlines()
for line in lines:
    print(line)
# Write to a file
f = open('newfile.txt', 'w')
f.write('This is a new file.')
f.close()
# Rename a file
import os
os.rename('myfile.txt', 'renamed.txt')
# Check if a file exists
if os.path.exists('myfile.txt'):
    print('File exists')
else:
    print('File does not exist')
# Get current working directory
cwd = os.getcwd()
print(cwd)
lambda **kwargs: sum(kwargs.values())(one=1, two=2, three=3) #5
#Simple decorators
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")
say_whee()
#Something is happening before the function is called.
#Whee!
#Something is happening after the function is called.
#recalling the decorators
def do_twice(fun):
    def wrapper_twice():
        fun()
        fun()
    return wrapper_twice

@do_twice
def caller():
    print("twice")
caller()