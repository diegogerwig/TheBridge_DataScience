class Tarea:
    def __init__(self, descripcion, completada=False):
        self.descripcion = descripcion
        self.completada = completada

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        tarea = Tarea(descripcion)
        self.tareas.append(tarea)

    def marcar_completada(self, indice):
        try:
            self.tareas[indice].completada = True
        except IndexError:
            print("La posición ingresada no existe en la lista.")

    def mostrar_tareas(self):
        for i, tarea in enumerate(self.tareas):
            estado = "Completada" if tarea.completada else "Pendiente"
            print(f"{i+1}. {tarea.descripcion} - Estado: {estado}")

    def eliminar_tarea(self, indice):
        try:
            del self.tareas[indice]
        except IndexError:
            print("La posición ingresada no existe en la lista.")

if __name__ == "__main__":
    gestor = GestorTareas()

    while True:
        print("\n1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar todas las tareas")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            descripcion = input("Ingrese la descripción de la tarea: ")
            gestor.agregar_tarea(descripcion)
        elif opcion == "2":
            indice = int(input("Ingrese el número de la tarea a marcar como completada: ")) - 1
            gestor.marcar_completada(indice)
        elif opcion == "3":
            gestor.mostrar_tareas()
        elif opcion == "4":
            indice = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
            gestor.eliminar_tarea(indice)
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")
