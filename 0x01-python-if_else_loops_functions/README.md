# Python - if/else, loops, functions

## Description
> This repository contains scripts that are created as part of the learning objectives of programming at ALX SE programme. The emphasis is on enforcing problem solving skills through programming and other technologies. This repository contains `.c` and `.py` files created for a deeper understanding of higher level programming in Python.

## Learning Objectives
* Why Python programming is awesome
* Why indentation is so important in Python
* How to use the `if`, `if ... else` statements
* How to use comments
* How to affect values to variables
* How to use the `while` and `for` loops
* How is Python’s `for` different from `C`‘s?
* How to use the `break` and `continues` statements
* How to use `else` clauses on loops
* What does the `pass` statement do, and when to use it
* How to use `range`
* What is a function and how do you use functions
* What does return a function that does not use any `return` statement
* Scope of variables
* What’s a traceback
* What are the arithmetic operators and how to use them

## Requirements

### General
- Allowed editors: `vi`, `vim`, or `emacs`
- All files should end with a new line

### Python Language
- Style Guide: [Pycodestyle](https://intranet.alxswe.com/rltoken/UQ25jC6sA5XqZl6ZZIdAaw)
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- The first line of every file should be exactly `#!/usr/bin/python3`
- All files must be executables.
- The length of all files will be tested using `wc`

### C Language
- Operating system: `Ubuntu 20.04 LTS`
- Style Guide: [Betty Style](https://github.com/alx-tools/Betty/tree/master)
- Compilation should be achieved using `gcc`, using the options `-Wall -Werror -Wextra -pedantic -std=gnu89`
- No more than 5 functions per file.
- The use of global variables is not allowed.
- All header files should be include guarded.
- The prototypes of all your functions and the prototype of the function should be included in your header file called `lists.h`

---
## Scripts
0. **0-positive_or_negative.py** - This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print whether the number stored in the variable `number` is positive or negative.
    * You can find the source code [here](https://intranet.alxswe.com/rltoken/e4tR3cjFHqhelf4y485-zQ)
    * The variable `number` will store a different value every time you will run this program
    * You don’t have to understand what `import`, `random`. `randint` do. Please do not touch this code
    * The output of the program should be:
        * The number, followed by
            * if the number is greater than 0: `is positive`
            * if the number is 0: `is zero`
            * if the number is less than 0: `is negative`
        * followed by a new line
<br>

1. **1-last_digit.py** - This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable `number`.
    * You can find the source code [here](https://intranet.alxswe.com/rltoken/Vku0ZPFeDPuXUKD8nZ4mOQ)
    * The variable `number` will store a different value every time you will run this program
    * You don’t have to understand what `import`, `random`. `randint` do. **Please do not touch this code**. This line should not change: `number = random.randint(-10000, 10000)`
    * The output of the program should be:
        * The string `Last digit of`, followed by
        * the number, followed by
        * the `string is`, followed by the last digit of `number`, followed by
            * if the last digit is greater than 5: the string `and is greater than 5`
            * if the last digit is 0: the string `and is 0`
            * if the last digit is less than 6 and not 0: the string `and is less than 6 and not 0`
        * followed by a new line
<br>


2. **2-print_alphabet.py** - Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
    * You can only use one `print` function with string format
    * You can only use one loop in your code
    * You are not allowed to store characters in a variable
    * You are not allowed to import any module
<br>

3. **3-print_alphabt.py** - Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
    * Print all the letters except `q` and `e`
    * You can only use one `print` function with string format
    * You can only use one loop in your code
    * You are not allowed to store characters in a variable
    * You are not allowed to import any module
<br>

4. **4-print_hexa.py** - Write a program that prints all numbers from `0` to `98` in decimal and in hexadecimal.
    * You can only use one `print` function with string format
    * You can only use one loop in your code
    * You are not allowed to store numbers or strings in a variable
    * You are not allowed to import any module
<br>

5. **5-print_comb2.py** - Write a program that prints numbers from `0` to `99`.
    * Numbers must be separated by `,`, followed by a space
    * Numbers should be printed in ascending order, with two digits
    * The last number should be followed by a new line
    * You can only use no more than 2 `print` functions with string format
    * You can only use one loop in your code
    * You are not allowed to store numbers or strings in a variable
    * You are not allowed to import any module
<br>

6. **6-print_comb3.py** - Write a program that prints all possible different combinations of two digits.
    * Numbers must be separated by `,`, followed by a space
    * The two digits must be different.
    * `01` and `10` are considered the same combination of the two digits `0` and `1`
    * Print only the smallest combination of two digits
    * Numbers should be printed in ascending order, with two digits
    * The last number should be followed by a new line
    * You can only use no more than 3 `print` functions with string format
    * You can only use no more than 2 loops in your code
    * You are not allowed to store numbers or strings in a variable
    * You are not allowed to import any module
<br>

7. **7-islower.py** - Write a function that checks for lowercase character.
    * Prototype: `def islower(c):`
    * Returns `True` if `c` is lowercase
    * Returns `False` otherwise
    * You are not allowed to import any module
    * You are not allowed to use `str.upper()` and `str.isupper()`
    * [Tips:ord()](https://intranet.alxswe.com/rltoken/WglAv9ep-gg2wwo49DYfKg)
<br>

8. **8-uppercase.py** - Write a function that prints a string in uppercase followed by a new line.
    * Prototype: `def uppercase(str):`
    * You can only use no more than 2 `print` functions with string format
    * You can only use one loop in your code
    * You are not allowed to import any module
    * You are not allowed to use `str.upper()` and `str.isupper()`
    * [Tips:ord()](https://intranet.alxswe.com/rltoken/WglAv9ep-gg2wwo49DYfKg)
<br>

9. **9-print_last_digit.py** - Write a function that prints the last digit of a number.
    * Prototype: `def print_last_digit(number):`
    * Returns the value of the last digit
    * You are not allowed to import any module
<br>

10. **10-add.py** - Write a function that adds two integers and returns the result.
    * Prototype: `def add(a, b):`
    * Returns the value of `a + b`
    * You are not allowed to import any module
<br>

11. **11-pow.py** - Write a function that computes `a` to the power of `b` and return the value.
    * Prototype: `def pow(a, b):`
    * Returns the value of `a ^ b`
    * You are not allowed to import any module
<br>

12. **12-fizzbuzz.py** - Write a function that prints the numbers from 1 to 100 separated by a space.
    * For multiples of three print `Fizz` instead of the number and for multiples of five print `Buzz`.
    * For numbers which are multiples of both three and five print `FizzBuzz`.
    * Prototype: `def fizzbuzz():`
    * Each element should be followed by a space
    * You are not allowed to import any module
<br>

13. **13-insert_number.c, lists.h** - **Technical interview preparation**
    * You are not allowed to google anything
    * Whiteboard first
    * Write a function in C that inserts a number into a sorted singly linked list.
        * Prototype: `listint_t *insert_node(listint_t **head, int number);`
        * Return: the address of the new node, or `NULL` if it failed
<br>

14. **100-print_tebahpla.py** - Write a program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (`z` in lowercase and `Y` in uppercase) , not followed by a new line.
    * You can only use one `print` function with string format
    * You can only use one loop in your code
    * You are not allowed to store characters in a variable
    * You are not allowed to import any module
<br>

15. **101-remove_char_at.py** - Write a function that creates a copy of the string, removing the character at the position `n` (not the Python way, the “C array index”).
    * Prototype: `def remove_char_at(str, n):`
    * You are not allowed to import any module
<br>

16. **102-magic_calculation.py** - Write the Python function `def magic_calculation(a, b, c):` that does exactly the same as the following Python bytecode:
```3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
```

<br>

---
## Author
* Siphamandla Matshiane, [![Twitter](http://i.imgur.com/wWzX9uB.png)](https://twitter.com/sbumatshiane916)

## LICENSE
[ALX Software Engineering](https://www.alxafrica.com/software-engineering/)
