class Agenda:
     def __init__(self, listaEventos):
        self.listaEventos = []

     def agregar (self, evento):
         self.listaEventos.append(evento)

     def mostrar_eventos (self, evento):
        for evento in self.listaEventos:
            print(evento)

     def eliminar (self, evento, eventoSeleccionado):
         for evento in self.listaEventos:
            if evento == eventoSeleccionado:
                self.listaEvento.remove(evento)