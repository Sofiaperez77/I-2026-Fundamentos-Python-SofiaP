contador = 0
while true
print("biemvenidos al registro de estudiantes")
Nombre= input("ingrese su nombre: ")
Carnet = input("Ingrse su carnet: ")
Nota = float(input("ingrese su nota final: "))

#Contador de estudiantes registrados
Contador += 1
print("Registro de estudiantes guardado exitosamente")
print("Total de estudiantes registrados:" contador)


archivo = open("Clase06\Estudiantes.txt" , "a")
archivo.write(f"nombre:   {Nombre}\n")
archivo.write(f"carnet   {Carnet}\n")
archivo.write(f"nota final:   {Nota}\n")
archivo.close()

continuar = input("¿Desea registrar otro estudiante? (si/no):")
if continuar.lower()=="no":
 break