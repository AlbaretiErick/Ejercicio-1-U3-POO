import csv
class Carrera:
    __codigo = None
    __nombre = None
    __fechaDeInicio = None
    __duracion = None
    __titulo = None
    def __init__ (self, codigo, nombre, fechaInicio, duracion, titulo):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__fechaDeInicio = fechaInicio
        self.__duracion = duracion
        self.__titulo = titulo
    def getNombre (self):
        return self.__nombre
    def getCodigo (self):
        return self.__codigo
    def mostrarA (self):
        print ('Carrera:', self.__nombre, '/ Duracion:', self.__duracion)

class Facultad:
    __codigo = None
    __nombre = str
    __direccion = str
    __localidad = str
    __telefono = str
    __carreras = []
    def __init__(self, codigo, nombre, direccion, localidad, telefono):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__direccion = direccion
        self.__localidad = localidad
        self.__telefono = telefono
    def setCarrera (self, dato1, dato2, dato3, dato4, dato5):
        carrera = Carrera (dato1, dato2, dato3, dato4, dato5)
        self.__carreras.append (carrera)
    def getCodigo (self):
        return self.__codigo
    def getNombre (self):
        return self.__nombre
    def mostrarCarrerasA (self):
        for carrera in self.__carreras:
            carrera.mostrarA()
    def buscarCarrera (self, nombC):
        bul = False
        i = 0
        while i<len (self.__carreras) and nombC!=self.__carreras[i].getNombre():
            i += 1
        if i<len (self.__carreras):
            print ('Codigo de carrera:', self.__carreras[i].getCodigo(), '\nNombre de la facultad:', self.__nombre, '\nLocalidad:', self.__localidad)
            bul = True
        return bul

class ManejaFacultades:
    def __init__ (self):
        self.__facultades = []
    def agregarFacultad (self, facu):
        self.__facultades.append (facu)
    def testFcultades (self):
        archivo = open ("Facultades.csv")
        reader = csv.reader (archivo, delimiter=',')
        for linea in reader:
            bul = '.' in linea[0]
            if bul == False:
                datos = Facultad (linea[0], linea[1], linea[2], linea[3], linea[4])
                self.agregarFacultad (datos)
            else:
                i = int (float (linea[0]))
                self.__facultades[i-1].setCarrera (linea[0], linea[1], linea[2], linea[3], linea[4])
        archivo.close()
    def mostrar1 (self, code):
        i = 0
        while i<len (self.__facultades) and self.__facultades[i].getCodigo()!=code:
            i += 1
        if i<len (self.__facultades):
            print ('Facultad:', self.__facultades[i].getNombre())
            self.__facultades[i].mostrarCarrerasA()
        else:
            print ('No se encontro una facultad con el codigo ingresado.')
    def mostrar2 (self, nombC):
        bul = False
        i = 0
        while i<len (self.__facultades) and bul==False:
            bul = self.__facultades[i].buscarCarrera (nombC)
            i += 1
        if i>=len (self.__facultades):
            print ('No se encontro la carrera buscada.')


class Menu:
    __switcher = None
    def __init__ (self):
        self.__switcher = {'a': self.opcionA,
                           'b': self.opcionB}
    def opcion (self, op, manejador):
        funcion = self.__switcher.get (op)
        if op=='a' or op=='b':
            funcion (manejador)
        else:
            print ('La opcion ingresada no existe.')
    def opcionA (self, manejador):
        cod = input ('Ingrese el codigo de una facultad: ')
        manejador.mostrar1 (cod)
    def opcionB (self, manejador):
        nombreCarrera = input ('Ingrese el nombre de una carrera: ')
        manejador.mostrar2 (nombreCarrera)