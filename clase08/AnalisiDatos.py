import pandas

#carga el archivo CSV
datos=pandas.read_csv("clase08/estudiantes.csv")

#Mostrar las primeras filas del DataFrame
print(datos.head(2))

#Mostrar solo las columnas "nombre" y "apellido"
print(datos[["Nombre , ""Apellido"]].head(5))

#Calcular estadisticas descriptivas
print(datos.describe())

#Calcular estadisticas descriptiva
print(datos.describe())

#Calcular el maximo de la edad 
print(datos[´edad´].max())

#Calcular el minimo de la edad
print(datos[´edad´].min())
            
#Filtrar estudiantes con calificacion mayora 85
estudiantes_alta_nota=datos.groupby(´sexo´)[´nota´].mean()
print(media_por_genero)

