from particulas import Particula

class Lista:

    def __init__ (self):
            self.__Lista = []

    def agregar_final(self, particulas:Particula ):
            self.__Lista.append(particulas)
        
     
    def agregar_inicio(self, particulas:Particula ):
            self.__Lista.insert(0, particulas)
            

    def mostrar(self):
            for particulas in self.__Lista:
                print(particulas)


l92 = Particula(id=10,origen_x=5,origen_y=45,destino_x=2,destino_y=16,velocidad=100,red=23,green=3,blue=5)
l01 = Particula(14,34,29,98,67,56,23,6,7)
almacen=Lista()

almacen.agregar_final(l92)


almacen.mostrar()

