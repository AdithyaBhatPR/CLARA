if_statement = {
'definition': "Conditionally executes code.Used where code needs to be executed only if some condition is true.",

'Syntax':
"""
if ( expression ) statement_true  (1) 
if ( expression ) statement_true else statement_false (2) 
""",
'Explanation':
"""
expression must be an expression of any scalar type.

If expression compares not equal to the integer zero, statement_true is executed.

In the form (2), if expression compares equal to the integer zero, statement_false is executed.

As with all other selection and iteration statements, the entire if-statement has its own block scope:
""",
'Related Keywords':
"if, else,conditional_statement,ift_explanation",
'Example':
"""
#include <stdio.h>
 
int main(void)
{
    int i = 2;
    if (i > 2) {
        printf("first is true\n");
    } else {
        printf("first is false\n");
    }
 
    i = 3;
    if (i == 3) printf("i == 3\n");
 
    if (i != 3) printf("i != 3 is true\n");
    else        printf("i != 3 is false\n");
}
Output:

first is false
i == 3
i != 3 is false
"""
}

else_statement = {'definition':"""The else is always associated with the closest preceding if (in other words, if statement_true is also an if statement, then that inner if statement must contain an else part as well)""",
'Syntax':"if ( expression ) statement_true else statement_false",
'Example':
"""
int j = 1;
if (i > 1)
   if(j > 2)
       printf("%d > 1 and %d > 2\n", i, j);
    else // this else is part of if(j>2), not part of if(i>1) 
       printf("%d > 1 and %d <= 2\n", i, j);
If statement_true is entered through a goto, statement_false is not executed.
""",
'Related Keywords':
"if, else,conditional_statement,ift_explanation"
}

# print(if_statement.keys())
# print(else_statement.keys())
array_doc = {
'definition':"Array is a type consisting of a contiguously allocated nonempty sequence of objects with a particular element type. The number of those objects (the array size) never changes during the array lifetime.",
'Syntax':"""
In the declaration grammar of an array declaration, the type-specifier sequence designates the element type (which must be a complete object type), and the declarator has the form:

[ static(optional) qualifiers(optional) expression(optional) ]  (1) 
[ qualifiers(optional) static(optional) expression(optional) ]  (2) 
[ qualifiers(optional) * ]  (3) 
1,2) General array declarator syntax
3) Declarator for VLA of unspecified size (can appear in function prototype scope only) where
expression  - any expression other than comma operator, designates the number of elements in the array
qualifiers  - any combination of const, restrict, or volatile qualifiers, only allowed in function parameter lists; this qualifies the pointer type to which this array parameter is transformed
float fa[11], *afp[17]; // fa is an array of 11 floats
                        // afp is an array of 17 pointers to floats
                        """,
'Assignment':
"""
Objects of array type are not modifiable lvalues, and although their address may be taken, they cannot appear on the left hand side of an assignment operator. However, structs with array members are modifiable lvalues and can be assigned:

int a[3] = {1,2,3}, b[3] = {4,5,6};
int (*p)[3] = &a; // okay, address of a can be taken
// a = b;            // error, a is an array
struct { int c[3]; } s1, s2 = {3,4,5};
s1 = s2; // okay: can assign structs holding array members
""",
'Multidimensional arrays':
"""
When the element type of an array is another array, it is said that the array is multidimensional:

// array of 2 arrays of 3 ints each
int a[2][3] = {{1,2,3},  // can be viewed as a 2x3 matrix
               {4,5,6}}; // with row-major layout
Note that when array-to-pointer conversion is applied, a multidimensional array is converted to a pointer to its first element, e.g., pointer to the first row:

int a[2][3]; // 2x3 matrix
int (*p1)[3] = a; // pointer to the first 3-element row
int b[3][3][3]; // 3x3x3 cube
int (*p2)[3][3] = b; // pointer to the first 3x3 plane
Multidimensional arrays may be variably modified in every dimension:

int n = 10;
int a[n][2*n];
""",
'Array initialization':
"""
When initializing an object of array type, the initializer must be either a string literal (optionally enclosed in braces) or be a brace-enclosed list of initialized for array members:

= string_literal  (1) 
= { expression , ... }
= { designator(optional) expression , ... }

(2) (until C99)
(since C99)
1) string literal initializer for character and wide character arrays
2) comma-separated list of constant (until C99) expressions that are initializers for array elements, optionally using array designators of the form [ constant-expression ] = (since C99)
Arrays of known size and arrays of unknown size may be initialized, but not VLAs. (since C99).

All array elements that are not initialized explicitly are initialized implicitly the same way as objects that have static storage duration.
""",
'Initialization from strings':
"""
string literal (optionally enclosed in braces) may be used as the initializer for an array of matching type:

Successive bytes of the string literal or wide characters of the wide string literal, including the terminating null byte/character, initialize the elements of the array:

char str[] = "abc"; // str has type char[4] and holds 'a', 'b'. 'c', '\0'

If the size of the array is known, it may be one less than the size of the string literal, in which case the terminating null character is ignored:

char str[3] = "abc"; // str has type char[3] and holds 'a', 'b', 'c'
Note that the contents of such array are modifiable, unlike when accessing a string literal directly with char* str = "abc";.
""",
'Initialization from brace-enclosed lists':
"""
When an array is initialized with a brace-enclosed list of initializers, the first initializer in the list initializes the array element at index zero (unless a designator is specified) (since C99), and each subsequent initializer without a designator (since C99)initializes the array element at index one greater than the one initialized by the previous initializer.

int x[] = {1,2,3}; // x has type int[3] and holds 1,2,3
int y[5] = {1,2,3}; // y has type int[5] and holds 1,2,3,0,0
int z[3] = {0}; // z has type int[3] and holds all zeroes

It's an error to provide more initializers than elements when initializing an array of known size (except when initializing character arrays from string literals).
""",
'Nested arrays':
"""
f the elements of an array are arrays, structs, or unions, the corresponding initializers in the brace-enclosed list of initializers are any initializers that are valid for those members, except that their braces may be omitted as follows:

If the nested initializer begins with an opening brace, the entire nested initializer up to its closing brace initializes the corresponding array element:

int y[4][3] = { // array of 4 arrays of 3 ints each (4x3 matrix)
    { 1 },      // row 0 initialized to {1, 0, 0}
    { 0, 1 },   // row 1 initialized to {0, 1, 0}
    { [2]=1 },  // row 2 initialized to {0, 0, 1}
};  

If the nested initializer does not begin with an opening brace, only enough initializers from the list are taken to account for the elements or members of the sub-array, struct or union; any remaining initializers are left to initialize the next array element:

int y[4][3] = {    // array of 4 arrays of 3 ints each (4x3 matrix)
1, 3, 5, 2, 4, 6, 3, 5, 7 // row 0 initialized to {1, 3, 5}
};                        // row 1 initialized to {2, 4, 6}
                          // row 2 initialized to {3, 5, 7}
                          // row 3 initialized to {0, 0, 0}
 
struct { int a[3], b; } w[] = { { 1 }, 2 }; // array of structs
   // { 1 } is taken to be a fully-braced initializer for element #0 of the array
   // that element is initialized to { {1, 0, 0}, 0}
   // 2 is taken to be the first initialized for element #1 of the array
   // that element is initialized { {2, 0, 0}, 0}
""",
'Related Keywords':"if, else,conditional_statement,ift_explanation,while,break_and_continue,for"

}

