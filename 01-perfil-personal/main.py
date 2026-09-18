#!/usr/bin/env python3
"""
Proyecto 01: Perfil Personal con Inputs
======================================

Mini-proyecto que demuestra:
- Uso de input() para recolectar datos del usuario
- Conversión de tipos (str → int)
- f-strings para formateo avanzado
- Presentación estructurada de información
- Buena estructura con función main() y guard de ejecución

Este es el primer proyecto de la serie y establece las bases para interacción con el usuario.
"""

from typing import Tuple


def collect_user_data() -> Tuple[str, int, str, str]:
    """Recolecta información personal del usuario mediante inputs.

    Returns:
        Tuple con (nombre, edad, ciudad, profesión)
    """
    name = input("¿Cuál es tu nombre? ").strip()
    while True:
        try:
            age_str = input("¿Cuántos años tienes? ").strip()
            age = int(age_str)
            if age < 0:
                print("La edad no puede ser negativa. Inténtalo de nuevo.")
                continue
            break
        except ValueError:
            print("Por favor ingresa un número válido para la edad.")

    city = input("¿En qué ciudad vives? ").strip()
    profession = input("¿Cuál es tu profesión? ").strip()

    return name, age, city, profession


def print_profile(name: str, age: int, city: str, profession: str) -> None:
    """Imprime el perfil formateado de manera profesional.

    Args:
        name: Nombre del usuario
        age: Edad del usuario
        city: Ciudad de residencia
        profession: Profesión u ocupación
    """
    print("\n" + "=" * 25)
    print("     MI PERFIL")
    print("=" * 25)
    print(f"Nombre     : {name}")
    print(f"Edad       : {age} años")
    print(f"Ciudad     : {city}")
    print(f"Profesión  : {profession}")
    print("=" * 25)
    print("\n¡Perfil generado exitosamente!")


def main() -> int:
    """Función principal del programa."""
    print("=== Generador de Perfil Personal ===\n")
    print("Por favor responde las siguientes preguntas:\n")

    name, age, city, profession = collect_user_data()

    if not name or not city or not profession:
        print("\n⚠️  Algunos campos quedaron vacíos. El perfil se generará de todos modos.")

    print_profile(name, age, city, profession)
    return 0


if __name__ == "__main__":
    main()
