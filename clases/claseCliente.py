class Cliente:
    def _init_(self, ruc, nom, direc, tel, mail, est=True):
        self.ruc=ruc
        self.nombre=nom
        self.direccion=direc
        self.telefono=tel
        self.email=mail
        self.estado=est
    
    def mostrarCliente(self):
        return " {} - {} - {} - {} - {} ".format(self.ruc, self.direccion, 
        self.telefono, self.email)

# cli1 = Cliente('034',  'Milagro', '0999239999', 'Barcelona16@gmail.com')
# print(cli1.mostrarCliente())