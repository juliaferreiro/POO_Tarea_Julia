class Agenda:
     def __init__(self):
        self.listaEventos = []

     def agregar (self, Evento):
         self.listaEventos.append(Evento)

     def mostrar_eventos (self):
        for evento in self.listaEventos:
            print(evento)

     def eliminar (self, Evento):
         for evento in self.listaEventos:
            if evento.fecha == Evento.fecha and evento.descripcion == Evento.descripcion:
                self.listaEventos.remove(evento)
                print(f"Se eliminó el evento {evento.descripcion} del día {evento.fecha}")

     def mostrar_fecha_descripcion (self):
         for evento in self.listaEventos:
            print (f"Esta es la fechas del evento: {evento.fecha} y esta es su descripción {evento.descripcion}")