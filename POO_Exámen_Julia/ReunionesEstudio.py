from Eventos import Evento

class ReunionEstudio(Evento):
    def __init__(self, fecha, descripcion, materia):
        super().__init__ (fecha, descripcion)
        self.materia = materia
    def __str__(self, descripción, materia) -> str:  
        pass
    
#Creo las clases hijas con sus correspondientes atributos y metodos.
        