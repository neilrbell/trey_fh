import sys, random

WORDLIST = "./words.txt" # 'c:\Python27\words.txt'

# This is where we'll put constants and "definitions" of things, not code that is explicitly going to execute.

def textGen(numWords):
	with open(WORDLIST, 'r') as in_file:
		all_lines = [line.strip() for line in in_file.readlines()]
		num_lines = len(all_lines)
		numTexts = range(0, numWords)
		for i in numTexts:
			word_index = random.randint(0, num_lines-1) # https://docs.python.org/2/library/random.html#random.randint
			chosen_word = all_lines[word_index]
			# right now chosen_word is scoped to this loop. The output cycle below isn't inside this loop, 
			# so it'll just end up taking and using whatever the *final* value of chosen_word is.

			# In reality (in other languages) line 20 below should throw a horrible UnknownVariable error 
			# since chosen_word isn't defined outside the scope of this loop right here, so a language like C would
			# cause that variable to basically be garbage collected, and thus isn't available any longer. Python is nice
			# and lets chosen_word sorta be at the scope of the function (it's definitely not available down in multTextGen)
			# but that's it being nice.
	
	for i in xrange(3):
	   open('file_'+str(i)+'.txt', 'w').write(chosen_word)
			#print a[b] #this works, I just need to output this value each time...

def multTextGen(numRuns, numWords):
	for _ in range(int(numRuns)):
		textGen(numWords)

		
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
	multTextGen(numRuns, numWords) # because numRuns is no longer global, we'll need to pass it in
