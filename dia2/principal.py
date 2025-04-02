import models.clases as c 
from controllers.dao_controller import MateriaDao
import os


"""materia = c.Materia("Calculo", "MAT101", 4)
materia_dao = dao.MateriaDao()
dao.agregar_materias(materia)
dao.obtener_materias()"""

# Limpiar la consola dependiendo del sistema operativo
os.system('cls' if os.name == 'nt' else 'clear')

# Color fondo de consola
os.system('color 0A') # Color help 

    
def agregar_materia(dao):
    print("-"*10)
    nombre = input("Ingrese el nombre de la materia: ")
    codigo = input("Ingrese el código de la materia: ")
    creditos = int(input("Ingrese el número de créditos: "))
    
    materia = c.Materia(nombre, codigo, creditos)
    dao.agregar_materias(materia)
    print("Materia agregada exitosamente!")
    print("-"*10)
    
def mostrar_materias(dao):
    print("-"*10)
    print("Lista de materias:")
    dao.obtener_materias()
    print("-"*10)
    
def menu():
    print("Bienvenido al sistema de gestión de materias")
    print("1. Agregar materia")
    print("2. Mostrar materias")
    print("3. Salir")
    
def main():
    materia_dao = MateriaDao()
    while True:
        menu()
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            agregar_materia((materia_dao))
        elif opcion == 2:
            mostrar_materias(materia_dao)
        elif opcion == 3:
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
