#!/usr/bin/env python3
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the
# words with more than 20 characters (not counting whitespace).
##############################################################################
# Imports

# Body
def findWords(n):
	""" Finds words in the input file that are more than n characters in length (excluding whitespaces) 
	"""
	file = open("words.txt")
	for word in file:
		if(len(word.strip()) > n):
			print(word)


##############################################################################
def main():
    pass  # Call your functions here.

    findWords(20)

if __name__ == '__main__':
    main()
