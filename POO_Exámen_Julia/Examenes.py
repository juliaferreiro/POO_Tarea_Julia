from Eventos import Evento
class Examen(Evento):
    def __init__(self, fecha, descripcion, materia, complejidad):
        super().__init__ (fecha, descripcion)
        self.materia = materia
        self.complejidad = complejidad
    def __str__(self):
        return ("Trabajo práctico de ", self.materia, ": " , self.descripción, ", fecha:" , self.fecha)

#Creo las clases hijas con sus correspondientes atributos y metodos.
#Agrego un método str para que me devuelva el resultado como quiero.