for_loop = {
'definition':"Executes a statement repeatedly, until the value of expression becomes equal to zero. The test takes place before each iteration.",
'Syntax':"""
for (initializationStatement; testExpression; updateStatement)
{
    // statements inside the body of loop
}
""",
'Explanation':"""
The initialization statement is executed only once.
Then, the test expression is evaluated. If the test expression is evaluated to false, the for loop is terminated.
However, if the test expression is evaluated to true, statements inside the body of for loop are executed, and the update expression is updated.
Again the test expression is evaluated.If the execution of the loop needs to be terminated at some point, a break statement can be used anywhere within the loop_statement.
The continue statement used anywhere within the loop_statement transfers control to iteration_expression.As with all other selection and iteration statements, the for statement establishes block scope: any identifier introduced in the init_clause, cond_expression, or iteration_expression goes out of scope after the loop_statement.
""",
'Example':
"""
// Program to calculate the sum of first n natural numbers
// Positive integers 1,2,3...n are known as natural numbers

#include <stdio.h>
int main()
{
    int num, count, sum = 0;

    printf("Enter a positive integer: ");
    scanf("%d", &num);

    // for loop terminates when num is less than count
    for(count = 1; count <= num; ++count)
    {
        sum += count;
    }

    printf("Sum = %d", sum);

    return 0;
}

Enter a positive integer: 10
Sum = 55
""",
'Related Keywords':"if, else,conditional_statement,ift_explanation,while,break_and_continue"
}

