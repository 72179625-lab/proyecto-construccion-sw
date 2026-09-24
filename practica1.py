def mostrar_menu():
    print("\n=== SISTEMA DE GESTIÓN DE TAREAS ===")
    print("1. Mostrar tareas pendientes")
    print("2. Agregar una nueva tarea")
    print("3. Salir")

def gestionar_tareas():
    tareas = ["Configurar el repositorio Git", "Crear el archivo .gitignore"]
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-3): ").strip()
        if opcion == "1":
            print("\n--- Lista de Tareas ---")
            for i, tarea in enumerate(tareas, 1): print(f"{i}. {tarea}")
        elif opcion == "2":
            nueva_tarea = input("Descripción de la nueva tarea: ").strip()
            if nueva_tarea: tareas.append(nueva_tarea)
        elif opcion == "3":
            print("Saliendo del sistema...")
            break

if __name__ == "__main__":
    gestionar_tareas()

