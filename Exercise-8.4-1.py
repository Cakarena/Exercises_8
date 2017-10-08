##Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None.
##Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

def chop(t):
	t.remove(1) #In the readings this is the only place it says, it will return None
	t.remove(5)
my_list = [1, 2, 3, 4, 5]
chop(my_list)
print(my_list)


def middle (t):
	del t [0]
	del t [-1]

my_list = [1, 2, 3, 4, 5]
middle(my_list)
print(my_list)
# that works in the command thingo

