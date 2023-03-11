#import debug
#import pdb
#pdb.run("debug.main()")
#It is used in the terminal
def add(x,y):
    sum=x+y
    return sum
def main():
    x=int(input("Num 1 is: "))
    y=int(input("Num 2 is: "))
    z=add(x,y)
    print(z)
if __name__=="__main__":
    main()

