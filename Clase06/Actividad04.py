print("biemvenidos al registro de estudiantes")
While True
Nombre= input("ingrese su nombre: ")
Carnet = input("Ingrse su carnet: ")
Nota = float(input("ingrese su nota final: "))

archivo = open("Clase06\Estudiantes.txt" , "a")
archivo.write(f"nombre:   {Nombre}\n")
archivo.write(f"carnet   {Carnet}\n")
archivo.write(f"nota final:   {Nota}\n")
archivo.close()
