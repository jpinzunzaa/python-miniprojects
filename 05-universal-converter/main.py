#!/usr/bin/env python3
"""
Project 05: Universal Converter
===============================

A complete universal unit converter with multiple categories:
- Temperature (Celsius ↔ Fahrenheit)
- Distance (Kilometers ↔ Miles)
- Weight (Kilograms ↔ Pounds)

Features:
- Menu-driven interface with loop
- Bidirectional conversions
- Clean function-based design
- Input validation and formatted output
- Professional structure following previous project patterns

This is the fifth project, increasing complexity with multiple conversion categories
and a more sophisticated menu system.
"""

from typing import Callable, Dict


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def kilometers_to_miles(kilometers: float) -> float:
    """Convert kilometers to miles."""
    return kilometers * 0.621371


def miles_to_kilometers(miles: float) -> float:
    """Convert miles to kilometers."""
    return miles * 1.60934


def kilograms_to_pounds(kilograms: float) -> float:
    """Convert kilograms to pounds."""
    return kilograms * 2.20462


def pounds_to_kilograms(pounds: float) -> float:
    """Convert pounds to kilograms."""
    return pounds / 2.20462


def print_menu() -> None:
    """Display the main converter menu."""
    print("\n" + "=" * 35)
    print("     CONVERSOR UNIVERSAL")
    print("=" * 35)
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Kilómetros → Millas")
    print("4. Millas → Kilómetros")
    print("5. Kilogramos → Libras")
    print("6. Libras → Kilogramos")
    print("7. Salir")
    print("=" * 35)


def get_conversion_choice() -> str:
    """Get and validate user's menu choice."""
    while True:
        choice = input("\nSelecciona una opción (1-7): ").strip()
        if choice in ["1", "2", "3", "4", "5", "6", "7"]:
            return choice
        print("Opción no válida. Por favor elige entre 1 y 7.")


def get_value(prompt: str = "Ingresa el valor: ") -> float:
    """Get a numeric value from the user with validation."""
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Error: Por favor ingresa un número válido.")


def main() -> None:
    """Main program with conversion menu loop."""
    conversions: Dict[str, Callable[[float], float]] = {
        "1": celsius_to_fahrenheit,
        "2": fahrenheit_to_celsius,
        "3": kilometers_to_miles,
        "4": miles_to_kilometers,
        "5": kilograms_to_pounds,
        "6": pounds_to_kilograms,
    }

    unit_names = {
        "1": "°F",
        "2": "°C",
        "3": "millas",
        "4": "kilómetros",
        "5": "libras",
        "6": "kilogramos",
    }

    print("¡Bienvenido al Conversor Universal!")

    while True:
        print_menu()
        option = get_conversion_choice()

        if option == "7":
            print("\n¡Gracias por usar el Conversor Universal! Hasta pronto.")
            break

        value = get_value()

        result = conversions[option](value)
        unit = unit_names[option]

        print(f"\nResultado: {result:.2f} {unit}")


if __name__ == "__main__":
    main()
