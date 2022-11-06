class Alumno:
  def __init__(self, nombre, nota):
    self.nombre= nombre
    self.nota= nota
    print("El alumno se ha creado con éxito\n")
  
  def calificacion(self):
    if self.nota>=5:
      print(self.nombre, "ha aprobado\n\n")
    else:
      print(self.nombre, "ha suspendido\n\n")
