#!/usr/bin/env python3

def to_seconds(hours, minutes, seconds):
	return hours * 3600 + minutes*60 + seconds

print("Welcome to this time convertor")

cont = "y"
while(cont.lower() == "y"):
	hours = int(input("Enter the no. of hours : "))
	minutes = int(input("Enter the no. of minutes : "))
	seconds = int(input("Enter the no. of seconds : "))
	print("That's {} seconds. ".format(to_seconds(hours, minutes, seconds)))
	print()
	cont = input("Do you want to do another conversion : [y to continue] ")

print("Good Bye!")
