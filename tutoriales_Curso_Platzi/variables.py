print("""
-------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------
Una variable se debe pensar como una cajita o contenedor. Aloja un objeto u objetos.

La manera de crearlas es NombreDeVariable = ContenidoDeVariable

    colorDeRemera = 'amarillo'

Así creamos la variable colorDeRemera y el contenido es amarillo.

Nota: las comillas están ya que el contenido es texto.

Podemos ver el contenido de una variable de la siguiente manera

    print(colorDeRemera)
""")
colorDeRemera = 'amarillo'
print(colorDeRemera)

print("""
-------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------
En caso de que la variable que quiero crear sea numérica no hacen falta las comillas

    cantidadDeRemerasAmarillas = 15

Así creamos la variable cantidadDeRemerasAmarillas y el contenido es 15.

    print(cantidadDeRemerasAmarillas)""")
cantidadDeRemerasAmarillas = 15
print(cantidadDeRemerasAmarillas)

print("""
-------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------
También se pueden hacer operaciones con las variables ya que Python lee su contenido

    cantidadDeRemerasRojas = 10

Podemos sumar la cantidad de remeras amarillas y la cantidad de rojas de la siguiente
manera:

    cantidadDeRemerasAmarillas + cantidadDeRemerasRojas""")
cantidadDeRemerasRojas = 10
print(cantidadDeRemerasRojas + cantidadDeRemerasAmarillas)

print("""
-------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------
Se pueden crear variables de otras variables por ejemplo

    cantidadTotalDeRemeras = cantidadDeRemerasAmarillas + cantidadDeRemerasRojas

    print(cantidadTotalDeRemeras)
""")
cantidadTotalDeRemeras = cantidadDeRemerasAmarillas + cantidadDeRemerasRojas
print(cantidadTotalDeRemeras)

print("""
-------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------
Si se designa una variable nuevamente con otro contenido, el anterior se borra

    print(cantidadTotalDeRemeras)
""")
print(cantidadTotalDeRemeras)

print("""
    cantidadTotalDeRemeras = 90

    print(cantidadTotalDeRemeras)
""")
cantidadTotalDeRemeras = 90
print(cantidadTotalDeRemeras)

print("""
-------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------
Por ultimo el nombre de las variables no puede comenzar con un número 
y debe estar en minúsculas para buenas practicas.
Las palabras dentro de las variables se separan con guiones bajos.
-------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------
""")
