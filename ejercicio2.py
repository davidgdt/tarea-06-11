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

  
  def __str__(self):
    return "{}, ha sacado un: {}".format(self.nombre, self.nota)


alumno1=Alumno("david", 7)
print(alumno1)
calificacion= alumno1.calificacion()

alumno2=Alumno("paco", 1)
print(alumno2)
calificacion= alumno2.calificacion()
