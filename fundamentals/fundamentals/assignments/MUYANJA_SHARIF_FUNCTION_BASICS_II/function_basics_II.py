
#1  countdown

def count_down(x):
    for i in range (x,-1,-1):
        print(i)

count_down(5)


#2 print and return

def print_and_return(x,y):
    print(x)
    return y

print_and_return(2,3)


#3 first plus length

def first_plus_length(x):
    for i in range (len(x)):
        return x[0] + x[len(x)-1]
    
sum = first_plus_length([1,2,3,4,5])
print(sum)
    


#4 values greater than second
new_list = []
def greater_than_second(x):
    if len(x) > 1:
        for i in range (len(x)):
            if x[i] > 2:
                new_list.append(x[i])
    else:
        return False
    
    return new_list

r = greater_than_second([5,2,3,2,1,4])
print(r)

r = greater_than_second([3])
print(r)

#5 this length, that value

new_list = []

def this_length_that_value(x,y):
    for i in range (x):
        new_list.append(y)
    
    return new_list

y = this_length_that_value(6,2)
print(y)





