# Bucle For de Python

numeros = (1, 2, 3, 4, 5)

for num in numeros:
    print(num)

# Función Suma
    
def suma(num1, num2, num3):
    resultado = num1 + num2 + num3
    return resultado

print(suma(3, 5, 7))

# Función Lambda

sum_lamb = lambda num1, num2, num3: num1 + num2 + num3

print(sum_lamb(5, 2, 6))

# Valor en variable

nombre = 'Enrique'
lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']

if nombre in lista_nombre:
    print("El nombre está incluido en la lista.")
else:
    print("El nombre NO está incluido en la lista")
