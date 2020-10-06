#!/usr/bin/env python3

def pair(y):
	for i in y:
		a = bin(i).strip('0b')
		if(a.count("1") % 2 == 0 ):
			b = "1" + a
			c = bytearray(b,'utf-8')
		else:
			b = "0" + a
			c = bytearray(b,'utf-8')
	print("Le bytearray avec le bit de parite est: ",c)
x = input("entrer un mot: ")
y = bytearray(x,'utf-8')
pair(y)
