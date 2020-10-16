if_statement = {
'definition':	"Conditionally executes code.Used where code needs to be executed only if some condition is true.",
'explanation': """
It selects exactly one of the suites by evaluating the expressions one
by one until one is found to be true (see section Boolean operations
for the definition of true and false); then that suite is executed
(and no other part of the "if" statement is executed or evaluated).
If all expressions are false, the suite of the "else" clause, if
present, is executed.

""",
'Synatx':"""
if_stmt ::= "if" expression ":" suite
               ("elif" expression ":" suite)*
               ["else" ":" suite]

""",
'Example':"""
# If the number is positive, we print an appropriate message

num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")
""",
'Related Keywords':"else,elif,for,while,break_and_continue_statements_and_else_clauses_on_loops,range,python_nested_if_statements"
}

else_statement = {
'definition' : "The else is always associated with the closest preceding if (in other words, if statement_true is also an if statement, then that inner if statement must contain an else part as well)",
'Example':
"""
num = 3

# Try these two variations as well. 
# num = -5
# num = 0

if num >= 0:
    print("Positive or Zero")
else:
    print("Negative number")
""",
'Syntax':
"""
if test expression:
    Body of if
else:
    Body of else

""",
'Related Keywords':"elif,for,while,list,break_and_continue_statements_and_else_clauses_on_loops,range,if,python_nested_if_statements"		
}

elif_statement = {
'definition' : 	"""The elif is short for else if. It allows us to check for multiple expressions.
If the condition for if is False, it checks the condition of the next elif block and so on.
If all the conditions are False, the body of else is executed.
Only one block among the several if...elif...else blocks is executed according to the condition.
The if block can have only one else block. But it can have multiple elif blocks.""",
'Syntax': """
if test expression:
    Body of if
elif test expression:
    Body of elif
else: 
    Body of else
    """,
'Example':"""
num = 3.4

# Try these two variations as well:
# num = 0
# num = -4.5

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
""",
'Related Keywords': "else,for,while,list,break_and_continue_statements_and_else_clauses_on_loops,range,if,python_nested_if_statements"
}

python_nested_if_statements = {
'definition':"""
We can have a if...elif...else statement inside another if...elif...else statement. This is called nesting in computer programming.
Any number of these statements can be nested inside one another. Indentation is the only way to figure out the level of nesting. They can get confusing, so they must be avoided unless necessary.
""",
'Syntax':"""if test expression:
    			Body of if
    			if test expression:
    				Body of if
    					if test expression:
    						Body of if
    							.............
    							.............
			elif test expression:
    			Body of elif
			else: 
    			Body of else""",
'Example':"""
In this program, we input a number
check if the number is positive or
negative or zero and display
an appropriate message
This time we use nested if statement

num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
""",
'Related Keywords': "else,elif,for,while,list,break_and_continue_statements_and_else_clauses_on_loops,range,if"
}

range_function = {
'definition':"If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy. It generates arithmetic progressions:",
'explanation':
"""
1. The given end point is never part of the generated sequence; range(10) generates 10 values, the legal indices for items of a sequence of length 10. It is possible to let the range start at another number, or to specify a different increment (even negative; sometimes this is called the ‘step’):
2. To iterate over the indices of a sequence, you can combine range() and len()
""",
'Syntax':
"""
range(start,stop,step)
 
where
start: integer starting from which the sequence of integers is to be returned
stop: integer before which the sequence of integers is to be returned.
The range of integers end at stop – 1.
step: integer value which determines the increment between each integer in the sequence

""",
'Example':
"""
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4

following explanation 1
range(5, 10)
   5, 6, 7, 8, 9

range(0, 10, 3)
   0, 3, 6, 9

range(-10, -100, -30)
  -10, -40, -70

following explanation 2
>>> a = ['Mary', 'had', 'a', 'little', 'lamb']
>>> for i in range(len(a)):
...     print(i, a[i])
...
0 Mary
1 had
2 a
3 little
4 lamb
""",
'Related Keywords': "else,elif,for,while,list,if,break_and_continue_statements_and_else_clauses_on_loops,python_nested_if_statements"
}

