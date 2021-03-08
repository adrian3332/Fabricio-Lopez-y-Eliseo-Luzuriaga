from claseMarca import Marca
from claseGrupo import Grupo
from claseProducto import Producto
from claseDetVenta import DetVenta
from claseCliente import Cliente
class Venta:
    def _init_(self, fact, fech, clien, sub, iva, total, det, est=True):
        self.factura=fact
        self.fecha=fech
        self.cliente=clien
        self.subtotal=sub
        self.iva=iva
        self.total=total
        self.detalle=det
        self.estado=est
    
    def mostrarVenta(self):
        return [self.factura,
        self.fecha,
        self.cliente,
        self.subtotal,
        self.iva,
        self.total,
        self.detalle,
        self.estado]

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
detalle = [det1, det2, det3]
cli1 = Cliente('034',  'Milagro', '0999239999', 'Barcelona16@gmail.com')
venta1 = Venta('F01', '07/03/2021', cli1, 20, 2, 22, detalle)
datosVenta = venta1.mostrarVenta()
print("Datos de la factura")
print(datosVenta[0], datosVenta[1], datosVenta[2].nombre, datosVenta[5])
for det in datosVenta[6]:
  print(det.mostrarDetalle()