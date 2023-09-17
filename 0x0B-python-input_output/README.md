# Python - Input/Output

## Description
> This repository contains scripts that are created as part of the learning objectives of programming at ALX SE programme. The emphasis is on enforcing problem solving skills through programming and other technologies. The `.py` files created are for a deeper understanding of I/O in Python.

## Learning Objectives
- Why Python programming is awesome
- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the `with` statement
- What is `JSON`
- What is serialization
- What is deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure

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

0. **0-read_file.py** - Write a function that reads a text file (`UTF8`) and prints it to stdout:
    * Prototype: `def read_file(filename=""):`
    * You must use the `with` statement
    * You don’t need to manage `file permission` or `file doesn't exist` exceptions.
    * You are not allowed to import any module
<br>

1. **1-write_file.py** - Write a function that writes a string to a text file (`UTF8`) and returns the number of characters written:
    * Prototype: `def write_file(filename="", text=""):`
    * You must use the `with` statement
    * You don’t need to manage file permission exceptions.
    * Your function should create the file if doesn’t exist.
    * Your function should overwrite the content of the file if it already exists.
    * You are not allowed to import any module
<br>

2. **2-append_write.py** - Write a function that appends a string at the end of a text file (`UTF8`) and returns the number of characters added:
    * Prototype: `def append_write(filename="", text=""):`
    * If the file doesn’t exist, it should be created
    * You must use the `with` statement
    * You don’t need to manage `file permission` or `file doesn't exist` exceptions.
    * You are not allowed to import any module
<br>

3. **3-to_json_string.py** - Write a function that returns the JSON representation of an object (string):
    * Prototype: `def to_json_string(my_obj):`
    * You don’t need to manage exceptions if the object can’t be serialized.
<br>

4. **4-from_json_string.py** - Write a function that returns an object (Python data structure) represented by a JSON string:
    * Prototype: `def from_json_string(my_str):`
    * You don’t need to manage exceptions if the JSON string doesn’t represent an object.
<br>

5. **5-save_to_json_file.py** - Write a function that writes an Object to a text file, using a JSON representation:
    * Prototype: `def save_to_json_file(my_obj, filename):`
    * You must use the `with` statement
    * You don’t need to manage exceptions if the object can’t be serialized.
    * You don’t need to manage file permission exceptions.
<br>

6. **6-load_from_json_file.py** - Write a function that creates an Object from a “JSON file”:
    * Prototype: `def load_from_json_file(filename):`
    * You must use the `with` statement
    * You don’t need to manage exceptions if the JSON string doesn’t represent an object.
    * You don’t need to manage file permissions / exceptions.
<br>

7. **7-add_item.py** - Write a script that adds all arguments to a Python list, and then save them to a file:
    * You must use your function `save_to_json_file` from `5-save_to_json_file.py`
    * You must use your function `load_from_json_file` from `6-load_from_json_file.py`
    * The list must be saved as a JSON representation in a file named `add_item.json`
    * If the file doesn’t exist, it should be created
    * You don’t need to manage file permissions / exceptions.
<br>

8. **8-class_to_json.py** - Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:
    * Prototype: `def class_to_json(obj):`
    * `obj` is an instance of a Class
    * All attributes of the `obj` Class are serializable: list, dictionary, string, integer and boolean
    * You are not allowed to import any module
<br>

9. **9-student.py** - Write a class `Student` that defines a student by:
    * Public instance attributes:
        * `first_name`
        * `last_name`
        * `age`
    * Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
    * Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`):
    * You are not allowed to import any module
<br>

10. **10-student.py** - Write a class `Student` that defines a student by: (based on `9-student.py`)
    * Public instance attributes:
        * `first_name`
        * `last_name`
        * `age`
    * Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
    * Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`):
        * If `attrs` is a list of strings, only attributes name contain in this list must be retrieved.
        * Otherwise, all attributes must be retrieved
    * You are not allowed to import any module
<br>

11. **11-student.py** - Write a class `Student` that defines a student by: (based on `10-student.py`)
    * Public instance attributes:
        * `first_name`
        * `last_name`
        * `age`
    * Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
    * Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`):
        * If `attrs` is a list of strings, only attributes name contain in this list must be retrieved.
        * Otherwise, all attributes must be retrieved
    * Public method `def reload_from_json(self, json):` that replaces all attributes of the `Student` instance:
        * You can assume `json` will always be a dictionary
        * A dictionary key will be the public attribute name
        * A dictionary value will be the value of the public attribute
    * You are not allowed to import any module
<br>

12. **12-pascal_triangle.py** - **Technical interview preparation**
    * You are not allowed to google anything
    * Whiteboard first
    * Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of `n`:
        * Returns an empty list if `n <= 0`
        * You can assume `n` will be always an integer
        * You are not allowed to import any module
<br>

---
## Author
* Siphamandla Matshiane, [![Twitter](http://i.imgur.com/wWzX9uB.png)](https://twitter.com/sbumatshiane916)

## LICENSE
[ALX Software Engineering](https://www.alxafrica.com/software-engineering/)