break_and_continue_statements_and_else_clauses_on_loops = {
'explanation':
"""
1.The break statement, like in C, breaks out of the innermost enclosing for or while loop.
Loop statements may have an else clause; it is executed when the loop terminates through exhaustion of the iterable (with for) or when the condition becomes false (with while), but not when the loop is terminated by a break statement. 
2.When used with a loop, the else clause has more in common with the else clause of a try statement than it does with that of if statements: a try statement’s else clause runs when no exception occurs, and a loop’s else clause runs when no break occurs.
3. The continue statement, also borrowed from C, continues with the next iteration of the loop
""",
'Example':
"""
following explanation 1 and 2
>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(n, 'equals', x, '*', n//x)
...             break
...     else:
...         # loop fell through without finding a factor
...         print(n, 'is a prime number')
...
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3

following explanation 3 
>>> for num in range(2, 10):
...     if num % 2 == 0:
...         print("Found an even number", num)
...         continue
...     print("Found a number", num)
Found an even number 2
Found a number 3
Found an even number 4
Found a number 5
Found an even number 6
Found a number 7
Found an even number 8
Found a number 9
""",
'Related Keywords': "else,elif,for,while,list,if,range,python_nested_if_statements"
}

while_loop = {
'definition' :
"""
The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true.

We generally use this loop when we don't know the number of times to iterate beforehand.
""",
'Syntax':
"""
while test_expression:
    Body of while
""",
'explanation':
"""
n the while loop, test expression is checked first. The body of the loop is entered only if the test_expression evaluates to True. After one iteration, the test expression is checked again. This process continues until the test_expression evaluates to False.
Python interprets any non-zero value as True. None and 0 are interpreted as False.
""",
'Example': 
"""
n = 10

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)
the sum is 55
""",
'While loop with else':
"""
Same as with for loops, while loops can also have an optional else block.
The else part is executed if the condition in the while loop evaluates to False.
The while loop can be terminated with a break statement. In such cases, the else part is ignored. Hence, a while loop's else part runs if no break occurs and the condition is false.

Example
counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")

Inside loop
Inside loop
Inside loop
Inside else
""",
'Related Keywords': "else,elif,for,while,list,,if,break_and_continue_statements_and_else_clauses_on_loops,python_nested_if_statements"
}

for_loop = {
'definition':"The for statement is used to iterate over the elements of a sequence (such as a string, tuple or list) or other iterable object",
'Syntax':
"""
for_stmt ::=  "for" target_list "in" expression_list ":" suite
              ["else" ":" suite]
""",
'Related Keywords': "else,elif,for,while,list,if,break_and_continue_statements_and_else_clauses_on_loops",
'Example':
"""
# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
	sum = sum+val

print("The sum is", sum)

The sum is 48
"""
}

list_doc = {
'definition':"List is a collection which is ordered and changeable. Allows duplicate members List literals are written within square brackets [ ]. Lists work similarly to strings -- use the len() function and square brackets [ ] to access data, with the first element at index 0.",
'Syntax':"list_name = [list element 1,list element 2,................,,list element n]",
'Related Keywords': "else,elif,for,while,if,break_and_continue_statements_and_else_clauses_on_loops,python_nested_if_statements",
'Example':
"""
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.count('tangerine')
0
>>> fruits.index('banana')
3
>>> fruits.index('banana', 4)  # Find next banana starting a position 4
6
>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'
""",
'List Comprehensions':
"""
List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.
Example:
squares = [x**2 for x in range(10)]
squares = [0,1,4,9,16,25,36,49,64,81]

>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
"""

}


return_statement = {
    'definition':"""A return statement is used to end the execution of the function call and “returns” the result (value of the expression following the return keyword) to the caller. 
    The statements after the return statements are not executed. If the return statement is without any expression, then the special value None is returned.

    Note: Return statement can not be used outside the function.
    """,
    'Syntax':"""
    def fun():
    statements
    .
    .
    return [expression]
    """,
    'Examples':
    """
    # Python program to  
    # demonstrate return statement  
      
    def add(a, b): 
      
        # returning sum of a and b 
        return a + b 
      
    def is_true(a): 
      
        # returning boolean of a 
        return bool(a) 
      
    # calling function 
    res = add(2, 3) 
    print("Result of add function is {}".format(res)) 
      
    res = is_true(2<5) 
    print("\nResult of is_true function is {}".format(res)) 
    """
}

