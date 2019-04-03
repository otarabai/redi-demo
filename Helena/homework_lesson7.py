'''
Question 1:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
Hints:
Consider use range(#begin, #end) method
'''

var_5_7 = ''
for numero in range(2000, 3201):
    if (numero % 7 == 0 and numero % 5 != 0):
        var_5_7 += (str(numero) + ', ')
print(var_5_7)


list_of_multiples = []
for numero in range(2000, 3200):
    if (numero % 7 == 0 and numero % 5 != 0):
        list_of_multiples.append(numero)
print(list_of_multiples)



'''
Question 2:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input. 
Consider use dict()
'''

print('Please enter a positive integer not greater than 10: ')
our_n = int(input())

dict_of_squares = {}

for i in range(1, our_n + 1):
    dict_of_squares[i] = i * i
print(dict_of_squares)



'''
Question 3:
Ask the user for a number and determine whether the number is prime or not.
Create a function is_prime() that takes an integer and returns a boolean.
'''


# abandoned attempt
print('Please enter an integer greater than 1: ')
user_number = int(input())

def is_prime():
    for i in range(2, user_number):

        if user_number == 2:
            print('The number you chose is a prime.')
        elif user_number % i == 0:
            print('The number you chose is not a prime.')

        else:
            print('The number you chose is a prime.')

is_prime()
'''

print('Please enter an integer greater than 1: ')
i = int(input())

def is_prime(i):
    if i == 2:
        print(True)
    if i == 3:
        print(True)
    if i % 2 == 0:
        print(False)
    if i % 3 == 0:
        print(False)

    n = 5
    w = 2

    while n * n <= i:
        if i % n == 0:
            print(False)

        n += w
        w = 6 - w

    print(True)

is_prime(i)

'''

'''
Question 4:
Draw a chess board. Chess boards have a size of 8x8 and look like this:




 --- --- --- --- --- --- --- ---
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |
 --- --- --- --- --- --- --- ---
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |
 --- --- --- --- --- --- --- ---
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |
 --- --- --- --- --- --- --- ---
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |
 --- --- --- --- --- --- --- ---
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |
 --- --- --- --- --- --- --- ---
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |
 --- --- --- --- --- --- --- ---
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |
 --- --- --- --- --- --- --- ---
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |
 --- --- --- --- --- --- --- ---
'''

'''

var1 = ' ---'
var2 = '|   '
for i in range(0, 8):
    print(var1 * 8)
    print(var2 * 9)
    print(var2 * 9)
print(var1 * 8)

'''






