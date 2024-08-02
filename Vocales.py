#Pide al usuario una palabra
palabra = input("Ingrese la palabra: ").lower() #Convertir la palabra a minúsculas

#Inicializa contadores para cada vocal
contador_a = contador_e = contador_i = contador_o = contador_u = 0

#Recorre cada caracter de la palabra
for letra in palabra:
    if letra == 'a': #Verifica el caracter actual que es igual a letra a
        contador_a += 1 #Incrementa el valor

print(f"Palabra ingresada: {palabra}") #Muestra la palabra ingresada
#Muestra resultados
print(f"Número de veces que aparece la vocal 'a': {contador_a}")
