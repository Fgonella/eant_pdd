#%%

#Abrir, escribir cvs libreria

import csv

#El with es usado aca
#Newline es para que no te agregue un salto de linea mas 

with open('peliculas.csv',encoding='utf-8') as archivo_in, open('peliculas_salida2.csv', 'w', encoding='utf-8', newline='') as archivo_out:
    entrada = csv.reader(archivo_in)
    salida = csv.writer(archivo_out, delimiter=';')
    salida.writerow(['Titulo','Director','ANO'])
    for linea in entrada:
        salida.writerow([linea[0],linea[2],linea[1]])
        

#%% Normalizar la infomacion

#Arrancamos con las fechas Normalizamos fechas 


from datetime import datetime as dt

fecha = '12/2/2019'

objeto_fecha = dt.strptime(fecha , '%d/%m/%Y')
print(objeto_fecha)
fecha_normalizada = dt.strftime(objeto_fecha, '%d-%m-%Y')
print(fecha_normalizada)

#%%

def normalizar_fechas(fecha, patron_entrada,patron_salida='%d-%m-%Y'):
    objeto_fecha = dt.strptime(fecha , patron_entrada)
    fecha_normalizada = dt.strftime(objeto_fecha, '%d-%m-%Y')
    print(fecha,'-->', objeto_fecha,'-->', fecha_normalizada)
    
def traductor_de_fecha(fecha):
    mes=['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO','AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE', 'DICIEMBRE']
    lista  = fecha9.split('/')
    mes = lista[1].upper()
    nro_mes= mes.index(mes)+1
    fecha_aux = lista[0]+'/'+str(nro_mes)+'/'+lista[2]
    return fecha_aux
    
    

fecha1 = "13/2/2019"
fecha2 = "2/13/2019"
fecha3 = "02/19" 
fecha4 = "20191302"
fecha5 = "2019-13-02 14:23:33"
fecha6 = "13/Feb/2019"
fecha7 = "13/February/2019"
fecha8 = "13 days after February 2019"
fecha9 = "13/Febrero/2019"


normalizar_fechas(fecha2, '%m/%d/%Y')
normalizar_fechas(fecha3, '%m/%y')
normalizar_fechas(fecha4, '%Y%d%m')
normalizar_fechas(fecha5, '%Y-%d-%m %H:%M:%S')
normalizar_fechas(fecha6, '%d/%b/%Y')
normalizar_fechas(fecha7, '%d/%B/%Y')
normalizar_fechas(fecha8, '%d days after %B %Y')


mes= ['ENERO','FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO','JULIO','AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE', 'DICIEMBRE']
fecha9 = "13/Febrero/2019"
lista  = fecha9.split('/')
mes = lista[1].upper()
nro_mes= mes.index(mes)+1
fecha_aux = lista[0]+'/'+str(nro_mes)+'/'+lista[2]

normalizar_fechas(fecha_aux,'%d/%m/%Y')

import normalizar_fechas_formulas as nf

nf.normalizar_fechas(fecha2, '%m/%d/%Y')

#%%

# MANEJOR DE EXCEPCIONES

a = 5

try:
    resultado = 'resulrado:'+ a
    print(resultado)
except:
    print('No funciona la cosa')


#Aplicamos un ejemplpo con la fecha

fecha = '13/2/2019'

try :
    nf.normalizar_fechas(fecha, '%d-%m-%Y')
except:
    try:
       nf. normalizar_fechas(fecha, '%d/%m/%Y')
    except:
        print('No funciono')

nf.normalizar_fechas(fecha, '%d/%m/%Y')

#%% Bajando data de Buenos aires Data


import csv 

with open('/Users/fernandogonella/Documents/Curso Eant/Data/hospitales.csv', 'r', encoding='utf-8') as archivo_in, open('hospitales_out.cvs', 'w', encoding='utf-8', newline='',) as archivo_out:
    entrada = csv.reader(archivo_in)
    salida = csv.writer(archivo_out, delimiter=',')
    salida.writerow(['Latitud','Longitud','Direccion', 'Nombre'])
    for linea in archivo_in:
        salida.writerow([linea])
                         















