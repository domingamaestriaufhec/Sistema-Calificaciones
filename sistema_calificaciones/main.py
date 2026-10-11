"""
Sistema de Gestión de Calificaciones de Estudiantes
---------------------------------------------------
Estudiante: Dominga Rodríguez Marte
Grupo: 40
Institución: Instituto Tecnológico de Las Américas (ITLA)
Asignatura: Fundamentos de Programación

Este programa implementa el uso y manipulación de arreglos (vectores)
en Python para la administración y análisis de calificaciones académicas.

Requisitos cumplidos:
- Vector con al menos 5 elementos.
- Acceso a elementos mediante índices.
- Modificación de elementos mediante índice.
- Recorrido del vector usando ciclos (for / while).
- Condiciones if aplicadas a los elementos del vector.
- Operaciones de cálculo (promedio, suma, máximos, mínimos) y búsqueda.
- Presentación amigable y estructurada de resultados.
"""


def mostrar_calificaciones(calificaciones):
    """Muestra todas las calificaciones recorriendo el arreglo con un ciclo."""
    print("\n--- LISTA ACTUAL DE CALIFICACIONES ---")
    print("Índice | Calificación | Estado")
    print("---------------------------------")
    # Recorrido del vector usando un ciclo for
    for i in range(len(calificaciones)):
        nota = calificaciones[i] # Acceso mediante índice
        # Condición if aplicada a los elementos
        if nota >= 70:
            estado = "Aprobado"
        else:
            estado = "Reprobado"
        print(f"  [{i}]  |     {nota:3d}      | {estado}")
    print("---------------------------------")

def consultar_por_indice(calificaciones):
    """Acceso a un elemento determinado usando su índice."""
    print("\n--- CONSULTAR CALIFICACIÓN POR ÍNDICE ---")
    try:
        indice = int(input(f"Ingrese el índice a consultar (0 a {len(calificaciones) - 1}): "))
        if 0 <= indice < len(calificaciones):
            nota = calificaciones[indice] # Acceso directo por índice
            estado = "Aprobado" if nota >= 70 else "Reprobado"
            print(f"-> Elemento en el índice [{indice}]: {nota} ({estado})")
        else:
            print("Error: Índice fuera de rango.")
    except ValueError:
        print("Error: Por favor, ingrese un número entero válido.")

def modificar_calificacion(calificaciones):
    """Modificación de un elemento del vector mediante su índice."""
    print("\n--- MODIFICAR CALIFICACIÓN ---")
    try:
        indice = int(input(f"Ingrese el índice del elemento a modificar (0 a {len(calificaciones) - 1}): "))
        if 0 <= indice < len(calificaciones):
            print(f"Calificación actual en el índice [{indice}]: {calificaciones[indice]}")
            nueva_nota = int(input("Ingrese la nueva calificación (0-100): "))
            if 0 <= nueva_nota <= 100:
                nota_anterior = calificaciones[indice]
                calificaciones[indice] = nueva_nota # Modificación de elemento
                print(f"Éxito: Se actualizó el índice [{indice}] de {nota_anterior} a {nueva_nota}.")
            else:
                print("Error: La calificación debe estar entre 0 y 100.")
        else:
            print("Error: Índice fuera de rango.")
    except ValueError:
        print("Error: Entrada no válida. Ingrese valores numéricos.")

def calcular_estadisticas(calificaciones):
    """Cálculos estadísticos: promedio, máximo, mínimo, aprobados y reprobados."""
    print("\n--- ESTADÍSTICAS Y CÁLCULOS DEL GRUPO ---")
    total_estudiantes = len(calificaciones)
    if total_estudiantes == 0:
        print("No hay calificaciones registradas.")
        return

    suma = 0
    aprobados = 0
    reprobados = 0
    nota_maxima = calificaciones[0]
    nota_minima = calificaciones[0]
    indice_max = 0
    indice_min = 0

    # Recorrido con ciclo para cálculo acumulativo y búsqueda de extremos
    for i in range(total_estudiantes):
        nota = calificaciones[i]
        suma += nota

        # Condición if para conteo de aprobados y reprobados
        if nota >= 70:
            aprobados += 1
        else:
            reprobados += 1

        # Búsqueda de nota máxima
        if nota > nota_maxima:
            nota_maxima = nota
            indice_max = i

        # Búsqueda de nota mínima
        if nota < nota_minima:
            nota_minima = nota
            indice_min = i

    promedio = suma / total_estudiantes

    print(f"Total de evaluaciones : {total_estudiantes}")
    print(f"Promedio general       : {promedio:.2f}")
    print(f"Calificación más alta  : {nota_maxima} (en el índice [{indice_max}])")
    print(f"Calificación más baja  : {nota_minima} (en el índice [{indice_min}])")
    print(f"Estudiantes aprobados  : {aprobados} ({(aprobados / total_estudiantes) * 100:.1f}%)")
    print(f"Estudiantes reprobados : {reprobados} ({(reprobados / total_estudiantes) * 100:.1f}%)")

def buscar_calificacion(calificaciones):
    """Búsqueda de calificaciones específicas en el vector."""
    print("\n--- BÚSQUEDA DE CALIFICACIÓN ---")
    try:
        objetivo = int(input("Ingrese la calificación que desea buscar: "))
        encontrados = []
        for i in range(len(calificaciones)):
            if calificaciones[i] == objetivo:
                encontrados.append(i)
        
        if encontrados:
            print(f"-> La calificación {objetivo} se encontró en el/los índice(s): {encontrados}")
        else:
            print(f"-> La calificación {objetivo} no se encuentra en el arreglo.")
    except ValueError:
        print("Error: Ingrese un valor numérico entero.")

def main():
    # Arreglo o vector inicial con al menos 5 elementos
    calificaciones = [85, 67, 92, 74, 58]

    while True:
        print("\n==========================================")
        print("   SISTEMA DE GESTIÓN DE CALIFICACIONES   ")
        print("==========================================")
        print("1. Mostrar todas las calificaciones")
        print("2. Consultar calificación por índice")
        print("3. Modificar una calificación")
        print("4. Calcular estadísticas (promedio, máx, mín, aprobados)")
        print("5. Buscar una calificación específica")
        print("6. Salir")
        print("==========================================")
        
        opcion = input("Seleccione una opción (1-6): ").strip()

        if opcion == "1":
            mostrar_calificaciones(calificaciones)
        elif opcion == "2":
            consultar_por_indice(calificaciones)
        elif opcion == "3":
            modificar_calificacion(calificaciones)
            mostrar_calificaciones(calificaciones)
        elif opcion == "4":
            calcular_estadisticas(calificaciones)
        elif opcion == "5":
            buscar_calificacion(calificaciones)
        elif opcion == "6":
            print("\nGracias por utilizar el Sistema de Calificaciones. ¡Hasta pronto!\n")
            break
        else:
            print("\nOpción no válida. Por favor, seleccione un número del 1 al 6.")

if __name__ == "__main__":
    main()
