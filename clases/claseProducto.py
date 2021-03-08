from claseMarca import Marca
from claseGrupo import Grupo
class Producto:
    def _init_(self, cod, des, pre, sto, marc, gru, est):
        self.id=cod
        self.descripcion=des
        self.precio=pre
        self.stock=sto
        self.marca=marc
        self.grupo=gru 
        self.estado=est 

    def mostrarProducto(self):
        return " {} - {} - {} - {} - {} - {} - {} ".format(self.id, self.descripcion, self.precio, 
        self.stock, self.marca.descripcion, self.grupo.descripcion, self.estado)

grupo1 = Grupo(1, "Embutidos", True)
grupo2 = Grupo(2, "Lacteos", True)
grupos = [grupo1, grupo2]
marca1 = Marca(1, "Plumrose", True)
marca2 = Marca(2, "La Lechera", True)
marcas = [marca1, marca2]
numeros = [2, 4]
print(numeros[0], marcas[0].mostrarMarca())

productos = []
for i in range (0,2):
    nombre = input("Coloque el producto: ")
    precio = input("Coloque el precio: ")
    stock = input("Coloque el stock disponible: ")
    producto = Producto(i, nombre, precio, stock, grupos[i], marcas[i], True)
    productos.append(producto)

print("Id Descripción Estado")
for p in productos:
    print(p.mostrarProducto())
    print(grupo.mostrarProducto())