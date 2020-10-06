#!/usr/bin/env python3
x=input("Entrez un mot : ")
print("Lettre Valeur checksumsum1  checksum2")
cs1=0
cs2=0
for i in range(len(x)):   
    cs1 = cs1 + ord(x[i])
    cs2 = cs2 + cs1
    print("   "+x[i]+"     "+str(ord(x[i]))+ "    "+str(cs1)+"    "+str(cs2) ) 
