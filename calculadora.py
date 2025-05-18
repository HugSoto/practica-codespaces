def suma(a, b):
 return a + b

def resta(a, b):
 return a - b

def multiplicar(a, b):
 return a * b
 
def dividir(a, b):
 if b != 0:
    return a / b
 return "Error: división por cero"

print("Suma:", suma(4, 2))
print("Resta:", resta(4, 2))
print("Multiplicación:", multiplicar(4, 2))
print("División:", dividir(4, 2))