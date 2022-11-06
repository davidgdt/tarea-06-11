
print("\n\n")

class Producto:
  def __init__(self, codigo, nombre, precio, tipo):
    print("El producto se ha creado con éxito\n")
    self.codigo= codigo
    self.nombre= nombre
    self.precio= precio
    self.tipo = tipo

  def __str__(self):
    return "El código de el/la {1} es {0}, su precio es de {2}$ y es {3}".format(self.codigo, self.nombre, self.precio, self.tipo)


producto1=Producto(71864527, "pera", 1, "comida")
print(producto1)

print("\n\n")

producto2=Producto(7823498, "falda", 15, "vestimenta")
print(producto2)

print("\n\n")

producto3=Producto(2674612678, "movil", 700, "electrónica")
print(producto3)
