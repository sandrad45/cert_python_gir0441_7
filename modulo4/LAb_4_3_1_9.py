'''
Nombre: Sandra Dania Gonzalez Manzano 
Fecha:  04 / Oct /2022
Descripción: 

    Proyectar y escribir funciones con parámetros.
    Utilizar la sentencia return.
    Construir un conjunto de funciones de utilidad.
    Utilizar las funciones propias del estudiante.


'''
def isPrincipal (num):
 for i in range (2, int, (1 + num ** 0.5)):
        if num % i == 0:
          return False
          return True
    
 for i in range (1, 20):
       if isPrincipal (i + 1):
        print (i + 1, end = " ")
print ()
