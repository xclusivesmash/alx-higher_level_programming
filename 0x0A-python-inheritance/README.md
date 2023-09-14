# Python - Inheritance

## Description
> This repository contains scripts that are created as part of the learning objectives of programming at ALX SE programme. The emphasis is on enforcing problem solving skills through programming and other technologies. The `.py` files created are for a deeper understanding of inheritance in Python.

## Learning Objectives
- Why Python programming is awesome
- What is a superclass, baseclass or parentclass
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit class from another
- How to define a class with multiple base classes
- What is the default class every class inherit from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- What are, when and how to use `isinstance`, `issubclass`, `type` and `super` built-in functions

## Requirements

### General
- Allowed editors: `vi`, `vim`, or `emacs`
- All files should end with a new line
- Operating system: `Ubuntu 20.04 LTS`
- The length of all files will be tested using `wc`

### Python Scripts
- The first line of all files should be exactly `#!/usr/bin/python3`
- All files must be executables

### Python Test Cases
- All test files should be inside a folder `tests`
- All test files should be text files (extension: `.txt`)
- All tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)

--- 
## Scripts

0. **0-lookup.py** - Write a function that returns the list of available attributes and methods of an object:
    * Prototype: `def lookup(obj):`
    * Returns a `list` object
    * You are not allowed to import any module
<br>

1. **1-my_list.py, tests/1-my_list.txt** - Write a class `MyList` that inherits from `list`:
    * Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort)
    * You can assume that all the elements of the list will be of type `int`
    * You are not allowed to import any module
<br>

2. **2-is_same_class.py** - Write a function that returns `True` if the object is exactly an instance of the specified class ; otherwise `False`.
    * Prototype: `def is_same_class(obj, a_class):`
    * You are not allowed to import any module
<br>

3. **3-is_kind_of_class.py** - Write a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise `False`.
    * Prototype: `def is_kind_of_class(obj, a_class):`
    * You are not allowed to import any module
<br>

4. **4-inherits_from.py** - Write a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise `False`.
    * Prototype: `def inherits_from(obj, a_class):`
    * You are not allowed to import any module
<br>

5. **5-base_geometry.py** - Write an empty class `BaseGeometry`.
    * You are not allowed to import any module
<br>

6. **6-base_geometry.py** - Write a class `BaseGeometry` (based on `5-base_geometry.py`).
    * Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`
    * You are not allowed to import any module
<br>

7. **7-base_geometry.py, tests/7-base_geometry.txt** - Write a class `BaseGeometry` (based on `6-base_geometry.py`).
    * Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`
    * Public instance method: `def integer_validator(self, name, value):` that validates `value`:
        * you can assume `name` is always a string
        * if `value` is not an integer: raise a `TypeError` exception, with the message `<name> must be an integer`
        * if `value` is less or equal to `0`: raise a `ValueError` exception with the message `<name> must be greater than 0`
    * You are not allowed to import any module
<br>

8. **8-rectangle.py** - Write a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`).
    * Instantiation with `width` and `height`: `def __init__(self, width, height):`
        * `width` and `height` must be private. No getter or setter
        * `width` and `height` must be positive integers, validated by `integer_validator`
<br>

9. **9-rectangle.py** - Write a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`). (task based on `8-rectangle.py`)
    * Instantiation with `width` and `height`: `def __init__(self, width, height):`:
        * `width` and `height` must be private. No getter or setter
        * `width` and `height` must be positive integers, validated by `integer_validator`
    * the `area()` method must be implemented
    * `print()` should print, and `str()` should return, the following rectangle description: `[Rectangle] <width>/<height>`
<br>

10. **10-square.py** - Write a class `Square` that inherits from `Rectangle` (`9-rectangle.py`):
    * Instantiation with `size`: `def __init__(self, size):`:
        * `size` must be private. No getter or setter
        * `size` must be a positive integer, validated by `integer_validator`
    * the `area()` method must be implemented
<br>

11. **11-square.py** - Write a class `Square` that inherits from `Rectangle` (`9-rectangle.py`). (task based on `10-square.py`).
    * Instantiation with `size`: `def __init__(self, size):`:
        * `size` must be private. No getter or setter
        * `size` must be a positive integer, validated by `integer_validator`
    * the `area()` method must be implemented
    * `print()` should print, and `str()` should return, the square description: `[Square] <width>/<height>`
<br>

12. **100-my_int.py** - Write a class `MyInt` that inherits from `int`:
    * `MyInt` is a rebel. `MyInt` has `==` and `!=` operators inverted
    * You are not allowed to import any module
<br>

13. **101-add_attribute.py** - Write a function that adds a new attribute to an object if it’s possible:
    * Raise a `TypeError` exception, with the message `can't add new attribute` if the object can’t have new attribute
    * You are not allowed to use `try/except`
    * You are not allowed to import any module
<br>

---
## Author
* Siphamandla Matshiane, [![Twitter](http://i.imgur.com/wWzX9uB.png)](https://twitter.com/sbumatshiane916)

## LICENSE
[ALX Software Engineering](https://www.alxafrica.com/software-engineering/)
