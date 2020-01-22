#Exercise 2.1.1
print('\n ***Exercise 2.1.1*** \n')
n=42
print(n)
print('\n We’ve seen that n = 42 is legal. What about 42 = n,It gives a syntax error(Can not assign to literal)\n')

#Exercise 2.1.2
print('\n ***Exercise 2.1.2*** \n')
x=y=1;
print(x)
print(y)
print('\n How about x = y = 1, it will return the value of x=1 and y=1 \n')

#Exercise 2.1.3
print('\n ***Exercise 2.1.3*** \n')
print(n*x);
print('\n In some languages every statement ends with a semicolon, ;. What happens if you put a semicolon at the end of a Python statement,nothing it depends upon you')

#Exercise 2.1.4
print('\n ***Exercise 2.1.4*** \n')
a=2. #it turn a integer  no. into floating number
print(a)
#print(a).
print('\nWhat if you put a period at the end of a statement, it gives a syntax error(Invalid syntax) ')

#Exercise 2.1.5
print('\n ***Exercise 2.1.5*** \n')
x=23
y=45
print(x*y)
#print(xy)
print('\n In math notation you can multiply x and y like this: . What happens if you try that in Python,it gives a name error(name xy is not defined)what means python treat it as name')

#Exercise 2.2.1
print('\n ***Exercise 2.2.1*** \n')
pi= 3.141592653589793
r= 5
v=4/3*pi*r**3
print('\n the volume of a sphere with radius 5 is')
print(v)

#Exercise 2.2.2
print('\n ***Exercise 2.2.2*** \n')
bookprice=24.95
discount=bookprice*(40/100)
shippingpriceother=.75
shippingpricefirst=3
totalcopies=60
BookpriceWithoutSC =bookprice-discount
totalbookpricewithoutsc = BookpriceWithoutSC*totalcopies
totalsc = shippingpricefirst+(shippingpriceother*59)
print('\n the total wholesale cost for 60 copies  is ')
print(totalbookpricewithoutsc+totalsc)

#Exercise 2.2.3
print('\n ***Exercise 2.2.3*** \n')
seconds = 1
hours = seconds / (60*60)
seconds = seconds - hours*60*60
minutes = seconds / 60
seconds = seconds - minutes *60
print(hours)

