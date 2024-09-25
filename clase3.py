

#PEDIR DOS NUMEROS POR TECLADO Y MOSTRA LA SUMA DE AMBOS

#V1

"""
num_uno = input("Ingrese un numero: ")
num_dos = input("Ingrese otro numero: ")


num_uno = int(num_uno)
num_dos = int(num_dos)


suma = num_uno + num_dos

print("La suma de los dos numero es: ", suma)

"""

#V2
"""
num_uno = int(input("Ingrese un numero: "))
num_dos = int(input("Ingrese otro numero: "))

suma = num_uno + num_dos

print("La suma de los dos numero es: ", suma)
"""


#V3
"""
suma = int(input("Ingrese un numero: ")) + int(input("Ingrese otro numero: "))

print("La suma de los dos numero es: ", suma )
"""






#INT 

#EJEMPLO 1
resultado = int("30")
print(resultado)
print(type(resultado))


#EJEMPLO 2
print( int("50") )

#EJEMPLO 3

#print( int("Pedro") )


#FLOAT

resultado = float("55.1")
print(resultado)
print(type(resultado))

#STR

resultado = str(100)
print(resultado)
print(type(resultado))









"""

cuenta = float(input("¿Cuánto se gastó en la comida?: "))
propina = float(input("¿Qué porcentaje de propina se quiere dejar?: "))
propina_a_pagar = propina * cuenta / 100
total_a_pagar = propina_a_pagar + cuenta
print("La cuenta fue de $" , cuenta ,". La propina de " ,propina, "% es de $" ,propina_a_pagar,". El total a pagar es de $" ,total_a_pagar)

"""



# F STRINGS

nombre_alumno = "Juan"
print("Hola: ", nombre_alumno )
#print("Hola: "+ nombre_alumno )
print( f"Hola: {nombre_alumno}")


a =30
b= 60

print("Suma: a+b")
print(f"Suma: {a+b}")