from Eventos import Evento
from Examenes import Examen
from ReunionesEstudio import ReunionEstudio
from TrabajosPracticos import TrabajoPractico
from Agendas import Agenda
#Importo la clase evento
Evento1 = Evento("", "")
agenda = Agenda()
#Creo dos objetos vacío
print("Bienvenido a la agenda")
hacer = int(input("Ingresa que quieres hacer, 1 para agregar, 2 para mostrar, 3 para eliminar y 4 para salir "))
while hacer < 4:
   
    if hacer == 1:
        print("pulse 1 para Exámenes, 2 para reuniones de estudio y 3 para trabajos prácticos")
        opcion = int(input("Indica que tipo de evento querés agregar " ))
        materiaEvento = str(input("Ingresa la materia "))
        descripcionEvento = str(input("Ingresa una breve descripción "))
        fechaEvento = str(input("Ingresa la fecha "))

        if opcion == 1:
            complejidadEvento = str(input("Ingresa la dicultad del exámen del uno al 10 "))
            Evento1 = Examen(fechaEvento, descripcionEvento, materiaEvento, complejidadEvento)
        if opcion == 2:
            Evento1 = ReunionEstudio(fechaEvento, descripcionEvento, materiaEvento)
        if opcion == 3:
            Evento1 = TrabajoPractico(fechaEvento, descripcionEvento, materiaEvento)       
        agenda.agregar(Evento1)
        #Pido los datos y dependiendo de que tipo de evento crea creo un objeto en una clase diferente con los
        #atributos siendo completados con las variables.
        
    if hacer == 2: 
        agenda.mostrar_eventos()

    if hacer == 3:
        agenda.mostrar_fecha_descripcion()
        eventoSeleccionadoFecha = str(input("Ingresa la fecha del evento que queres eliminar "))
        eventoSeleccionadoDescripcion = str(input("Ingresa la descripcion del evento que queres eliminar "))
        eventoaeliminar = Evento(eventoSeleccionadoFecha, eventoSeleccionadoDescripcion)
        agenda.eliminar(eventoaeliminar)
    hacer = int(input("Ingresa que quieres hacer, 1 para agregar, 2 para mostrar, 3 para eliminar y 4 para salir "))

print ("Gracias por utilizar nuestro programa :3")