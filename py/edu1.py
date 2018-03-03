import sys

print ('1')
print (sys.version)
print (2 ** 3)

m = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
#for key in m:
#    print(key, m[key])

num = 3;num_sqrt = num ** 0.5;print('The square root of %0.3f is %0.3f' % (num, num_sqrt))


#x = input("something:")
#print(x)


#x = raw_input("somethingR:")
#print(x)

a = b = c = 1
print (a);print (b);print (c)

a, b, c = 3, 4, "john"
print (a);print (b);print (c)

print ("str")
str = 'Hello World!'
print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string


print ("list")
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print (list)          # Prints complete list
print (list[0])       # Prints first element of the list
print (list[1:4])     # Prints elements starting from 2nd till 3rd
print (list[2:])      # Prints elements starting from 3rd element
print (tinylist * 2)  # Prints list two times
print (list + tinylist) # Prints concatenated lists


print ("tuple")#Картежи
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')
print (tuple)           # Prints complete tuple
print (tuple[0])        # Prints first element of the tuple
print (tuple[1:3])      # Prints elements starting from 2nd till 3rd
print (tuple[2:])       # Prints elements starting from 3rd element
print (tinytuple * 2)   # Prints tuple two times
print (tuple + tinytuple) # Prints concatenated tuple

print ("Dictionary")#Словари
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values


var = 100
if ( var  == 100 ) : print ("Value of expression is 100")


print("for while") #Циклы
list = [1,2,3,4]
it = iter(list) # this builds an iterator object
print (next(it)) #prints next available element in iterator
print (next(it)) #prints next available element in iterator
for x in it:
   print (x, end=" ")
"""
#or using next() function
while True:
   try:
      print (next(it))
   except StopIteration:
      sys.exit() #you have to import sys module for this
"""
"""
print("fibonacci Exmpl") #Циклы
def fibonacci(n): #generator function
   a, b, counter = 0, 1, 0
   while True:
      if (counter > n):
         return
      yield a
      a, b = b, a + b
      counter += 1
f = fibonacci(5) #f is iterator object

while True:
   try:
      print (next(f), end=" ")
   except StopIteration:
      sys.exit()
"""

print("String")
var1 = 'Hello World!'
print ("Updated String :- ", var1[:6] + 'Python')
print ("My name is %s and weight is %d kg!" % ('Zara', 21))


Money = 2000
def AddMoney():
   # Uncomment the following line to fix the code:
   global Money
   Money = Money + 1
print (Money)
AddMoney()
print (Money)

import math
content = dir(math)
print (content)



from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry("100x100")
def helloCallBack():
   msg = messagebox.showinfo( "Hello Python", "Hello World")
B = Button(top, text = "Hello", command = helloCallBack)
B.place(x = 50,y = 50)
top.mainloop()