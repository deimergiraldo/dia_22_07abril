from datetime import datetime, date


RUTA = "1.txt"

#estoy abriendo el documento y en caso de que no exista se crea, en este ejemplo voy a crearlo
with open(RUTA, "a+") as fichero_fecha:
  fecha_actual = datetime.now()
  if fichero_fecha.tell():
    fichero_fecha.seek(0)
    fecha = datetime.strptime(next(fichero_fecha).rstrip(), "%Y/%m/%d")
    cont = int(next(fichero_fecha).split(".")[0])
    #En está parte estoy diciendo que si la diferencia en días es mayor a dos que actualice que fecha antigua a la fecha del momento 
    if (fecha_actual - fecha).days > 2: 
      fichero_fecha.seek(0)
      fichero_fecha.truncate()
      fichero_fecha.write(f'{fecha_actual.strftime("%Y/%m/%d")}\n{cont + 1}.txt\n')
  
  #En caso de que la fecha sea menos a dos días escribir
  else:
    fichero_fecha.write(f'{fecha_actual.strftime("%Y/%m/%d")}\n1.txt\n')


#Ejemplo 2
import openpyxl
import datetime
import datetime as dt

horas=openpyxl.load_workbook('Minuevoarchivo.xlsx')

columna=horas.active

#Estoy guardando el momento de inicio
inicio = datetime.datetime.now()

#inserto dos fechas y le calculo la diferencia, por sierto esa diferencia estará en horas
hoy=dt.datetime(2021,4,6,)
micumple = dt.datetime(1999,5,10)
diferencia=hoy - micumple

#Inserto esa diferencia en la columna D del documento de excel
columna['D1']='Diferencia de fechas'
for i in range(2,5):
  columna[f'D{i}']=diferencia

#Aquí guardo el momento en que termina
fin = datetime.datetime.now()

duracion = fin - inicio

#concateno dos celdas y luego inserto los datos de inicio, fin y tiempo que duro la ejecución de los algoritmos anteriores
columna.merge_cells('E1:F1')
columna['E1']='tiempo de ejecución de fechas'
columna['E2']='Inicio'
columna['F2']=inicio
columna['E3']='Fin'
columna['F3']=fin
columna['E4']='Duración'
columna['F4']=duracion

#Guardo todo en un nuevo documento y listo
horas.save('Ejecucion_tiempo.xlsx')