operator_entity = {
  'definition' : """An operator is a symbol that tells the compiler to perform specific mathematical or logical functions.
           Python language is rich in built-in operators and provides the following types of operators :
            a) Arithmetic Operators
            b) Comparison (Relational) Operators
            c) Logical Operators
            d) Assignment Operators
            e) Bitwise Operators
            f) Membership Operators
            g) Identity Operators
           \nWe will describe in brief the first three category of operators that is used most frequently. For other operators you could refer to python's standard documentation.""",
  'Arithmetic operators' : """ Assume variable a holds 10 and variable b holds 20, for the examples used below.\n
+ Addition : Adds values on either side of the operator. Eg : a + b = 30\n
- Subtraction : Subtracts right hand operand from left hand operand. Eg : a – b = -10\n
* Multiplication : Multiplies values on either side of the operator. Eg : a * b = 200\n
/ Division : Divides left hand operand by right hand operand. Eg : b / a = 2\n
% Modulus : Divides left hand operand by right hand operand and returns remainder. Eg : b % a = 0\n
** Exponent : Performs exponential (power) calculation on operators. Eg : a**b =10 to the power 20\n
//  Floor Division : The division of operands where the result is the quotient in which the digits after the decimal point are removed. 
                    But if one of the operands is negative, the result is floored, i.e., rounded away from zero (towards negative infinity).
                    Some of the examples are : 9//2 = 4 and 9.0//2.0 = 4.0, -11//3 = -4, -11.0//3 = -4.0\n
""",
  'Comparison (Relational) operators' : """These operators compare the values on either sides of them and decide the relation among them. They are also called Relational operators.
  Assume variable a holds 10 and variable b holds 20, for the examples used below.\n
==  ,If the values of two operands are equal, then the condition becomes true. Eg : (a == b) is not true.\n
!=  ,If values of two operands are not equal, then condition becomes true. Eg : (a != b) is true.\n
<>  ,If values of two operands are not equal, then condition becomes true. Eg : (a <> b) is true. This is similar to != operator.\n
>   ,If the value of left operand is greater than the value of right operand, then condition becomes true. Eg :(a > b) is not true.\n
<   ,If the value of left operand is less than the value of right operand, then condition becomes true. Eg : (a < b) is true.\n
>=  ,If the value of left operand is greater than or equal to the value of right operand, then condition becomes true. Eg : (a >= b) is not true.\n
<=  ,If the value of left operand is less than or equal to the value of right operand, then condition becomes true. Eg : (a <= b) is true.\n
""",
  'Logical operators' : """Assume variable A holds 1(True) and B holds 0(False).\n
(and) Called Logical AND operator. If both the operands are non-zero, then the condition becomes true. Eg : (A and B) is false.\n
(or) Called Logical OR Operator. If any of the two operands is non-zero, then the condition becomes true. Eg : (A or B) is true.\n
(not) Called Logical NOT Operator. It is used to reverse the logical state of its operand. If a condition is true, then Logical NOT operator will make it false. Eg : not(A and B) is true.\n
"""
}

local_variable = {
    'contents':"""
    A variable declared inside the function's body or in the local scope is known as a local variable.

    Example:
    def foo():
    y = "local"


    foo()
    print(y)

    output : NameError: name 'y' is not defined
    The output shows an error because we are trying to access a local variable y in a global scope whereas the local variable only works inside foo() or local scope.
    """
}

global_variable = {
    'contents':"""
    In Python, a variable declared outside of the function or in global scope is known as a global variable. This means that a global variable can be accessed inside or outside of the function.
   
    Example:
    x = "global"

    def foo():
        print("x inside:", x)


    foo()
    print("x outside:", x)

    output :
    x inside: global
    x outside: global
    """
}

nonlocal_variables = {
'contents':"""

Nonlocal variables are used in nested functions whose local scope is not defined. This means that the variable can be neither in the local nor the global scope.

We use nonlocal keyword to create nonlocal variables.

Example:
def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()

output:
inner: nonlocal
outer: nonlocal

In the above code, there is a nested inner() function. We use nonlocal keywords to create a nonlocal variable. The inner() function is defined in the scope of another function outer().
"""
}

