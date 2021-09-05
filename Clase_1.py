#Abrir un txt

archivo = open('/Users/fernandogonella/Documents/Curso Eant/Data/frutas.txt','r', encoding='utf-8')

for i in archivo:
    #linea = i.strip('\n')
    #linea = i.replace('\n','')
    linea = i[:-1]
    
    print(linea)
    
#El print por defecto tiene salto de linea al final 

archivo.close() #Cerrar el archivo 

#%%

archivo2 = open('/Users/fernandogonella/Documents/Curso Eant/Data/subtes.csv','r', encoding='utf-8')

for linea in archivo2: 
    linea = linea[:-1] # saco el salto de linea
    lista = linea.split(',') #divido las comas, perod devuelve lista
    
    
    print (lista[2])
    

archivo.close()

#%%

archivo_in = open('/Users/fernandogonella/Documents/Curso Eant/Data/subtes.csv','r', encoding='utf-8')

archivo_out = open('/Users/fernandogonella/Documents/Curso Eant/Data/subtes_salida.csv','w', encoding='utf-8')

for linea in archivo_in: 
    linea = linea[:-1] # saco el salto de linea
    lista = linea.split(',') #divido las comas, perod devuelve lista
    
    archivo_out.write(lista[1]+','+ lista[0]+','+ lista[2]+'\n')
    
archivo_in.close()
archivo_out.close() # hay q ponerlo

#%%

archivo_in2 = open('/Users/fernandogonella/Documents/Curso Eant/Data/peliculas.csv','r', encoding='utf-8')

for linea in archivo_in2: 
    linea = linea[:-1] # saco el salto de linea
    lista = linea.split(',') #divido las comas, perod devuelve lista
    print(lista)
    

    
#%%
# Uso la libreria nativa de Python CSV

import csv 

archivo_in3 = open('/Users/fernandogonella/Documents/Curso Eant/Data/peliculas.csv','r', encoding='utf-8')

archivo_out3 = open('/Users/fernandogonella/Documents/Curso Eant/Data/peliculas_salida.csv','w', encoding='utf-8')

tabla = csv.reader(archivo_in3, delimiter=',')


archivo_out3.write('titulo,director,ano\n')

for i in tabla:
    fila = ','.join([i[0],i[2],i[1]])
    archivo_out3.write(fila + '\n')
 
    
    
archivo_in3.close()
archivo_out3.close()























