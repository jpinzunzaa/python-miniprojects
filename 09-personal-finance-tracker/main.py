#!/usr/bin/env python3
"""
Project 09: Personal Finance Tracker 💰
======================================

A complete personal expense tracker with:
- Add expenses with description, amount and category
- View all expenses
- Summary with total and breakdown by category
- Menu-driven interface
- Persistent in-memory storage (for this mini-project)

This is the ninth project, introducing data management with lists of dictionaries,
menu systems, and basic data analysis (grouping by category).
"""

from typing import List, Dict


expenses: List[Dict] = []


def add_expense() -> None:
    """Add a new expense to the tracker."""
    description = input("Descripción del gasto: ").strip()
    while True:
        try:
            amount = float(input("Cantidad ($): ").strip())
            if amount <= 0:
                print("La cantidad debe ser mayor que 0.")
                continue
            break
        except ValueError:
            print("Por favor ingresa un número válido.")

    category = input("Categoría (comida, transporte, etc.): ").strip().lower()

    expense = {
        "description": description,
        "amount": amount,
        "category": category or "sin-categoria"
    }

    expenses.append(expense)
    print("✅ Gasto registrado correctamente.")


def show_expenses() -> None:
    """Display all recorded expenses."""
    if not expenses:
        print("No hay gastos registrados aún.")
        return

    print("\n" + "=" * 50)
    print("               LISTA DE GASTOS")
    print("=" * 50)

    for i, expense in enumerate(expenses, 1):
        print(
            f"{i:2d}. {expense['description']:<25} "
            f"${expense['amount']:>8.2f}   "
            f"{expense['category']}"
        )

    print("=" * 50)


def show_summary() -> None:
    """Show total expenses and breakdown by category."""
    if not expenses:
        print("No hay gastos registrados aún.")
        return

    total = sum(expense["amount"] for expense in expenses)

    categories: Dict[str, float] = {}
    for expense in expenses:
        cat = expense["category"]
        categories[cat] = categories.get(cat, 0) + expense["amount"]

    print("\n" + "=" * 50)
    print("                 RESUMEN")
    print("=" * 50)
    print(f"Total gastado: ${total:.2f}\n")
    print("Por categoría:")

    for category, amount in sorted(categories.items(), key=lambda x: x[1], reverse=True):
        percentage = (amount / total * 100) if total > 0 else 0
        print(f"• {category:<15} ${amount:>8.2f} ({percentage:5.1f}%)")

    print("=" * 50)


def main() -> None:
    """Main program loop."""
    print("💰 SISTEMA DE CONTROL DE GASTOS PERSONALES")
    print("Mantén el control de tus finanzas de forma simple.\n")

    while True:
        print("\n" + "-" * 40)
        print("1. Agregar gasto")
        print("2. Ver todos los gastos")
        print("3. Ver resumen por categoría")
        print("4. Salir")
        print("-" * 40)

        option = input("Selecciona una opción: ").strip()

        if option == "1":
            add_expense()
        elif option == "2":
            show_expenses()
        elif option == "3":
            show_summary()
        elif option == "4":
            print("\n👋 ¡Hasta luego! Mantén el control de tus gastos.")
            break
        else:
            print("❌ Opción inválida. Por favor elige 1-4.")


if __name__ == "__main__":
    main()
