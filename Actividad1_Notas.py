nota1=float(input("digite la nota 1: "))
nota2=float(input("digite la nota 2: "))
nota3=float(input("digite la nota 3: "))

p1=nota1*0.3
p2=nota2*0.3
p3=nota3*0.4

nf=p1+p2+p3

print(f"su nota final es de: {nf} ")

if 1 <= nf  <= 1.9:
    print("deficiente")
elif 1.9 <= nf  <= 2.9:    
    print("insuficiente")
elif 2.9 <= nf  <= 3.9: 
    print("aceptable")
elif 4.0<= nf <=5.0:
    print("destacado") 