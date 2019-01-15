import math
print("Noteikta integrala aprekinasana\n")
N = int(input("Ievadiet, cik summas bus integrali,\nvairak ir precizak, bet var aiznemt ilgaku laiku: "))
a = float(input("\nIntegresanas sakuma punkts: "))
b = float(input("Integresanas beigu punkts: "))
funkcija = "math.sin(x)"

def integ(N, a, b):
    def f(x):
        return eval(funkcija)
    x1=0
    x2=0
    
    for n in range(1,N+1):
        x1 += f(a+((n-(1/2))*((b-a)/N)))
    x2 = ((b-a)/N)*x1
    return x2

print("\nNoteiktais integralis funkcijai %s starp %g un %g ir %.2f."%(funkcija, a, b, integ(N,a,b)))