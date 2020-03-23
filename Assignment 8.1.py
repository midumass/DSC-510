# DSC510-T301 Assignment 8.1
# Zachary Hill
# 02FEB2019
# This program takes a file, parses each line of the file then splits out each word in each line and either adds the words to a dictionary as a key with value 1 or increments the value if the key is already found.
# Run the program and enter your filename when prompted.
		
import string

textfile = input('Please enter your text file name including extention: ')
dict = {}
sorted_dict = []

def pretty_print(dict):
	print('Length of the dictionary: ', len(dict))
	print('Word          Count')
	print('___________________')
	sorted_dict = [(key, dict[key]) for key in sorted(dict, key=dict.get, reverse=True)]
	for key, value in sorted_dict:
		print(key.ljust(12), repr(value).rjust(6))
	
def add_word(words, dict):
	for word in words:
		if word not in dict:
			dict[word] = 1
		else :
			dict[word] += 1
		
def process_line(line, dict):
	for lines in line:
		lines = lines.rstrip()
		words = lines.translate(lines.maketrans('', '', string.punctuation)).lower().split()
		add_word(words, dict)
			
def main(text):
	with open(text) as f:
		process_line(f, dict)
		pretty_print(dict)
	f.closed
		
main(textfile)

