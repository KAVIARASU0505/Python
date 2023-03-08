f=open('/home/kaviarasuchinnu/Python-Impact Training/FileManipulation/file.txt','r')
print(f.readline(),end="")
print(f.readline(),end="")
f1=open('abc.txt','w')
f1.write("Something\nHappy")
f1=open("abc.txt",'a')
f1.write("\tEnvironment\n")
for i in f:
    f1.write(i)
f2=open("road-1072821__480.jpg",'rb')
for i in f2:
    print(i)
f3=open("My_pic.jpg","wb")
for i in f2:
    f3.write(i)
a=()