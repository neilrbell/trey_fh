import sys, random

WORDLIST = "./words.txt" # 'c:\Python27\words.txt'

#numWords  = int(raw_input("How many words to generate? "))
#numRuns = raw_input("How many times to run? ")

if len(sys.argv) < 2:
	print "Usage: python.exe fh.py <#words to generate> <#times to run> > <file_out.ext>"


numWords = int(sys.argv[1])
numRuns = int(sys.argv[2])

def textGen():
	with open(WORDLIST, 'r') as in_file:
		a = in_file.readlines()
		space = range(0,len(a))
		numTexts = range(0, numWords)
		for i in numTexts:
			b = random.choice(space)
			c = a[b]
	for i in xrange(3):
	   open('file_'+str(i)+'.txt', 'w').write(c)
			#print a[b] #this works, I just need to output this value each time...

def multTextGen():
	for _ in range(int(numRuns)):
		textGen()

		
if "__main__" == __name__:
	#textGen()
	multTextGen()
