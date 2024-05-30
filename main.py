#Contador de vocales en nombres

#Funcion para contar vocales
Nombre  = input("Ingrese su nombre: ")
count = 0
Vocales = ("a","e","i","o","u")
for item in Nombre:
  if item in Vocales:
    count += 1
if count <= 3:
   print("Su nombre tiene 3 o mas vocales")
else:
   print("Su nombre tiene menos de 3 vocales")