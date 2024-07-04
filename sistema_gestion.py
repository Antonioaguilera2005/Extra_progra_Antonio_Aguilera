class Tarea:
    def __init__(self, titulo, descripcion=""):
        self.titulo = titulo
        self.descripcion = descripcion

    def __str__(self):
        return f"Título: {self.titulo}, Descripción: {self.descripcion}"


class GestorDeTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, titulo, descripcion=""):
        nueva_tarea = Tarea(titulo, descripcion)
        self.tareas.append(nueva_tarea)
        print(f"Tarea '{titulo}' agregada con éxito.")

    def eliminar_tarea(self, titulo):
        for tarea in self.tareas:
            if tarea.titulo == titulo:
                self.tareas.remove(tarea)
                print(f"Tarea '{titulo}' eliminada con éxito.")
                return
        print(f"Tarea '{titulo}' no encontrada.")

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas.")
        else:
            print("Lista de Tareas:")
            for tarea in self.tareas:
                print(tarea)


def mostrar_menu():
    print("\nGestor de Tareas")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Mostrar tareas")
    print("4. Salir")


def main():
    gestor = GestorDeTareas()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            titulo = input("Ingrese el título de la tarea: ")
            descripcion = input("Ingrese la descripción de la tarea (opcional): ")
            gestor.agregar_tarea(titulo, descripcion)
        elif opcion == '2':
            titulo = input("Ingrese el título de la tarea a eliminar: ")
            gestor.eliminar_tarea(titulo)
        elif opcion == '3':
            gestor.mostrar_tareas()
        elif opcion == '4':
            print("Saliendo del gestor de tareas.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
