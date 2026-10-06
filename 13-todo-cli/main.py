#!/usr/bin/env python3
"""
Project 13: To-Do CLI ✅
========================

A complete command-line To-Do List manager with:
- Add, list, complete, and delete tasks
- Persistent storage using JSON file (`tasks.json`)
- Clean menu-driven interface
- Proper error handling and user feedback

This is the thirteenth project, introducing file persistence with JSON,
CRUD operations on structured data, and a practical productivity tool.
"""

import json
from pathlib import Path
from typing import List, Dict, Any


FILE = Path("tasks.json")


def load_tasks() -> List[Dict[str, Any]]:
    """Load tasks from JSON file or return empty list if file doesn't exist."""
    if not FILE.exists():
        return []

    try:
        with FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        print("⚠️  Error al leer el archivo. Se iniciará con una lista vacía.")
        return []


def save_tasks(tasks: List[Dict[str, Any]]) -> None:
    """Save tasks to JSON file."""
    try:
        with FILE.open("w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"❌ Error al guardar las tareas: {e}")


def add_task(tasks: List[Dict[str, Any]]) -> None:
    """Add a new task."""
    title = input("Nueva tarea: ").strip()
    if not title:
        print("❌ La tarea no puede estar vacía.")
        return

    task = {
        "title": title,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)
    print("✅ Tarea agregada correctamente.")


def list_tasks(tasks: List[Dict[str, Any]]) -> None:
    """Display all tasks."""
    if not tasks:
        print("No hay tareas pendientes. ¡Bien hecho! 🎉")
        return

    print("\n" + "=" * 50)
    print("                    TAREAS")
    print("=" * 50)

    for index, task in enumerate(tasks, start=1):
        status = "✅" if task["completed"] else "⬜"
        print(f"{index:2d}. {status} {task['title']}")

    print("=" * 50)


def complete_task(tasks: List[Dict[str, Any]]) -> None:
    """Mark a task as completed."""
    list_tasks(tasks)
    if not tasks:
        return

    try:
        number = int(input("\nNúmero de tarea a completar: "))
        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            save_tasks(tasks)
            print("✅ Tarea marcada como completada.")
        else:
            print("❌ Número de tarea inválido.")
    except ValueError:
        print("❌ Por favor ingresa un número válido.")


def delete_task(tasks: List[Dict[str, Any]]) -> None:
    """Delete a task."""
    list_tasks(tasks)
    if not tasks:
        return

    try:
        number = int(input("\nNúmero de tarea a eliminar: "))
        if 1 <= number <= len(tasks):
            deleted = tasks.pop(number - 1)
            save_tasks(tasks)
            print(f"🗑️  Tarea eliminada: {deleted['title']}")
        else:
            print("❌ Número de tarea inválido.")
    except ValueError:
        print("❌ Por favor ingresa un número válido.")


def main() -> None:
    """Main menu loop for the To-Do CLI."""
    tasks = load_tasks()

    print("✅ TODO CLI - Gestor de Tareas")
    print("Mantén tu productividad organizada.\n")

    while True:
        print("\n" + "-" * 45)
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")
        print("-" * 45)

        option = input("Selecciona una opción: ").strip()

        if option == "1":
            add_task(tasks)
        elif option == "2":
            list_tasks(tasks)
        elif option == "3":
            complete_task(tasks)
        elif option == "4":
            delete_task(tasks)
        elif option == "5":
            print("\n👋 ¡Hasta luego! Tus tareas han sido guardadas.")
            break
        else:
            print("❌ Opción inválida. Por favor elige 1-5.")


if __name__ == "__main__":
    main()
