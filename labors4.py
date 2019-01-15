import math as math4

#precizitate
h = 0.01

#definejam (izmantoju https://en.wikipedia.org/wiki/Finite_difference)
def f(x):
    return math4.sin(x)
def atv(c):
    return (math4.sin(c+h)-math4.sin(c))/h
def atv2(d):
    return (math4.sin(d+h)-2*math4.sin(d)+math4.sin(d-h))/(h**2)

#inputs   
print("Tabula ar pirmo un otro sinusa atvasinajumu\n")
a = int(input("Ievadi aprekinu sakumpunktu: "))
b = int(input("Ievadi aprekinu beigu punktu: "))

#neliels loops
print()
print("\t\t sinuss \tatvasinajums\totras kartas")
print("skaitlis a\t punkta a\tpunkta a\tatvasinajums")
print()
for i in range(a,b+1):
    print ("%d\t\t %.2f\t\t %.2f\t\t %.2f"%(i, f(i), atv(i), atv2(i)))
