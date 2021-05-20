#!/usr/bin/python3
#
#  Author:      Cameron Kerley
#  Date:        6 Feb 2019
#  Description: Caesar Cipher

import time, os, sys, encryptText, argparse

def main():
	parser = argparse.ArgumentParser(description='Encrypt a textfile with 2 ciphers i wrote')
	parser.add_argument('--file-In', dest='input', required=True)
	parser.add_argument('--file-Out', dest='output', required= True)
	args = parser.parse_args()
	inputFilename = args.input
	print('orginal .txt', inputFilename)
	# BE CAREFUL! If a file with the outputFilename name already exists,
	# this program will overwrite that file.
	outputFilename = args.output
	print('output .txt', outputFilename)
	
	myKey = int(input('select the key used/to be used : \n'))

	print('set to "encrypt" or "decrypt"')
	myMode = input()
	 

	# If the input file does not exist, then the program terminates early.
	if not os.path.exists(inputFilename):
		print('The file %s does not exist. Quitting...' % (inputFilename))
		sys.exit()

	# If the output file already exists, give the user a chance to quit.
	if os.path.exists(outputFilename):
		print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename))
		response = input('> ')
		if not response.lower().startswith('c'):
			sys.exit()

	# Read in the message from the input file
	fileObj = open(inputFilename)
	content = fileObj.read()
	fileObj.close()

	print('%sing...' % (myMode.title()))

	# Measure how long the encryption/decryption takes.
	startTime = time.time()
	if myMode.lower() == 'encrypt':
		translated = encryptText.encryptMessage(myKey, content)
		translated = encryptText.ceaser(myKey, translated, myMode)
	elif myMode.lower() =='decrypt':
		translated = encryptText.decryptMessage(myKey, content)
		translated = encryptText.ceaser(myKey,translated, myMode)
	totalTime = round(time.time() - startTime, 2)
	print('%sion time: %s seconds' % (myMode.title(), totalTime))

	# Write out the translated message to the output file.
	outputFileObj = open(outputFilename, 'w')
	outputFileObj.write(translated)
	outputFileObj.close()

	print('Done %sing %s (%s characters).' % (myMode, inputFilename, len(content)))
	print('%sed file is %s.' % (myMode.title(), outputFilename))


# If transpositionCipherFile.py is run (instead of imported as a module)
# call the main() function.
if __name__ == '__main__':
	main()
