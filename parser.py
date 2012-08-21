import sys
lines = open(sys.argv[1]) 
def s0():
	print "state s0"
def s1():
	print "state s1"
def s2():
	print "state s2"
def s3():
	print "state s3"
def s4():
	print "state s4"
def s5():
	print "state s5"
def s6():
	print "state s6"
def sE():
	print "state sE"
def states(x):
	return{
		's0':s0,
		's1':s1,
		's2':s2,
		's3':s3,
		's4':s4,
		's5':s5,
		's6':s6,
		'sE':sE,
	}[x]()
for line in lines:
	for character in line:
		print character
