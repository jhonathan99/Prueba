print("programa para ver si el alumno gano o perdio el año")  #Da una bienvenida al programa 
nombre_estudiante = input("Ingrese el nombre del estudiante: ")   #pide al usuario ingresar el nombre del estudiante 
grado_estudiante = input("Ingrese el grado del estudiante: ")   #ingresar el grado del estudiante 
colegio_estudiante = input("ingrese el nombre del colegio:")   #ingresar el nombre de el colegio 
años_estudiante = input("Ingrese la edad del estudiante:17:")   #ingrese la edad del estudiante 
materiafavorita_estudiante = input("Ingrese la materia favorita del estudiante") #ingresa la materia favorita del estudiante 

asignaturas = []  #lista vacia para las asignaturas 
notas = []    #lista vacia para las notas
 
for i in range(4): #el rango es de 4 bimestres 
    asignatura = input(f"Ingrese el nombre de la materia {i+1}: ") #ingresar el nombre de la materia 
    nota = float(input(f"Ingrese la nota para {asignatura}: "))   #ingresar la nota para la asignatura
    asignaturas.append(asignatura)   #agrega la lista de la asignatura 
    notas.append(nota)     
 
# valida las notas para ver si aprobo o no n
aprobadas = []   #lista vacia para ver si aprobo 
reprobadas = [] #lista vacia para ver las que reprobo
 
for i in range(len(notas)):  #el rango de las notas 
    if notas[i] >= 60:   #si la nota es mayor o igual a 60 aprobo la materia 
        aprobadas.append(asignaturas[i]) #llama a la variable de las aprobadas 
    else:    
        reprobadas.append(asignaturas[i])  #muestra si reprobo la materia 
 
# mostr4ar en pantalla las materias aprobadas y reprobadas 
print("\nMaterias aprobadas:")  #muestra en pantalla si la materia fue aprobada
for materia in aprobadas:  #bucle en la smaterais aprobadas 
    print(materia)    #imprimir la materia que fue aprobada 
 
print("\nMaterias reprobadas:")  #muestra las materias reprobadas 
for materia in reprobadas:  #bucle de la smaterais reprobadas 
    print(materia)   #muestra la materia que fue aprobada 
 
# Verificar si tiene derecho a recuperación o debe recursar el año
if len(reprobadas) <= 2:  #si las materias reprobadas son menores a 2 
    print("\nTiene derecho a recuperación.")    #tiene derecho a recuperacion
elif len(reprobadas) > 2:  #si las materias reprobadas fueron mas de 2 
    print("\nDebe recursar el año.")  #no tiene derecho a recuperacion y necesita recursar el año  