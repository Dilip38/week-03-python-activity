def function_name(arguments):
    # function body 

    return
    def greet():
    print('Hello World!')

# call the function
greet()

print('Outside function')
# function with two arguments
def add_numbers(num1, num2):
    sum = num1 + num2
    print('Sum: ',sum)

# function with no argument
def add_numbers():
    # code
    # function with two arguments
def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ",sum)

# function call with two values
add_numbers(5, 4)

# Output: Sum: 9
#filter function in python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# returns True if number is even
def check_even(number):
    if number % 2 == 0:
          return True  

    return False

# Extract elements from the numbers list for which check_even() returns True
even_numbers_iterator = filter(check_even, numbers)

# converting to list
even_numbers = list(even_numbers_iterator)

print(even_numbers)

# Output: [2, 4, 6, 8, 10]

# returns True if number is even
def check_even(number):
    if number % 2 == 0:
          return True  

    return False

# Extract elements from the numbers list for which check_even() returns True
even_numbers_iterator = filter(check_even, numbers)

# converting to list
even_numbers = list(even_numbers_iterator)

print(even_numbers)

# Output: [2, 4, 6, 8, 10]
# dictionary with keys and values of different data types
numbers = {1: "One", 2: "Two", 3: "Three"}
print(numbers)
capital_city = {"Nepal": "Kathmandu", "England": "London"}
print("Initial Dictionary: ",capital_city)

capital_city["Japan"] = "Tokyo"

print("Updated Dictionary: ",capital_city)
h_letters = []

for letter in 'human':
    h_letters.append(letter)

print(h_letters)
h_letters = [ letter for letter in 'human' ]
print( h_letters)
class Parrot:

    # class attribute
    name = ""
    age = 0

# create parrot1 object
parrot1 = Parrot()
parrot1.name = "Blu"
parrot1.age = 10

# create another object parrot2
parrot2 = Parrot()
parrot2.name = "Woo"
parrot2.age = 15
# base class
class Animal:
    
    def eat(self):
        print( "I can eat!")
    
    def sleep(self):
        print("I can sleep!")

# derived class
class Dog(Animal):
    
    def bark(self):
        print("I can bark! Woof woof!!")

# Create object of the Dog class
dog1 = Dog()

# Calling members of the base class
dog1.eat()
dog1.sleep()

# Calling member of the derived class
dog1.bark();


# access attributes
print(f"{parrot1.name} is {parrot1.age} years old")
print(f"{parrot2.name} is {parrot2.age} years old")
class Animal:

    # attribute and method of the parent class
    name = ""
    
    def eat(self):
        print("I can eat")

# inherit from Animal
class Dog(Animal):

    # new method in subclass
    def display(self):
        # access name attribute of superclass using self
        print("My name is ", self.name)

# create an object of the subclass
labrador = Dog()

# access superclass attribute and method 
labrador.name = "Rohu"
labrador.eat()

# call subclass method 
labrador.display()
#list vs generator
>>> my_list = []
>>> for x in range(10):
... my_list.append(x * 2)
...
>>> print(my_list)
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
>>> comp_list = [x * 2 for x in range(10)]
>>> print(comp_list)
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
#map function in python
numbers = [2, 4, 6, 8, 10]

# returns square of a number
def square(number):
  return number * number

# apply square() function to each item of the numbers list
squared_numbers_iterator = map(square, numbers)

# converting to list
squared_numbers = list(squared_numbers_iterator)
print(squared_numbers)

# Output: [4, 16, 36, 64, 100]

#arithmatic operator
print(2>4)
print(3==3)
print(3==4)
#set {},    (set does not allow index)(allow loop,for loop)
marks= {98, 96, 97, 97, 97}
print(marks)

for score in marks:
    print(score)print("Hello World")
print("Hello Coders")
print("i know how to count...1,2,3,4 ")
print("Hello")
#variable
name="shraddha"
age=22
print(name)
print(age)
name="aman"
age=25
print(name)
print(age)
number=18
print(number)
number=18.5
print(int(number))
number=25
print(float(number))
name="aman"
age=25
is_adult=True
age=16
is_adult=False
input
name=input("whst is your name")
print(name)
age=input("what is your age")
print(age)
Tonprint sum of two number
first=input("enter your first number")
second=input("enter your second number")
sum=int(first)+int(second)
print(sum)
strings capital, small, index(position), find, replace 
a="Tony stark"
print(a.upper())
print(a.lower())
print("T" in a)
print("S" in a)
print(a.find("s"))
print(a.find("n"))
print(a.find("T"))
print(a.replace("T","M"))
print(a.replace("Tony stark","Ironman"))
print(a.replace("stark","hello"))
#arithmatic  operator
print(2+3)
print(5-2)
print(5*3)
print(5/2)
print(5//2)
print(5**2)
print(5%2)
#operator precidense
print(15/5*2+5-1)
print(6/2+5*2)
print((2+5)*4/2)
#logical operator (or, and, not)
print(3>2 or 1>3)
print(2>4 or 3>5)
print(5>4 and 6>4)
print(3>2 and 2>5)
print(not 3>2)
print(not 2>3)
#comparison operator
print(3>2)
#touple(), 
marks=  (94, 98, 97, 97, 97)
#operation on touple
print(marks.count(97))
print(marks.index(97))

