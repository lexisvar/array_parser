#!/usr/bin/env python
# return True if re.match('([a-zA-Z])',char) elsE FalsE
# -*- coding: utf-8 -*-
import sys
import re
lines = open(sys.argv[1])
list_vec_debug = ""
list_vec = ""
list_veca = ""
def s0(char):
	if re.match('([a-zA-Z])',char):
		return('s1')
	elif re.match('([0-9])',char):
		return('sE')
	elif re.match('([[])',char):
		return('sE')
	elif re.match('([]])',char):
		return('sE')
	elif re.match('([,])',char):
		return('s3')
	elif re.match('([;])',char):
		return('sE')
def s1(char):
	if re.match('([a-zA-Z])',char):
		return('s1')
	elif re.match('([0-9])',char):
		return('s1')
	elif re.match('([[])',char):
		return('s2')
	elif re.match('([]])',char):
		return('sE')
	elif re.match('([,])',char):
		return('s3')
	elif re.match('([;])',char):
		return('s4')
def s2(char):
	if re.match('([a-zA-Z])',char):
		return('sE')
	elif re.match('([0-9])',char):
		return('s5')
	elif re.match('([[])',char):
		return('sE')
	elif re.match('([]])',char):
		return('sE')
	elif re.match('([,])',char):
		return('sE')
	elif re.match('([;])',char):
		return('sE')
def s3(char):
	if re.match('([a-zA-Z])',char):
		return('s1')
	elif re.match('([0-9])',char):
		return('sE')
	elif re.match('([[])',char):
		return('sE')
	elif re.match('([]])',char):
		return('sE')
	elif re.match('([,])',char):
		return('sE')
	elif re.match('([;])',char):
		return('sE')
def s4(char):
	if re.match('([a-zA-Z])',char):
		return('sE')
	elif re.match('([0-9])',char):
		return('sE')
	elif re.match('([[])',char):
		return('sE')
	elif re.match('([]])',char):
		return('sE')
	elif re.match('([,])',char):
		return('sE')
	elif re.match('([;])',char):
		return('sE')
def s5(char):
	if re.match('([a-zA-Z])',char):
		return('sE')
	elif re.match('([0-9])',char):
		return('s5')
	elif re.match('([[])',char):
		return('sE')
	elif re.match('([]])',char):
		return('s6')
	elif re.match('([,])',char):
		return('sE')
	elif re.match('([;])',char):
		return('sE')
def s6(char):
	if re.match('([a-zA-Z])',char):
		return('sE')
	elif re.match('([0-9])',char):
		return('sE')
	elif re.match('([[])',char):
		return('sE')
	elif re.match('([]])',char):
		return('sE')
	elif re.match('([,])',char):
		return('s3')
	elif re.match('([;])',char):
		return('s4')
def sE(char):
	if re.match('([a-zA-Z])',char):
		return('s1')
	elif re.match('([0-9])',char):
		return('s1')
	elif re.match('([[])',char):
		return('s2')
	elif re.match('([]])',char):
		return('sE')
	elif re.match('([,])',char):
		return('s3')
	elif re.match('([;])',char):
		return('s4')
def states(x,char):
        return{
                's0':s0,
                's1':s1,
                's2':s2,
                's3':s3,
                's4':s4,
                's5':s5,
                's6':s6,
                'sE':sE,
        }[x](char)
current_state = 's0'
for line in lines:
	print "Input: "+line;
	for character in line:
		current_state = states(current_state,character)
		#list_vec_debug+=character
		list_vec+=character
		#print list_vec_debug.split(',')
		list_vec
		if current_state == 's6':
			list_veca += list_vec+","
		elif character==',':
			list_vec=''
		#print character,states(current_state,character),current_state
		states(current_state,character)
print "Ouput: "+list_veca