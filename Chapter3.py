#Exercise 3.1.1
print('\n ***Exercise 3.1.1*** \n')
def right_justify(s):

    length = len('monty')
    
    spaces = 70 - length 
    print ("required space is",spaces)

    print(" " * spaces + s)

right_justify('monty')

#Exercise 3.2.1
print('\n ***Exercise 3.2.1***\n')
'''def print_spam():
    print('spam')
do_twice(print_spam)
'''
#Exercise 3.2.2
print('\n ***Exercise 3.2.2***\n')
def do_twice(name):
      print(name)
do_twice('Anurag')
do_twice('Shalabh')

#Exercise 3.2.3
print('\n ***Exercise 3.2.3***\n')
def print_twice(spam):
    print(spam)
    print(spam)
print_twice('spam')

#Exercise 3.2.4
print('\n ***Exercise 3.2.4***\n')
do_twice(print_twice('spam'))

