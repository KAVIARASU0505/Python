print(2+4+6+8); #Execute only in BODMAS rule
print(3+(5/4)*5); #Execute only in BODMAS rule
print(5*5/4); #Execute only in BODMAS rule
print(19/3); #Execute only in BODMAS rule
print(19//3); #Execute only in BODMAS rule
print(19%3); #Execute only in BODMAS rule
print(19*5+4-8); #Execute only in BODMAS rule
print(6**2) #This symbol will be used for power.
a=10
b=20
print(a+b)
value1=100
value2=200
value3=200
print(value1+value2/value3)
#Strings
print("Kaviarasu")
print('Kaviarasu')
print("Hi 'Everyone'")
print('It is doesn\'t look like good')  #\-->The Backslash symbol is used for 
print("He said \"good\"")
print('Aren\'t you')
a="How are you?\nI am Fine"; #\n -->It is used for new line creation
print(a)
print(r"Not Bad C:\Dir\file\main\Day1") #-->The r symbol is used as a raw string.So that the backslash will print as it given in he quotes.
print("""https://www.google.com/search?q=is+triple+quotes+and+raw+string+same+in+python&client=ubuntu""")
#-->""" quotes are used to span multiple line in a string
print(5*'new'+"older")
print('kavi''arasu'+30*' '+3*'kavi')
print('new'"older")
new=("Our world is full of" #--> parentheses symbol is used here for connection two strings in different lines.
" pollution")
print(new)
new1='Hunter';
new1='animal';
print(new1)
print(new1+' Human')
Name="Kaviarasu";
print(Name[0])
print(Name[-1])
#print(Name[-10]) --> It will show an error of string index out of range
print(Name[0:4])  #-->We can slice a word of what we required.
print(Name[:2])
print(Name[2:])
print(Name[:4]+Name[4:8])
print(Name[:-4]+Name[-4:-2])   
print(Name[30:]) #-->If out of range means in this context it will shoe only white spaces.
print(Name[10:40]); #-->It will also create an empty space
# Name[0]='J'  -->It will shows an 'str' object does not support item assignment as an error.
Name1='R'+Name[1:]
print(Name1)
Name2=Name[:4]+'Kumar'
print(Name2)
Name3=Name[:4]+"arasu"+Name2[-5:]
print(Name3)
print(len(Name))
print(len(Name1))
print(len(Name2))
print(len(Name3))
#Lists
arrays=[1,2,3,4,5,6,7,8,9];
print(arrays);
print(arrays[0]);
print(arrays[-5])
print(arrays[-4:])
print(arrays[:5])
print(arrays[:5]+[1,2,4,5,5])
print(arrays+[9,8,7,6,5,4,3,2,1])
arrays[4]=4
print(arrays)
print(arrays[:])
print(arrays[1]**4)
arrays.append(10)
print(arrays)
arrays.append(2**4)
print(arrays)
words=['a','b','c','d','e','f','g','h']
print(words[2:])
print(words[4:20])
words[2:5]=['C','D','E','F','G','H'] #We can add extra elements in this array without deleting next.
print(words)
words[7:10]=[]
print(words)
#words[:]=[] -->If we give this all words array got deleted.
print(len(words))
#We can also do nest using new array declaration
num=[1,2,3,4,5]
a=[words,num]
print(a)
print(a[0])
print(a[0][4])
print(a[0][0:3])
print(a[1])
print(a[1][4])
print(a[1][:2])
#Fibonacci Series
a,b=0,1
print(a)
print(b)
while(a<10):
    print(a,end=',')
    a,b=b,a+b
c=300+175
print("The percentage of the mark is ",c/5)


