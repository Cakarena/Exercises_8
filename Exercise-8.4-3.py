##https://www.py4e.com/html3/08-lists, Exercise 3
## Exercise 3: Rewrite the guardian code in the above example without two if statements. 
##Instead, use a compound logical expression using the and logical operator with a single if statement.

##THIS IS THE EXERCISE 2 FILE: 

#fhand = open('mbox-short2.txt', 'r')
#count = 0
#for line in fhand:
#   words = line.split()
#   # print('Debug:', words)
#   if len(words) == 0 or len(words) < 3: continue
#   if words[0] != 'From' : continue
#   print(words[2])

###EXERCISE 3, THIS IS THE REWRITE:
## Exercise 3: Rewrite the guardian code in the above example without two if statements. 
##Instead, use a compound logical expression using the and logical operator with a single if statement.

fhand = open('mbox-short2.txt', 'r')
count = 0
for line in fhand:
	words = line.split()
    # print('Debug:', words)
    #if (len(words) == 0 or len(words) < 3) and words[0] != 'From': continue (doesn't work obviously)
    ##if not line.startswith('From ') and (len(words) == 0 or len(words) < 3): continue 
    ##Line 29 actually works!!! Why use 'and' as an operator??
	if len(words) >= 3 and words[0] == 'From':  
			print(words[2])
