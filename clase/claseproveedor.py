class Cliente:
    def __init__(self, ruc, nom, direc, tel, mail, est=True):
        self.ruc=ruc
        self.nombre=nom
        self.direccion=direc
        self.telefono=tel
        self.email=mail
        self.estado=est
    
    def mostrarCliente(self):
        return " {} - {} - {} - {} - {} ".format(self.ruc,  self.direccion, 
        self.telefono, self.email)

cli1 = Cliente('0914',  'Milagro', '0925987144', 'ejemplo@hotmail.com')
print(cli1.mostrarCliente())

# mar1 = Marca("1", "Plumrose", True)
# mar2 = Marca("2", "Iberica", True)
# resp = mar1.mostrarMarca()
# print (resp)
# print (mar2.mostrarMarca())
# marcas = []
# for i in range (1,6):
#     nombre = input("Ingrese marca: ")
#     marca = Marca(i, nombre, True)
#     marcas.append(marca)
# listas=[2, 4, 6, 8, 10]
# for num in listas:
#     print(num)
# print("Id Descripción Estado")
# for marca in marcas:
#     print(marca.mostrarMarca())