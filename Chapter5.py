#Exercise 5.1.1
print("\n Exercise 5.1.1*** \n")
import time
def t():
    epoch=time.time()
    print(epoch,"epoch \n ")
    return epoch
t()
    
def t1():
    e_date = t() #e_date=epoch
    total_days = e_date // 3600 // 24
    print(total_days,"days since epoch")
    
    c_date = total_days * 24 * 3600

    seconds = e_date - c_date
    c_hours = seconds // 3600
    c_minutes = (seconds - (c_hours*3600))//60
    c_seconds =  seconds - (c_hours*3600 + c_minutes*60)
    c_time = "%s:%s:%s" % (c_hours,c_minutes,c_seconds)
    print(c_time,"ON",total_days,"Days Since Epoch")
  
t1()    

#Exercise 5.2.1
print("\n ***Exercise 5.2.1*** \n")
import math
def check_fermat(a, b, c, n):
    if n > 2 and (a**n + b**n == c**n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn’t work.")
check_fermat(3,5,6,3)

#Exercise 5.2.2
print("\n ***Exercise 5.2.2*** \n")
def check_numbers():
    a = int(input("Enter the Value for a: "))
    b = int(input("Enter the Value for b: "))
    c = int(input("Enter the Value for c: "))
    n = int(input("Enter the Value for n: "))
    return check_fermat(a, b, c, n)
check_numbers()

#Exercise 5.3.1
print("\n ***Exercise 5.3.1*** \n")
def is_triangle(x, y, z):
    if (x + y == z):
        print("Yes!")
    else:
        print("No!")
is_triangle(2,4,6)

#Exercise 5.3.2
print("\n ***Exercise 5.3.2*** \n")
def is_triangle_v():
    x = int(input("Enter the value for x: "))
    y = int(input("Enter the value for y: "))
    z = int(input("Enter the value for z: "))
    return is_triangle(x, y, z)
is_triangle_v()

#Exercise 5.4.1
print("\n ***Exercise 5.4.1*** \n")
def recurse(n, s):
    if n == 0:
        print(s)
    else:
            recurse(n-1, n+s)
recurse(3, 0)

#Exercise 5.4.2
print("\n ***Exercise 5.4.2*** \n")
print("\n if i called this function like this: recurse(-1, 0),then it will give a Recursion Error(Maximum Recursion depth exceeded in comparison) \n")
print("\n This is recursion function: \n first of all it will go to function recurse(), then for if conditon and go for else condition because if condition is false because n=3 \n now n=2,s=3 \n ")
print("\n Then again it will go to if condition then again it is false because this time n=2 again it will go for else condition and now n=1 , s=5 \n again it will go for if condition then again it is false and go for else condition \n now n=0, s=6 \n")
print("\n Again it come to if condition this time if condition is true and will print S that is 6.")



