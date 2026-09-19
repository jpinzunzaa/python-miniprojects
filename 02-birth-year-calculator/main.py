#!/usr/bin/env python3
"""
Project 02: Birth Year Calculator
=================================

Mini-project that demonstrates:
- Working with the datetime module
- Calculating derived values from user input
- Simple arithmetic with current year
- Clear user interaction and formatted output

This project builds on Project 01 by introducing the standard library and basic calculations.
"""

from datetime import datetime
from typing import Tuple


def get_user_info() -> Tuple[str, int]:
    """Collect name and age from the user.

    Returns:
        Tuple containing the user's name and age.
    """
    name = input("¿Cuál es tu nombre? ").strip()
    while True:
        try:
            age_str = input("¿Cuántos años tienes? ").strip()
            age = int(age_str)
            if age < 0:
                print("La edad no puede ser negativa. Inténtalo de nuevo.")
                continue
            if age > 120:
                print("Parece una edad muy avanzada. ¿Estás seguro? (sí/no)")
                if input().lower() not in ("sí", "si", "yes", "y"):
                    continue
            break
        except ValueError:
            print("Por favor ingresa un número válido para la edad.")

    return name, age


def calculate_birth_year(age: int) -> int:
    """Calculate approximate birth year based on current age.

    Args:
        age: Current age of the person.

    Returns:
        Estimated birth year.
    """
    current_year = datetime.now().year
    return current_year - age


def display_result(name: str, birth_year: int) -> None:
    """Display a friendly message with the calculated birth year.

    Args:
        name: User's name
        birth_year: Calculated birth year
    """
    print("\n" + "=" * 40)
    print(f"¡Hola {name}!")
    print(f"Aproximadamente naciste en el año {birth_year}.")
    print("=" * 40)
    print("\n¡Cálculo completado exitosamente!")


def main() -> int:
    """Main function of the program."""
    print("=== Birth Year Calculator ===\n")
    print("Vamos a calcular en qué año aproximadamente naciste.\n")

    name, age = get_user_info()
    birth_year = calculate_birth_year(age)

    display_result(name, birth_year)
    return 0


if __name__ == "__main__":
    main()
