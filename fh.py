import sys, random

WORDLIST = "./words.txt" # 'c:\Python27\words.txt'

# This is where we'll put constants and "definitions" of things, not code that is explicitly going to execute.

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

def multTextGen(numRuns):
	for _ in range(int(numRuns)):
		textGen()

		
if "__main__" == __name__:
	
	# if you're running like a program, put all your "executable" code inside the __main__ check.
	# This makes sure that other functions you define (like textGen or multTextGen) can be imported
	# into other scripts without the "executable" stuff running. Like you wouldn't want the sys.argv check 
	# breaking your other thing from running, because maybe all is good in _that_ context.
	if len(sys.argv) < 2:
		print "Usage: python.exe fh.py <#words to generate> <#times to run> > <file_out.ext>"
	
	# same thing as the sys.argv check, only check these here in the "executable" area. 
	#numWords  = int(raw_input("How many words to generate? "))
	#numRuns = raw_input("How many times to run? ")
	numWords = int(sys.argv[1])
	numRuns = int(sys.argv[2])
	
	
	#textGen()
	multTextGen(numRuns) # because numRuns is no longer global, we'll need to pass it in
