#!/usr/bin/env python3

data = input("This will come from STDIN: ")
print("Now we will write it to STDOUT: " +data)
raise ValueError("Now we will generate an error to STDERR")
