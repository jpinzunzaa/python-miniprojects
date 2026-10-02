#!/usr/bin/env python3
"""
Project 11: File Organizer 📁
============================

A professional automatic file organizer that:
- Scans a folder for files
- Organizes them into categorized subfolders (images, documents, videos, audio, others)
- Uses pathlib for modern path handling
- Handles existing files gracefully
- Provides clear feedback during organization

This is the eleventh project, introducing file system operations, pathlib, and practical automation tools.
"""

from pathlib import Path
from typing import Dict


def create_folders(base_folder: Path) -> None:
    """Create category folders if they don't exist."""
    folders = ["imagenes", "documentos", "videos", "audio", "otros"]

    for folder_name in folders:
        (base_folder / folder_name).mkdir(exist_ok=True)


def get_category(extension: str) -> str:
    """Return the appropriate category for a file extension."""
    categories: Dict[str, list[str]] = {
        "imagenes": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".tiff"],
        "documentos": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".csv", ".pptx", ".md"],
        "videos": [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv"],
        "audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"]
    }

    ext = extension.lower()

    for category, extensions in categories.items():
        if ext in extensions:
            return category

    return "otros"


def organize_files(folder: Path) -> None:
    """Organize all files in the given folder into category subfolders."""
    if not folder.exists():
        print("❌ La carpeta no existe.")
        return

    if not folder.is_dir():
        print("❌ La ruta proporcionada no es una carpeta.")
        return

    create_folders(folder)

    organized_count = 0

    for file in folder.iterdir():
        if not file.is_file():
            continue

        category = get_category(file.suffix)
        destination = folder / category / file.name

        if destination.exists():
            print(f"⚠️  Ya existe: {file.name} en {category}")
            continue

        try:
            file.rename(destination)
            print(f"✅ {file.name} → {category}")
            organized_count += 1
        except Exception as e:
            print(f"❌ Error al mover {file.name}: {e}")

    print(f"\n🚀 Organización completada. {organized_count} archivos organizados.")


def main() -> None:
    """Main function for the file organizer."""
    print("📁 ORGANIZADOR AUTOMÁTICO DE ARCHIVOS")
    print("=" * 50)
    print("Este programa organiza tus archivos en carpetas por tipo.\n")

    while True:
        path_input = input("Ingresa la ruta de la carpeta a organizar (o 'salir'): ").strip()

        if path_input.lower() in ("salir", "exit", "q"):
            print("👋 ¡Hasta luego!")
            break

        folder = Path(path_input)

        if not folder.exists():
            print("❌ La carpeta no existe. Inténtalo de nuevo.")
            continue

        organize_files(folder)

        again = input("\n¿Quieres organizar otra carpeta? (s/n): ").strip().lower()
        if again not in ("s", "sí", "si", "y", "yes"):
            print("¡Gracias por usar el Organizador de Archivos!")
            break


if __name__ == "__main__":
    main()
