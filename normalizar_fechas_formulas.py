

#%%

def normalizar_fechas(fecha, patron_entrada,patron_salida='%d-%m-%Y'):
    from datetime import datetime as dt
    objeto_fecha = dt.strptime(fecha , patron_entrada)
    fecha_normalizada = dt.strftime(objeto_fecha, '%d-%m-%Y')
    print(fecha,'-->', objeto_fecha,'-->', fecha_normalizada)
    
def traductor_de_fecha(fecha):
    from datetime import datetime as dt
    mes=['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO','AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE', 'DICIEMBRE']
    lista  = fecha9.split('/')
    mes = lista[1].upper()
    nro_mes= mes.index(mes)+1
    fecha_aux = lista[0]+'/'+str(nro_mes)+'/'+lista[2]
    return fecha_aux