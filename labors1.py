import math as math2
print("Sin aprekinasana:")
x = float(input("Ievadi argumentu x: "))
y = math2.sin(x)
print("sin(%.2f)=%.2f"%(x,y))
print()

k = 0
a = (-1)**0*x**1/(1)
S = a
print("a0 = %.2f S0 = %.2f"%(a,S))

#neliels loops
for k in range(1, 501):
    a = a * (-1)*x*x/((2*k)*(2*k+1))
    S = S + a
    if k == 499 or k == 500:
        print("a%d = %.2f S%d = %.2f"%(k,a,k,S))

#gala rezultats pie 500 iteracijas
print("sin(%.2f) caur summu: %.2f"%(x,S))

#ascii
print()
print("            500")
print("           _____")
print("           \           k   2*k+1")
print("            \      (-1) * x")
print("sin(%.2f) = >   _________________ = %.2f"%(x,S))
print("            /")
print("           /____      (2*k+1)!")
print("            k=0")
print()
print("                                    2")
print("                            (-1) * x")
print("rekurences reizinatajs: ___________________")
print()
print("                          k * 2 * (2*k+1)")



