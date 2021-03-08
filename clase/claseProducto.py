from claseMarca import Marca
from claseGrupo import Grupo
class Producto:
    def __init__(self, codigo=0, des="", pre=1, sto=1, marc= None, gru= None, est= True):
        self.id=codigo
        self.descripcion=des
        self.precio=pre
        self.stock=sto
        self.marca=marc
        self.grupo=gru 
        self.estado=est 

    def mostrarProducto(self):
        return " {} - {} - {} - {} - {} - {} - {} ".format(self.id, self.descripcion, self.precio, 
        self.stock, self.marca.descripcion, self.grupo.descripcion, self.estado)
    
    # def listaProducto(self):
    #    grupo1 = Grupo(1, "Embutidos", True)
    #    grupo2 = Grupo(2, "Lacteos", True)
    #    grupo3 = Grupo(3, "Colas", True)
    #    grupos = [grupo1, grupo2, grupo3]
    #    marca1 = Marca(1, "Plumrose", True)
    #    marca2 = Marca(2, "La Lechera", True)
    #    marca3 = Marca(3, "Coca Cola", True)
    #    marcas = [marca1, marca2, marca3]
    #    productos = []
    #    for i in range (0,3):
    #     nombre = input("Ingrese producto: ")
    #     precio = input("Ingrese precio: ")
    #     stock = input("Ingrese stock disponible: ")
    #     producto = Producto(i, nombre, precio, stock, grupos[i], marcas[i], True)
    #     productos.append(producto)
    #    return productos