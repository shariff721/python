num1 = 42             #variable declaration, initializing an integer
num2 = 2.3           # variable declatrion, initializing a float
boolean = True         # variable declatrion, initializing a boolean 
string = 'Hello World'           # variable declatrion, initalizing a string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']              # list initialising
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}            #variable declaration, initializing a dictionary
fruit = ('blueberry', 'strawberry', 'banana')             # variable declaration, initializing a tuple
print(type(fruit))                  # checkinf data type of fruit
print(pizza_toppings[1])            # accessing item at index 1 from list pizza_toppings
pizza_toppings.append('Mushrooms')         # adding item (mushrooms) to list of pizza_toppings
print(person['name'])      #accessing name of person from dictionary
person['name'] = 'George'    # updating the value of name in the dictionary
person['eye_color'] = 'blue'     # adding a  value of eyecolor to the dictionary
print(fruit[2])          # accessing value at index 2 of a tuple

if num1 > 45:
    print("It's greater")     # print if condition is met
else:
    print("It's lower")

if len(string) < 5: # conditional statment if
    print("It's a short word!")
elif len(string) > 15: # conditional statement elif
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):
    print(x)            # printins intergers from 0 to 5
for x in range(2,5):
    print(x)         # printing numbers in range from 2 to 5
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop() # remove last element from a list
pizza_toppings.pop(1) # remove element at index 1 in a list

print(person)          # log statement
person.pop('eye_color')       # deleting eye clor for the dictionary
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue                    # continue statement 
    print('After 1st if statement')
    if topping == 'Olives':
        break                        # break statement

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()       #log statement

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)       # logging hello 4 times

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')    # log statements

print_hello_x_or_ten_times()      #log statement
print_hello_x_or_ten_times(4)    #log statement


