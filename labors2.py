import math as math3
print("Sin iteraciju aprekinasana:")
x = float(input("Ievadi argumentu x: "))
y = math3.sin(x)

a = (-1)**0*x**1/(1)
S = a
k = 1

#uzsettojam precizitati
precizitate = 0.01

#neliels loops
while abs(S-y)>precizitate:
    a = a * (-1)*x*x/((2*k)*(2*k+1))
    S = S + a
    k=k+1

#outputs
print("\nPreciza sin(%g) vertiba ir %.4f, aprekinata vertiba ir %.4f.\nLai iegutu sadu precizitati (%g), bija nepieciesamas %d iteracijas."%(x,y,S,precizitate,k))







