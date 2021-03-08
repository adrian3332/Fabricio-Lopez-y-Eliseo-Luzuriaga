class Grupo:
    def __init__(self, codigo, des, est):
        self.id=codigo
        self.descripcion=des
        self.estado=est
    
    def mostrarGrupo(self):
        return " {} - {} - {} ".format(self.id, self.descripcion, self.estado)

# grupos = []
# for i in range (1,6):
#     nombre = input("Ingrese grupo: ")
#     grupo = Grupo(i, nombre, True)
#     grupos.append(grupo)
# print("Id Descripción Estado")
# for grupo in grupos:
#     print(grupo.mostrarGrupo())