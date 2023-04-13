#!/usr/bin/python3
"""
Module 7-add_item
that imports functions save_to_json_file and load_from_json_file
It adds all arguments given from commandline to a Python list,
and then saves them to a file
"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    file_content = load_from_json_file(filename)
except FileNotFoundError:
    file_content = []

save_to_json_file(file_content + argv[1:], filename)
