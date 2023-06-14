from Clases import ManejaFacultades
from Clases import Menu
if __name__ == "__main__":
    manejador = ManejaFacultades()
    menu = Menu()
    manejador.testFcultades()
    opcion = input ('Seleccione:\na - Mostrar nombre de la facultad, nombre y duración de cada una de las carreras que se dictan en esa facultad.\nb - Mostrar código, nombre y localidad de la facultad donde esta se dicta.\nOpcion: ')
    menu.opcion (opcion, manejador)
    print ('Fin del Programa...')