#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg_len = len(argv) - 1
    if arg_len == 0:
        a_string = "arguments."
    elif arg_len == 1:
        a_string = "argument:"
    else:
        a_string = "arguments:"
    print(f"{arg_len} {a_string}")
    for i in range(1, arg_len + 1):
        print(f"{i}: {argv[i]}")
