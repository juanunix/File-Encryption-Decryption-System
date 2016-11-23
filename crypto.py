'''
Project Name:- Crypto

Description:- Encryption of a text file using a key string. Algorithm of encryption is based on bitwise XORing of successive
characters of the file with successive characters of the key. When all the characters of the key are over,
they start all over again.
If we would run the program on the encrypted file with the same key, the algorithm would decrypt the
file as XOR operation is reversible.
Imported libraries are sys,uuid,getopt,hashlib.
sys:- For system functions.
uuid:- For generating random key.
getopt:- For command line arguments
hashlib:- For sha256 hash encryption


 
'''


import sys, uuid, getopt, hashlib
# Functon for reading the input text file and storing the whole file as a string.
def get(g):
	l = list(open(g,"r").readlines())
	s = ""
	for i in l:
		s += i
	return s
# Function for opening the output file, cleaning it and writting the encrypted text in it. 
def set(s, x):
	fp=open(s,"w")
	fp.truncate()
	fp.write(x)
# Function for generating a hash value for the key string.
def hash(k):
	k1 = k.encode('utf-8')
	return ((hashlib.sha256(k1)).hexdigest())
# Function to check if the file is already encrypted and if already encrypted,the key entered for decryption 
# is correct or not. 
def check(s, k):
		x = ""
		y = hash(k)
		s1 = s.split("\n")
		l = len(s1)
		#print("Hashfn : ", s1[0], y)
		if(s1[0]==y):
			for i in range(1, l-1):
					x = x+s1[i]+"\n"
			x = x+s1[l-1]
			#print(x, s)
			return x, 1
		else:
			return s, 0
# Function to generate a random key.
def random():
	return(str(uuid.uuid4()))
# Function to XOR the file content and the key
def crypt(s1, k):
	s2 = ""
	s3 = ""
	j = 0
	try:
		for i in s1:
			xbyte = ord(i)^ord(k[j])
			j += 1
			j = j%len(k)
			s2 += (chr(xbyte))
	finally:
 		return (s2)
# In the main program, we use flags to check whether or not any specific option(inputfile, outputfile, encryption key) is being used or not
def main(argv):
	inpfile = ''
	outfile = ''
	key = ''
	flag1 = 0
	flag2 = 0
	flag3 = 0
	try:
		opts, args = getopt.getopt(argv, "hi:o:k:", ["-i","-o","-k"])
	except getopt.GetoptError:
		print("Usage: test.py -i <input_file> -o <output_file> -k <key_for_encryption>\n-h or -help for usage\ndefault action without -i or --outputfile: takes input in the terminal\ndefault action without -o or --outputfile : displays output in terminal\ndefault action without -k or --key: generates and displays random key, which has to be inputed at the time of decryption\n")
		sys.exit(0)
	for opt, arg in opts:
		if opt in ("-h", "-help"):
			print("Usage: test.py -i <input_file> -o <output_file> -k <key_for_encryption>\n-h or -help for usage\ndefault action without -i or --outputfile: takes input in the terminal\ndefault action without -o or --outputfile : displays output in terminal\ndefault action without -k or --key: generates and displays random key, which has to be inputed at the time of decryption\n")
			sys.exit(1)
		elif opt in ('-i', "--inputfile"):
			flag1 = 1
			inpfile = arg
		elif opt in ('-o', "--outputfile"):
			flag2 = 1
			outfile = arg
		elif opt in ("-k", "--key"):
			flag3 = 1
			key = arg
	if flag3 == 0:
		key = random()
		print(key)
	if flag1 == 1:
		#print("Input file:", inpf)
		inputstring = get(inpfile)
		inputstring1, flag4 = check(inputstring, key)
		outputstring = crypt(inputstring1, key)
		if(flag4 == 0):
			outputstring = hash(key)+"\n"+outputstring
		#print(s1,crypt(s1, key))
		if flag2 == 1:
		#	print("Output file:", outf)
			set(outfile, outputstring)
		else:
			print("Output\n"+outputstring)
	else:
		text = input("No Input file:\nEnter text to encrypt:\n")
		outputstring = hash(key)+"\n"+crypt(text,key)
		if flag2 == 1:
			set(outfile, outputstring)
		else:
			print("Output\n"+outputstring)

if __name__ == "__main__":
	main(sys.argv[1:])
