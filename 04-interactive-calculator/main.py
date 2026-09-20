#!/usr/bin/env python3
"""
Project 04: Interactive Calculator
==================================

This is a complete interactive calculator that demonstrates:
- Functions for each arithmetic operation
- Menu-driven interface with loop
- Input validation
- Protection against division by zero
- Clean code organization and user-friendly interface

This project significantly increases complexity by introducing control flow with loops,
menu systems, and robust error handling.
"""

from typing import Optional, Callable


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> Optional[float]:
    """Return the division of a by b. Returns None if dividing by zero."""
    if b == 0:
        return None
    return a / b


def get_operation_choice() -> str:
    """Display menu and get user's operation choice."""
    print("\n===== CALCULADORA INTERACTIVA =====")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    return input("Selecciona una opción (1-5): ").strip()


def get_numbers() -> tuple[float, float]:
    """Get two numbers from the user."""
    while True:
        try:
            num1 = float(input("Primer número: "))
            num2 = float(input("Segundo número: "))
            return num1, num2
        except ValueError:
            print("Error: Por favor ingresa números válidos.")


def main() -> None:
    """Main program loop."""
    operations: dict[str, Callable[[float, float], Optional[float]]] = {
        "1": add,
        "2": subtract,
        "3": multiply,
        "4": divide,
    }

    print("Bienvenido a la Calculadora Interactiva!")

    while True:
        option = get_operation_choice()

        if option == "5":
            print("¡Gracias por usar la calculadora! Hasta pronto.")
            break

        if option not in operations:
            print("Opción no válida. Por favor selecciona 1-5.")
            continue

        num1, num2 = get_numbers()
        operation_func = operations[option]
        result = operation_func(num1, num2)

        if result is None:
            print("Error: No puedes dividir entre cero.")
        else:
            operation_name = {
                "1": "suma",
                "2": "resta",
                "3": "multiplicación",
                "4": "división"
            }.get(option, "operación")
            print(f"\nResultado de la {operation_name}: {result}")


if __name__ == "__main__":
    main()
