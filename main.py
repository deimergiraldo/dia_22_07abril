from datetime import datetime, date


RUTA = "1.txt"

with open(RUTA, "a+") as fichero_fecha:
  fecha_actual = datetime.now()
  if fichero_fecha.tell():
    fichero_fecha.seek(0)
    fecha = datetime.strptime(next(fichero_fecha).rstrip(), "%Y/%m/%d")
    cont = int(next(fichero_fecha).split(".")[0])
    if (fecha_actual - fecha).days > 2:
      fichero_fecha.seek(0)
      fichero_fecha.truncate()
      fichero_fecha.write(f'{fecha_actual.strftime("%Y/%m/%d")}\n{cont + 1}.txt\n')
  else:
    fichero_fecha.write(f'{fecha_actual.strftime("%Y/%m/%d")}\n1.txt\n')


#Ejemplo 2

