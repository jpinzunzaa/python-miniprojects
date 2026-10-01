#!/usr/bin/env python3
"""
Project 10: Contact Manager 📱
=============================

A complete command-line contact book (CRUD application) that allows:
- Add new contacts
- List all contacts
- Search contacts
- Update existing contacts
- Delete contacts

This is the tenth project, introducing full CRUD operations on a list of dictionaries,
search functionality, and a clean menu-driven interface.
"""

from typing import List, Dict, Optional


contacts: List[Dict] = []


def add_contact() -> None:
    """Add a new contact to the manager."""
    name = input("Nombre: ").strip()
    phone = input("Teléfono: ").strip()
    email = input("Email: ").strip()

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print("✅ Contacto agregado correctamente.")


def list_contacts() -> None:
    """Display all contacts."""
    if not contacts:
        print("No hay contactos registrados.")
        return

    print("\n" + "=" * 60)
    print("                    LISTA DE CONTACTOS")
    print("=" * 60)

    for i, contact in enumerate(contacts, 1):
        print(
            f"{i:2d}. {contact['name']:<20} | "
            f"{contact['phone']:<15} | "
            f"{contact['email']}"
        )

    print("=" * 60)


def find_contact() -> Optional[Dict]:
    """Find a contact by name and return it."""
    search_name = input("Nombre a buscar: ").strip().lower()

    for contact in contacts:
        if contact["name"].lower() == search_name:
            return contact

    return None


def search_contact() -> None:
    """Search and display a contact."""
    contact = find_contact()
    if contact:
        print("\n" + "=" * 40)
        print("               CONTACTO ENCONTRADO")
        print("=" * 40)
        print(f"Nombre : {contact['name']}")
        print(f"Teléfono: {contact['phone']}")
        print(f"Email  : {contact['email']}")
        print("=" * 40)
    else:
        print("❌ Contacto no encontrado.")


def update_contact() -> None:
    """Update an existing contact."""
    contact = find_contact()
    if not contact:
        print("❌ Contacto no encontrado.")
        return

    print("\nDeja el campo vacío si no quieres modificarlo.")

    name = input(f"Nombre [{contact['name']}]: ").strip()
    phone = input(f"Teléfono [{contact['phone']}]: ").strip()
    email = input(f"Email [{contact['email']}]: ").strip()

    if name:
        contact["name"] = name
    if phone:
        contact["phone"] = phone
    if email:
        contact["email"] = email

    print("✅ Contacto actualizado correctamente.")


def delete_contact() -> None:
    """Delete a contact."""
    contact = find_contact()
    if not contact:
        print("❌ Contacto no encontrado.")
        return

    confirm = input(f"¿Eliminar a {contact['name']}? (s/n): ").strip().lower()
    if confirm in ("s", "sí", "si", "y", "yes"):
        contacts.remove(contact)
        print("✅ Contacto eliminado correctamente.")
    else:
        print("Operación cancelada.")


def main() -> None:
    """Main menu loop for the contact manager."""
    print("📱 GESTOR DE CONTACTOS")
    print("Organiza tu agenda de forma sencilla.\n")

    while True:
        print("\n" + "-" * 45)
        print("1. Agregar contacto")
        print("2. Listar contactos")
        print("3. Buscar contacto")
        print("4. Actualizar contacto")
        print("5. Eliminar contacto")
        print("6. Salir")
        print("-" * 45)

        option = input("Selecciona una opción: ").strip()

        if option == "1":
            add_contact()
        elif option == "2":
            list_contacts()
        elif option == "3":
            search_contact()
        elif option == "4":
            update_contact()
        elif option == "5":
            delete_contact()
        elif option == "6":
            print("\n👋 ¡Hasta luego! Tu agenda ha sido guardada en memoria.")
            break
        else:
            print("❌ Opción inválida. Por favor elige 1-6.")


if __name__ == "__main__":
    main()
