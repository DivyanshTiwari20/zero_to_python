'''Solving the Tower of Hanoi problem is a classic recursive problem
that helps understand the principles of recursion.'''

def towerHanoi(n,a,b,c):
	if n==1:
		print("move 1st disk from ",a, " to ", c)
		return
	towerHanoi(n-1,a,c,b)
	print("move",n,"the disk from",a,"to",c)
	towerHanoi(n-1,b,a,c)

towerHanoi(14,"s","h","d")

