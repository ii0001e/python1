from math import *

print("Ruudu karakteristikud")
a=float(input("Sisesta ruudu k�lje pikkus => "))
S=a**2
print("Ruudu pindala - ",S)
P=4*a
print("Ruudu �mberm��t - ",P)
di_1=round(a*sqrt(2),2)
print("Ruudu diagonaal - ",di_1,"\n")
######################################
print("Ristk�liku karakteristikud")
b=float(input("Sisesta ristk�liku 1. k�lje pikkus => "))
c=float(input("Sisesta ristk�liku 2. k�lje pikkus => "))
S_1=b*c
print("Ristk�liku pindala - ",S_1)
P=2*(b+c)
print("Ristk�liku �mberm��t - ",P)
di_2=round(sqrt(b**2+c**2),2)
print("Ristk�liku diagonaal - ",di_2,"\n")
#######################################
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => "))
d=2*r
print("Ringi l�bim��t - ",d)
S_2=round(pi*r**2,2)
print("Ringi pindala - ",S_2)
Cp=round(2*pi*r,2)
print("Ringjoone pikkus - ",Cp)