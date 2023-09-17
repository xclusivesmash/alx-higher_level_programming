#!/usr/bin/python3
"""
Module: 7-add_item.py
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    content = load_from_json_file("add_item.json")
except FileNotFoundError:
    content = []

my_list = sys.argv[1:]
content += my_list
save_to_json_file(content, "add_item.json")
load_from_json_file("add_item.json")
