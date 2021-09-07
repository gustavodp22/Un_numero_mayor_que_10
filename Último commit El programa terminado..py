"""Escriba un algoritmo que lea del teclado un número entero y que compruebe si el número es menor que 10. Si no lo está, debe volver a leer el número repitiendo la operación hasta que el usuario escriba un valor correcto. Finalmente, debe escribir por pantalla el valor leído cuando este sea correcto"""

#!/usr/bin/python3
numero = int(input(u"Ingrese un número"))
while numero<10:
 numero = int(input(u"Ingrese un número"))
print ("numero")
