# Python - Data Structures: Lists, Tuples

## Description
> This repository contains scripts that are created as part of the learning objectives of programming at ALX SE programme. The emphasis is on enforcing problem solving skills through programming and other technologies. The `.c` and `.py` files created are for a deeper understanding of higher level programming in Python.

## Learning Objectives
* Why Python programming is awesome
* What are lists and how to use them
* What are the differences and similarities between strings and lists
* What are the most common methods of lists and how to use them
* How to use lists as stacks and queues
* What are list comprehensions and how to use them
* What are tuples and how to use them
* When to use tuples versus lists
* What is a sequence
* What is tuple packing
* What is sequence unpacking
* What is the `del` statement and how to use it

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

## Scripts
0. **0-print_list_integer.py** - Write a function that prints all integers of a list.
    * Prototype: `def print_list_integer(my_list=[]):`
    * Format: one integer per line.
    * You are not allowed to import any module
    * You can assume that the list only contains integers
    * You are not allowed to cast integers into strings
    * You have to use `str.format()` to print integers
<br>

1. **1-element_at.py** - Write a function that retrieves an element from a list like in C.
    * Prototype: `def element_at(my_list, idx):`
    * If `idx` is negative, the function should return `None`
    * If `idx` is out of range (> of number of element in `my_list`), the function should return `None`
    * You are not allowed to import any module
    * You are not allowed to use `try/except`
<br>


2. **2-replace_in_list.py** - Write a function that replaces an element of a list at a specific position (like in C).
    * Prototype: `def replace_in_list(my_list, idx, element):`
    * If `idx` is negative, the function should not modify anything, and returns the original list
    * If `idx` is out of range (> of number of element in `my_list`), the function should not modify anything, and returns the original list
    * You are not allowed to import any module
    * You are not allowed to use `try/except`
<br>

3. **3-print_reversed_list_integer.py** - Write a function that prints all integers of a list, in reverse order.
    * Prototype: `def print_reversed_list_integer(my_list=[]):`
    * Format: one integer per line. 
    * You are not allowed to import any module
    * You can assume that the list only contains integers
    * You are not allowed to cast integers into strings
    * You have to use `str.format()` to print integers
<br>

4. **4-new_in_list.py** - Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).
    * Prototype: `def new_in_list(my_list, idx, element):`
    * If `idx` is negative, the function should return a copy of the original `list`
    * If `idx` is out of range (> of number of element in `my_list`), the function should return a copy of the original `list`
    * You are not allowed to import any module
    * You are not allowed to use `try/except`
<br>

5. **5-no_c.py** - Write a function that removes all characters c and C from a string.
    * Prototype: `def no_c(my_string):`
    * The function should return the new string
    * You are not allowed to import any module
    * You are not allowed to use `str.replace()`
<br>

6. **6-print_matrix_integer.py** - Write a function that prints a matrix of integers.
    * Prototype: `def print_matrix_integer(matrix=[[]]):`
    * You are not allowed to import any module
    * You can assume that the list only contains integers
    * You are not allowed to cast integers into strings
    * You have to use `str.format()` to print integers
<br>

7. **7-add_tuple.py** - Write a function that adds 2 tuples.
    * Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`
    * Returns a tuple with 2 integers:
        * The first element should be the addition of the first element of each argument
        * The second element should be the addition of the second element of each argument
    * You are not allowed to import any module
    * You can assume that the two tuples will only contain integers
    * If a tuple is smaller than 2, use the value `0` for each missing integer
    * If a tuple is bigger than 2, use only the first 2 integers
<br>

8. **8-multiple_returns.py** - Write a function that returns a tuple with the length of a string and its first character.
    * Prototype: `def multiple_returns(sentence):`
    * If the sentence is empty, the first character should be equal to `None`
    * You are not allowed to import any module
<br>

9. **9-max_integer.py** - Write a function that finds the biggest integer of a list.
    * Prototype: `def max_integer(my_list=[]):`
    * If the list is empty, return `None`
    * You can assume that the list only contains integers
    * You are not allowed to import any module
    * You are not allowed to use the builtin `max()`
<br>

10. **10-divisible_by_2.py** - Write a function that finds all multiples of 2 in a list.
    * Prototype: `def divisible_by_2(my_list=[]):`
    * Return a new list with `True` or `False`, depending on whether the integer at the same position in the original list is a multiple of 2
    * The new list should have the same size as the original list
    * You are not allowed to import any module
<br>

11. **11-delete_at.py** - Write a function that deletes the item at a specific position in a list.
    * Prototype: `def delete_at(my_list=[], idx=0):`
    * If `idx` is negative or out of range, nothing change (returns the same list)
    * You are not allowed to use `pop()`
    * You are not allowed to import any module
<br>

12. **12-switch.py** - Complete the source code in order to switch value of `a` and `b`
    * You can find the source code [here](https://intranet.alxswe.com/rltoken/9kg8R2hfPSN5pClcVAeGlA)
    * Your code should be inserted where the comment is (line 4)
    * Your program should be exactly 5 lines long
<br>

13. **13-is_palindrome.c, lists.h** - **Technical interview preparation**
    * You are not allowed to google anything
    * Whiteboard first
    * Write a function in C that checks if a singly linked list is a palindrome.
        * Prototype: `int is_palindrome(listint_t **head);`
        * Return: `0` if it is not a palindrome, `1` if it is a palindrome
        * An empty list is considered a palindrome
<br>

14. **100-print_python_list_info.c** - CPython is the reference implementation of the Python programming language. Written in C, CPython is the default and most widely used implementation of the language.
Since we now know a bit of C, we can look at what is happening under the hood of Python. Let’s have fun with Python and C, and let’s look at what makes Python so easy to use.
    * All your files will be interpreted/compiled on Ubuntu 14.04 LTS
    * Create a C function that prints some basic info about Python lists:
        * Prototype: `void print_python_list_info(PyObject *p);`
        * Python version: 3.4
        * Your shared library will be compiled with this command line: `gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c`
        * OS: `Ubuntu 14.04 LTS`
        * Start by reading:
            * listobject.h
            * object.h
            * [Common Object Structures](https://intranet.alxswe.com/rltoken/jmRTk4m1VSzjsu3QTGaC6w)
            * [List Objects](https://intranet.alxswe.com/rltoken/7V1HlQRESjCqrKrw_O_Urw)
<br>

## Author
* Siphamandla Matshiane, [![Twitter](http://i.imgur.com/wWzX9uB.png)](https://twitter.com/sbumatshiane916)

## LICENSE
[ALX Software Engineering](https://www.alxafrica.com/software-engineering/)
