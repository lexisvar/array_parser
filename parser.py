import sys
import re
lines = open(sys.argv[1])
def s0(char):
	return True if char==('(a-Z)') else False
def s1(char):
	print "state s1"
def s2(char):
	print "state s2"
def s3(char):
	print "state s3"
def s4(char):
	print "state s4"
def s5(char):
	print "state s5"
def s6(char):
	print "state s6"
def sE(char):
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
		print s0(character)
