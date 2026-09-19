#!/usr/bin/env python3
"""
Project 03: Personal Profile v2
===============================

Mini-project that demonstrates:
- Multiple user inputs in one session
- Date calculations using datetime
- Simple future projections (age in 10 years)
- Professional ASCII box formatting for output
- Code organization with functions

This is an enhanced version of the personal profile concept, combining
data collection, calculations, and improved visual presentation.
"""

from datetime import datetime
from typing import Tuple


def get_user_data() -> Tuple[str, int, str, str]:
    """Collect personal information from the user.

    Returns:
        Tuple with (name, age, city, profession)
    """
    name = input("Nombre: ").strip()
    while True:
        try:
            age = int(input("Edad: ").strip())
            if age < 0:
                print("La edad no puede ser negativa.")
                continue
            break
        except ValueError:
            print("Por favor ingresa un número válido.")

    city = input("Ciudad: ").strip()
    profession = input("Profesión: ").strip()

    return name, age, city, profession


def calculate_data(age: int) -> Tuple[int, int]:
    """Perform calculations based on age.

    Args:
        age: Current age

    Returns:
        Tuple with (birth_year, age_in_10_years)
    """
    current_year = datetime.now().year
    birth_year = current_year - age
    age_in_10_years = age + 10
    return birth_year, age_in_10_years


def print_profile_box(
    name: str, profession: str, city: str, birth_year: int, age_in_10: int
) -> None:
    """Print the profile inside a nice ASCII box."""
    print()
    print("╔════════════════════════════╗")
    print("║       PERFIL PERSONAL      ║")
    print("╚════════════════════════════╝")
    print(f"Nombre: {name}")
    print(f"Profesión: {profession}")
    print(f"Ciudad: {city}")
    print(f"Año aproximado de nacimiento: {birth_year}")
    print(f"Edad dentro de 10 años: {age_in_10}")
    print("\n¡Perfil generado exitosamente!")


def main() -> int:
    """Main function of the program."""
    print("=== Perfil Personal v2 ===\n")
    print("Por favor completa tu información:\n")

    name, age, city, profession = get_user_data()
    birth_year, age_in_10_years = calculate_data(age)

    print_profile_box(name, profession, city, birth_year, age_in_10_years)
    return 0


if __name__ == "__main__":
    main()
