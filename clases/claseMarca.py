class Marca:
    def _init_(self, cod, des, est):
        self.id=cod
        self.descripcion=des
        self.estado=est
    
    def mostrarMarca(self):
        return " {} - {} - {} ".format(self.id, self.descripcion, self.estado)

mar1 = Marca("1", "Plumrose", True)
mar2 = Marca("2", "Iberica", True)
resp = mar1.mostrarMarca()
print (resp)
print (mar2.mostrarMarca())
marcas = []
for i in range (1,6):
    nombre = input("Coloque el marca: ")
    marca = Marca(i, nombre, True)
    marcas.append(marca)
listas=[2, 4, 6, 8, 10]
for num in listas:
    print(num)
print("Id Descripción Estado")
