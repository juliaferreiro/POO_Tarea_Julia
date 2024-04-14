from Eventos import Evento
class TrabajoPractico(Evento):
    def __init__(self, fecha, descripcion, materia):
        super().__init__ (fecha, descripcion)
        self.materia = materia
    def __str__(self):
        return f"Trabajo práctico de: {self.materia} Descripción: {self.descripcion} fecha: {self.fecha}"

#Creo las clases hijas con sus correspondientes atributos y metodos.