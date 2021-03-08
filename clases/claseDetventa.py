from claseMarca import Marca
from claseGrupo import Grupo
from claseProducto import Producto
class DetVenta:
    def _init_(self, id, produc, prec=0, cant=0):
        self.id=id
        self.producto=produc
        self.precio=produc.precio
        self.cantidad=cant
    
    def mostrarDetVenta(self):
        return " {} - {} - {} - {}  ".format(self.id, self.producto.descripcion, 
        self.producto.precio, self.cantidad)

grupo1 = Grupo(1, "Embutidos", True)
grupo2 = Grupo(2, "Lacteos", True)
grupo3 = Grupo(3, "Colas", True)
grupos = [grupo1, grupo2, grupo3]
marca1 = Marca(1, "Plumrose", True)
marca2 = Marca(2, "La Lechera", True)
marca3 = Marca(3, "Coca Cola", True)
marcas = [marca1, marca2, marca3]
productos = []
for i in range (0,3):
  nombre = input("Coloque el producto: ")
  precio = input("Coloque el precio: ")
  stock = input("Coloque el stock disponible: ")
  producto = Producto(i, nombre, precio, stock, grupos[i], marcas[i], True)
  productos.append(producto)

prods = Producto()
det1 = DetVenta(1, productos[0], 0, 5)
det2 = DetVenta(2, productos[1], 0, 15)
det3 = DetVenta(3, productos[2], 0, 10)
print(det1.mostrarDetVenta())
print(det2.mostrarDetVenta())
print(det3.mostrarDetVenta())