while_loop = {
'definition':"Executes a statement repeatedly, until the value of expression becomes equal to zero. The test takes place before each iteration.",
'Syntax':"""
while (testExpression) 
{
    // statements inside the body of the loop 
}""",
'Explanation':"""The while loop evaluates the test expression inside the parenthesis ().
If the test expression is true, statements inside the body of while loop are executed. Then, the test expression is evaluated again.
The process goes on until the test expression is evaluated to false.
If the test expression is false, the loop terminates (ends).f the execution of the loop needs to be terminated at some point, break statement can be used as a terminating statement.
If the execution of the loop needs to be continued at the end of the loop body, continue statement can be used as a shortcut.As with all other selection and iteration statements, the while statement establishes block scope: any identifier introduced in the expression goes out of scope after the statement.
""",
'Example':
"""// Print numbers from 1 to 5

#include <stdio.h>
int main()
{
    int i = 1;
    
    while (i <= 5)
    {
        printf("%d\n", i);
        ++i;
    }

    return 0;
}

1
2
3
4
5
""",
'do_while_explanation':"""
The do..while loop is similar to the while loop with one important difference. The body of do...while loop is executed at least once. Only then, the test expression is evaluated.
""",
'do_while_Syntax':"""
do
{
   // statements inside the body of the loop
}
while (testExpression);
""",
'do_while_example':
"""
// Program to add numbers until the user enters zero

#include <stdio.h>
int main()
{
    double number, sum = 0;

    // the body of the loop is executed at least once
    do
    {
        printf("Enter a number: ");
        scanf("%lf", &number);
        sum += number;
    }
    while(number != 0.0);

    printf("Sum = %.2lf",sum);

    return 0;
}
""",
'Related Keywords':"if, else,conditional_statement,ift_explanation,for,break_and_continue"
}

break_and_continue = {
'definition of break':"""
Causes the enclosing for, while or do-while loop or switch statement to terminate.
Used when it is otherwise awkward to terminate the loop using the condition expression and conditional statements.
Appears only within the statement of a loop body (while, do, for) or within the statement of a switch.After this statement the control is transferred to the statement or declaration immediately following the enclosing loop or switch.
""",
'Syntax for break':"break;",
'Example for break':
"""
// Program to calculate the sum of a maximum of 10 numbers
// If a negative number is entered, the loop terminates

# include <stdio.h>
int main()
{
    int i;
    double number, sum = 0.0;

    for(i=1; i <= 10; ++i)
    {
        printf("Enter a n%d: ",i);
        scanf("%lf",&number);

        // If the user enters a negative number, the loop ends
        if(number < 0.0)
        {
            break;
        }

        sum += number; // sum = sum + number;
    }

    printf("Sum = %.2lf",sum);
    
    return 0;
}


Enter a n1: 2.4
Enter a n2: 4.5
Enter a n3: 3.4
Enter a n4: -3
Sum = 10.30
""",
'definition of continue':"""The continue statement skips the current iteration of the loop and continues with the next iteration.Causes the remaining portion of the enclosing for, while or do-while loop body to be skipped.
Used when it is otherwise awkward to ignore the remaining portion of the loop using conditional statements.
""",
'Syntax of continue':"continue;",
'Example for continue':"""
// Program to calculate the sum of a maximum of 10 numbers
// Negative numbers are skipped from the calculation

# include <stdio.h>
int main()
{
    int i;
    double number, sum = 0.0;

    for(i=1; i <= 10; ++i)
    {
        printf("Enter a n%d: ",i);
        scanf("%lf",&number);

        if(number < 0.0)
        {
            continue;
        }

        sum += number; // sum = sum + number;
    }

    printf("Sum = %.2lf",sum);
    
    return 0;
}

Enter a n1: 1.1
Enter a n2: 2.2
Enter a n3: 5.5
Enter a n4: 4.4
Enter a n5: -3.4
Enter a n6: -45.5
Enter a n7: 34.5
Enter a n8: -4.2
Enter a n9: -1000
Enter a n10: 12
Sum = 59.70
""",
'Related Keywords':"if, else,conditional_statement,ift_explanation,for,while"
}

return_statement = {
'definition':"""A return statement ends the execution of a function, and returns control to the calling function. 
Execution resumes in the calling function at the point immediately following the call. 
A return statement can return a value to the calling function.
""",
'Syntax for return':"""return expression(optional, based on the return type specified in function prototype);""",
'Examples for return':"""
  Eg: 1)
    double ratio( int numerator, int denominator )
  {
    // Cast one operand to double to force floating-point
    // division. Otherwise, integer division is used,
    // then the result is converted to the return type.
    return numerator / (double) denominator;
  }

  Eg: 2)
  void report_square( void )
  {
    int value = INT_MAX;
    long long squared = 0LL;
    squared = square( value );
    printf( "value = %d, squared = %lld\n", value, squared );
    return; // Use an empty expression to return void.
  }

  Eg: 3)
  void report_ratio( int top, int bottom )
  {
    double fraction = ratio( top, bottom );
    printf( "%d / %d = %.16f\n", top, bottom, fraction );
    // It's okay to have no return statement for functions
    // that have void return types.
  }
  """
}

