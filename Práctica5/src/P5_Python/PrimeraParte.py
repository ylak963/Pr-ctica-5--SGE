# coding: utf-8
'''
Created on 23 feb. 2021
@author: Miguel Angel
'''
import random
from statistics import  mean, variance

#Creamos las listas donde guardaremos los datos
a = []
b = []
c = []
d = []
e = []

#Se crean 1000 registros y se rellenan las listas con un valor que este comprendido entre 
for i in range(1000):
    a.append(random.randrange(100)) #Con append añadimos el contenido
    b.append(random.randrange(100))
    c.append(random.randrange(100))
    d.append(random.randrange(100))
    e.append(random.randrange(100))

#Comprobación
#print(f"La lista a es {str(a)} ")
#print(f"La lista b es {str(b)} ")
#print(f"La lista c es {str(c)} ")
#print(f"La lista d es {str(d)} ")
#print(f"La lista e es {str(e)} ")

#Prueba con diccionario
#diccionario = {"A": 0, "B": 0, "C": 0, "D":0, "E":0}
#print(diccionario.items())
    
#Preguntar por el nombre de un fichero que queremos generar
fichero = input("Introduzca el nombre del fichero: ")
print("El fichero "+ fichero + " se ha creado correctamente")

try: #Usamos try y except para el control de errores que podría provocar el tema de ficheros
    f = open(fichero+".txt","w")#Abrimos el fichero con permisos de escritura
    f.write("A -- B -- C -- D -- E \n") #Creamos la cabecera del fichero
    for i in range(1000): #Generamos con el for y el rango el número de registros
        datos = f"{str(a[i])} - {str(b[i])} - {str(c[i])} - {str(d[i])} - {str(e[i])}"   
        f.write(datos+ "\n") 
except Exception:
    exit()
f.close()

#Guardamos en las variables la media de cada lista(propiedad), gracias al módulo statistics
media1 = mean(a)
media2 = mean(b)
media3 = mean(c)
media4 = mean(d)
media5 = mean(e)

#Guardamos en las variables la moda de cada lista(propiedad), gracias al módulo statistics
moda1=[]
moda2=[]
moda3=[]
moda4=[]
moda5=[]

#Calculamos la moda de cada característica
aAux = 0
for i in a:
    j = a.count(i) #count se utiliza para el contar el nº de veces que un elemento aparece en la lista, y lo guardamos en la variable j
    if j > aAux:
        aAux = j

    for i in a:
        j = a.count(i)
        if j == aAux and i not in moda1:
            moda1.append(i)
           
bAux = 0
for i in b:
    j = b.count(i)
    if j > bAux:
        bAux = j

    for i in b:
        j = b.count(i)
        if j == bAux and i not in moda2:
            moda2.append(i)      
          
cAux = 0
for i in c:
    j = c.count(i)
    if j > cAux:
        cAux = j

    for i in c:
        j = c.count(i)
        if j == cAux and i not in moda3:
            moda3.append(i)
             
dAux = 0
for i in d:
    j = d.count(i)
    if j > dAux:
        dAux = j

    for i in d:
        j = d.count(i)
        if j == dAux and i not in moda4:
            moda4.append(i)
            
eAux = 0
for i in e:
    j = e.count(i)
    if j > eAux:
        eAux = j

    for i in d:
        j = e.count(i)
        if j == eAux and i not in moda5:
            moda5.append(i)   

#Guardamos en las variables la varianza de cada lista(propiedad), gracias al módulo statistics
varianza1 = variance(a)
varianza2 = variance(b)
varianza3 = variance(c)
varianza4 = variance(d)
varianza5 = variance(e)
#Guardamos en las variables el valor máximo de cada lista(propiedad)
max1 = max(a)
max2 = max(b)
max3 = max(c)
max4 = max(d)
max5 = max(e)
#Guardamos en las variables el valor mínimo de cada lista(propiedad)
min1 = min(a)
min2 = min(b)
min3 = min(c)
min4 = min(d)
min5 = min(e)

#Guardamos en las variables la media, moda, varianza,mínimo y máximo de las caracteristicas de cada lista, lo conseguimos gracias al formateo
media = f"{str(media1)} - {str(media2)} - {str(media3)} - {str(media4)} - {str(media5)}"
moda = f"A:{str(moda1)} - B:{str(moda2)} - C:{str(moda3)} - D:{str(moda4)} - E:{str(moda5)}"
varianza = f"{str(varianza1)} - {str(varianza2)} - {str(varianza3)} - {str(varianza4)} - {str(varianza5)}" 
minimo = f"{str(min1)} - {str(min2)} - {str(min3)} - {str(min4)} - {str(min5)}" 
maximo = f"{str(max1)} - {str(max2)} - {str(max3)} - {str(max4)} - {str(max5)}" 

#Pedimos el nombre de fichero a mostrar
ficheroMostrar = input("Introduzca el nombre del fichero que quieres consultar: ")
try:
    file = open(ficheroMostrar+".txt","r")  #abrimos el txt con permisos de lectura
    print("Caracteristicas: A -- B -- C -- D -- E \n") #cabecera
    print("Media:"+media)
    print("Moda:"+moda)
    print("Varianza:"+varianza)
    print("Mínimo:"+minimo)
    print("Máximo"+maximo)
except Exception:
    exit()
file.close()
 


