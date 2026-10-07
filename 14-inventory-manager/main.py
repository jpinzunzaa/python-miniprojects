#!/usr/bin/env python3
"""
Project 14: Inventory Manager 📦
===============================

A complete inventory management system with:
- Add products (name, price, stock)
- List inventory
- Search products
- Record sales (reduces stock)
- View total inventory value
- Persistent storage using JSON file (`inventory.json`)

This is the fourteenth project, building on the previous To-Do and Contact Manager by introducing business logic (sales, valuation) and more sophisticated data operations.
"""

import json
from pathlib import Path
from typing import List, Dict, Any, Optional


FILE = Path("inventory.json")


def load_products() -> List[Dict[str, Any]]:
    """Load products from JSON file or return empty list."""
    if not FILE.exists():
        return []

    try:
        with FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        print("⚠️  Error al leer el archivo. Iniciando con inventario vacío.")
        return []


def save_products(products: List[Dict[str, Any]]) -> None:
    """Save products to JSON file."""
    try:
        with FILE.open("w", encoding="utf-8") as file:
            json.dump(products, file, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"❌ Error al guardar el inventario: {e}")


def add_product(products: List[Dict[str, Any]]) -> None:
    """Add a new product to inventory."""
    name = input("Nombre del producto: ").strip()
    if not name:
        print("❌ El nombre no puede estar vacío.")
        return

    try:
        price = float(input("Precio ($): ").strip())
        stock = int(input("Stock inicial: ").strip())
        if price < 0 or stock < 0:
            print("❌ El precio y el stock deben ser positivos.")
            return
    except ValueError:
        print("❌ Por favor ingresa números válidos.")
        return

    product = {
        "name": name,
        "price": price,
        "stock": stock
    }

    products.append(product)
    save_products(products)
    print("✅ Producto agregado correctamente.")


def list_products(products: List[Dict[str, Any]]) -> None:
    """Display all products in inventory."""
    if not products:
        print("El inventario está vacío.")
        return

    print("\n" + "=" * 60)
    print("                    INVENTARIO")
    print("=" * 60)

    for i, product in enumerate(products, 1):
        print(
            f"{i:2d}. {product['name']:<25} "
            f"${product['price']:>8.2f}   "
            f"Stock: {product['stock']:>3}"
        )

    print("=" * 60)


def find_product(products: List[Dict[str, Any]], search_name: str) -> Optional[Dict[str, Any]]:
    """Find a product by name (case-insensitive)."""
    search = search_name.lower()
    for product in products:
        if product["name"].lower() == search:
            return product
    return None


def search_product(products: List[Dict[str, Any]]) -> None:
    """Search and display a product."""
    name = input("Producto a buscar: ").strip()
    product = find_product(products, name)

    if product:
        print("\n" + "=" * 40)
        print("               PRODUCTO ENCONTRADO")
        print("=" * 40)
        print(f"Nombre : {product['name']}")
        print(f"Precio : ${product['price']:.2f}")
        print(f"Stock  : {product['stock']}")
        print("=" * 40)
    else:
        print("❌ Producto no encontrado.")


def sell_product(products: List[Dict[str, Any]]) -> None:
    """Record a sale and reduce stock."""
    name = input("Producto vendido: ").strip()
    product = find_product(products, name)

    if not product:
        print("❌ Producto no encontrado.")
        return

    try:
        quantity = int(input("Cantidad vendida: ").strip())
        if quantity <= 0:
            print("❌ La cantidad debe ser mayor que 0.")
            return
    except ValueError:
        print("❌ Por favor ingresa un número válido.")
        return

    if quantity > product["stock"]:
        print("❌ Stock insuficiente.")
        return

    product["stock"] -= quantity
    total = product["price"] * quantity

    save_products(products)

    print("\n✅ Venta registrada correctamente.")
    print(f"Producto   : {product['name']}")
    print(f"Cantidad   : {quantity}")
    print(f"Total      : ${total:.2f}")
    print(f"Stock restante: {product['stock']}")


def inventory_value(products: List[Dict[str, Any]]) -> None:
    """Calculate and display total inventory value."""
    if not products:
        print("El inventario está vacío.")
        return

    total_value = sum(product["price"] * product["stock"] for product in products)

    print("\n" + "=" * 40)
    print("           VALOR DEL INVENTARIO")
    print("=" * 40)
    print(f"Valor total: ${total_value:.2f}")
    print("=" * 40)


def main() -> None:
    """Main menu loop for the inventory manager."""
    products = load_products()

    print("📦 SISTEMA DE GESTIÓN DE INVENTARIO")
    print("Controla tu stock de forma eficiente.\n")

    while True:
        print("\n" + "-" * 50)
        print("1. Agregar producto")
        print("2. Ver inventario")
        print("3. Buscar producto")
        print("4. Registrar venta")
        print("5. Valor total del inventario")
        print("6. Salir")
        print("-" * 50)

        option = input("Selecciona una opción: ").strip()

        if option == "1":
            add_product(products)
        elif option == "2":
            list_products(products)
        elif option == "3":
            search_product(products)
        elif option == "4":
            sell_product(products)
        elif option == "5":
            inventory_value(products)
        elif option == "6":
            print("\n👋 Sistema cerrado. ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Por favor elige 1-6.")


if __name__ == "__main__":
    main()