operator_entity = {
  'definition' : """An operator is a symbol that tells the compiler to perform specific mathematical or logical functions.
           C language is rich in built-in operators and provides the following types of operators :
           a) Arithmetic operators
           b) Relational Operators
           c) Logical Operators
           d) Bitwise Operators
           e) Assignment Operators
           f) Misc Operators
           \nWe will describe in brief the first three category of operators that is used most frequently. """,
  'Arithmetic operators' : """ Assume variable A holds 10 and variable B holds 20, for the examples used below.\n
(+)Adds two operands. Eg: A + B = 30\n
(−)Subtracts second operand from the first. Eg: A − B = -10\n
(*)Multiplies both operands. Eg: A * B = 200\n
(/)Divides numerator by de-numerator.Eg: B / A = 2\n
(%)Modulus Operator and remainder of after an integer division.Eg: B % A = 0\n
(++)Increment operator increases the integer value by one.Eg:  A++ = 11\n
(--)Decrement operator decreases the integer value by one.Eg: A-- = 9\n
""",
  'Relational operators' : """Assume variable A holds 10 and variable B holds 20, for the examples used below.\n
(==) Checks if the values of two operands are equal or not. If yes, then the condition becomes true. Eg : (A == B) is not true\n
(!=) Checks if the values of two operands are equal or not. If the values are not equal, then the condition becomes true. Eg : (A != B) is true\n
(>) Checks if the value of left operand is greater than the value of right operand. If yes, then the condition becomes true. Eg : (A > B) is not true\n
(<) Checks if the value of left operand is less than the value of right operand. If yes, then the condition becomes true. Eg : (A < B) is true\n
(>=) Checks if the value of left operand is greater than or equal to the value of right operand. If yes, then the condition becomes true. Eg : (A >= B) is not true\n
(<=) Checks if the value of left operand is less than or equal to the value of right operand. If yes, then the condition becomes true. Eg : (A <= B) is true\n
""",
  'Logical operators' : """Assume variable A holds 1(True) and B holds 0(False).\n
(&&) Called Logical AND operator. If both the operands are non-zero, then the condition becomes true. Eg : (A && B) is false.\n
(||) Called Logical OR Operator. If any of the two operands is non-zero, then the condition becomes true. Eg : (A || B) is true.\n
(!) Called Logical NOT Operator. It is used to reverse the logical state of its operand. If a condition is true, then Logical NOT operator will make it false. Eg : !(A && B) is true.\n
"""
}

local_variable = {
  'definition':"""A variable that is declared and used inside the function or block is called local variable.
It’s scope is limited to function or block.It cannot be used outside the block.Local variables need
to be initialized before use.""",
'Example':"""
#include <stdio.h>
void function() {
int x = 10; // local variable
}

int main()
{
function();
}
In the above code x can be used only in the scope of function() . Using it in main function will give error.
"""
}

global_variable = {
  'definition':"A variable that is declared outside the function or block is called a global variable. It is declared at the starting of program. It is available to all the functions.",
  'Example':"""
  #include <stdio.h>
int x = 20;//global variable
void function1()
{
printf("%d\n" , x);
}
void function2()
{
printf("%d\n" , x);
}
int main() {

function1();
function2();
  return 0;
}

output
20
20
"""
}

static_variable = {
  'definition':"""A variable that retains its value between multiple function calls is known as static variable.
It is declared with the static keyword.""",
'Example':"""
#include <stdio.h>
void function(){
int x = 20;//local variable
static int y = 30;//static variable
x = x + 10;
y = y + 10;
printf("\n%d,%d",x,y);
}
int main() {

function();
function();
function();
return 0;
}

output:
30,40
30,50
30,60
In the above example , local variable will always print same value whenever function will be called whereas static variable will print the incremented value in each function call.
"""

}

automatic_variable = {
  'definition':"""
  All variables in C that are declared inside the block, are automatic variables by default. We
can explicitly declare an automatic variable using auto keyword.Automatic variables are similar as
local variables.
""",
'Example':
"""
#include <stdio.h>
void function()
{
int x=10;//local variable (also automatic)
auto int y=20;//automatic variable
}
int main() {

  function();
  return 0;
}

In the above example both x and y are automatic variables .The only difference is that variable y is explicitly declared with auto keyword.
"""
}

external_variable = {
  'definition':"""External variable can be shared between multiple C files.We can declare external variable using
extern keyword.""",
'Example':
"""
 myfile.h

  extern int x=10;//external variable (also global)  

   
  program1.c
  #include "myfile.h"  
  #include <stdio.h>  
  void printValue(){  
  printf("Global variable: %d", global_variable);  
  }  

In the above example x is an external variable which is used in multiple files.
  """
}
