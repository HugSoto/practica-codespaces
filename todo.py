def mostrar_menu():
    print("\n--- MENÚ DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

def agregar_tarea(lista_tareas):
    tarea = input("Escribe la nueva tarea: ")
    lista_tareas.append(tarea)
    print("Tarea agregada.")

def listar_tareas(lista_tareas):
    if not lista_tareas:
        print("No hay tareas.")
    else:
        print("\n--- TUS TAREAS ---")
        for i, tarea in enumerate(lista_tareas, start=1):
            print(f"{i}. {tarea}")

def eliminar_tarea(lista_tareas):
    listar_tareas(lista_tareas)
    if lista_tareas:
        try:
            num = int(input("Número de la tarea a eliminar: "))
            if 1 <= num <= len(lista_tareas):
                tarea_eliminada = lista_tareas.pop(num - 1)
                print(f"Tarea '{tarea_eliminada}' eliminada.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Por favor ingresa un número válido.")

def programa_principal():
    tareas = []
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-4): ")
        
        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            listar_tareas(tareas)
        elif opcion == "3":
            eliminar_tarea(tareas)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# Iniciar el programa
programa_principal()
