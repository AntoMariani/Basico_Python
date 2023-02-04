import random
import sys, time, os


def log_cat():
    imprimir("""
     /\-/\\
    /a a  \         El gato te apoya en lo que decidas                        
   =\ Y  =/-~~~~~~-,_______________________/ )
     '^--'          ________________________/
       \           /
       ||  |---'\  \  
      (_(__|   ((__|  
    """)


def generate_exercice_list(cant_ejs,unidades):

    diccionario_unidades = \
        {1: set(list(range(1,16))),\
        2: set(list(range(1,15))),\
        3: set(list(range(1,47))),\
        4: set(list(range(1,10))),\
        5: set(list(range(1,7))),\
        6: set(list(range(1,45))),\
        7: set(list(range(1,77))),\
        8: set(list(range(1,37))),\
        9: set(list(range(1,40))),\
        10: set(list(range(1,38)))}

    imprimir("Acá te van los ejercicios:\n")
    #for unidad in unidades:
        #imprimir("UNIDAD " + str(unidad) + ": EJERCICIO: " + str(random.sample(list(diccionario_unidades[unidad]),cant_ejs)) + "\n")
        
    {imprimir("UNIDAD " + str(unidad) + ": EJERCICIO: " + str(random.sample(list(diccionario_unidades[unidad]),cant_ejs)) + "\n") for unidad in unidades}


def imprimir(mensaje):
    for char in mensaje:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.00001)

def borrar_pantallita():
    os.system("cls")

if __name__ == "__main__":
    borrar_pantallita()
    metodo_dict = \
        {1: ["Todas las unidades",range(1,11)],\
        2: ["Primer Parcial (U1-U5)",range(1,6)], \
        3: ["Segundo Parcial (U6-U10)",range(6,11)], \
        4: ["Tus propias unidad/es"], \
        5: ""}

    while True:
        ############ UNIDADES
        imprimir("""####¿Qué querés estudiar hoy?#### \n
            1) Todas las unidades \n\
            2) Primer Parcial (U1-U5) \n\
            3) Segundo Parcial (U6-U10)\n\
            4) Introducir unidad/es a mano\n\
            5) Mejor no quiero hacer nada :/\n""")

        metodo = input()
        if int(metodo) not in metodo_dict:
            os.system("cls")
            imprimir("""
            # OPCIÓN INCORRECTA CAPO # \n
            # es del 1 al 4 y enter # \n
            # VAMOS DE NUEVO # \n\n """)
            continue

        borrar_pantallita()

        if int(metodo) in range(1,4):
            rango = list(metodo_dict[int(metodo)][1])
        elif int(metodo) == 5:
            log_cat()
            quit()
        else:
            imprimir("Escribí las unidades separadas por espacio nomás :P: \n")
            rango_string = input()
            rango_string = rango_string.split()
            ##list_comprehension, convierte todos los items de una lista a int
            rango = [int(x) for x in rango_string]            

        ################ CANTIDAD DE EJERCICIOS
        imprimir("¿Cuántos ejercicios de cada unidad querés hacer?\n")
        cant_ejs = input()
        borrar_pantallita()
        if not cant_ejs.isnumeric():
            os.system("cls")
            imprimir("""
            # OPCIÓN INCORRECTA CAPO # \n\
            # es numérico el tema # \n\
            # VAMOS DE NUEVO # \n\n """)
            continue
        elif int(cant_ejs) > 6:
            imprimir("""
            Del 1 al 6 capo que todavía no ta tan debuggeado el codigo\n\
            ...\n\
            Y la idea es que no te quemes, andá de a poco D: \
            ...\n""")
            time.sleep(3)
            borrar_pantallita()
            continue
        imprimir("Muy bien!!!!! Elegiste para estudiar: " + str(metodo_dict[int(metodo)][0]) + "\n")
        imprimir("Y vas a hacer: " + cant_ejs + " ejercicios por unidad :D\n\n")

        break

    generate_exercice_list(int(cant_ejs),rango)
