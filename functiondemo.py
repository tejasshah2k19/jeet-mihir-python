#no return with argument 
#return no argument
#return with argument
 
#no return no argument
def add():
    print("Enter two number")
    a=input() # 10
    a = int(a) 
    b= int(input()) # 20 
    c=a+b #1020 
    print("add = ",c)

#no return with argument 
def sub(a,b):
    c = a-b
    print("sub = ",c)

#return no argument
def mul():
    print("Enter two number")
    a=input() # 10
    a = int(a) 
    b= int(input()) # 20 
    c=a*b #1020 
    return c 

# return with argument 

def sqr(n):
    //print 
    return n*n


# core = getCurrentCoreSize() // 16 
# if(core >= 5 ):
#     do multithread
# else:
#     dosinglethread 

#mobile -> battery ?

def cube(b):
    return a*a*a

def sum(*a):
    s = 0
    for data in a:
        s = s + data 

sum(1)
sum(1,2)
sum(23,23,4,435,5)

print("out of the function ")

add() # call 
print("\nEnter two num for subtraction ")
x = int(input())
y = int(input())
sub(x,y)

ans = mul() 
print("mul = ",ans)

ans = sqr(5)
print("sqr = ",ans)

print("sqr = ",sqr(6))

#user = login(email,password)

