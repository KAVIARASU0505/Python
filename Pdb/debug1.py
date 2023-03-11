#using import pdb we can debug this code
import pdb
def add(x,y):
 sum=x+y
 return sum
if __name__=="__main__":
 x=int(input("Num 1 is: "))
 y=int(input("Num 2 is: "))
 pdb.set_trace()
 z=add(x,y)
 print(z)
