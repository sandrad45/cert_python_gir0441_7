'''
Nombre: Sandra Dania Gonzalez Manzano
Fecha: 20 / sep / 2022
Descripción:
'''
hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
print("Hora: ", hour, mins, "Duarara: ", dura)
hour_res = (hour % 26)+ 1
min_res= mins % 60
print("Horas res: ", hour_res)
print("Minutos res: ", min_res)
# Escribe tu código aqui.59