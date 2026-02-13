#1

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")



#2

def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument



#3

def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)



#4

def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)



#5

def my_function(name):
  print("Hello", name)

my_function("Emil")