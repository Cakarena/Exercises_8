##https://www.py4e.com/html3/08-lists, Exercise 2
## Figure out which line of the above program is still not properly guarded.
## See if you can construct a text file which causes the program to fail 
##and then modify the program so that the line is properly guarded 
##and test it to make sure it handles your new text file.

## The problem is if the SECOND word is missing also, not just the first, it will throw up an IndexError.
## Created a file called mbox-short2.txt I removed the second word from the first two lines i.e. Sat
## It just prints out a bunch of Fri and Thur now.

## THIS IS THE OLD FILE
#fhand = open('mbox-short2.txt', 'r')
#count = 0
#for line in fhand:
#   words = line.split()
#   # print('Debug:', words)
#   if len(words) == 0 : continue
#   if words[0] != 'From' : continue
#   print(words[2])

##THIS IS THE NEW FILE 

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