#!/usr/bin/env python3
"""
Project 12: Text Analyzer 📝
============================

A complete text analysis tool that provides:
- Character and word count
- Average word length
- Word frequency analysis
- Top N most used words
- Support for both direct text input and .txt files
- Clean text processing (remove punctuation, lowercase)

This is the twelfth project, introducing text processing, frequency analysis,
and file reading with pathlib. It has a strong data analysis flavor.
"""

import string
from pathlib import Path
from collections import Counter
from typing import Dict, List, Tuple, Union


def clean_text(text: str) -> str:
    """Clean text by converting to lowercase and removing punctuation."""
    text = text.lower()
    return text.translate(str.maketrans("", "", string.punctuation))


def analyze_text(text: str) -> Dict:
    """Analyze a text and return statistics."""
    cleaned = clean_text(text)
    words = cleaned.split()

    if not words:
        return {
            "characters": len(text),
            "words": 0,
            "unique_words": 0,
            "average_word_length": 0.0,
            "top_words": []
        }

    frequency = Counter(words)
    total_chars = len(text)
    chars_no_spaces = len(text.replace(" ", ""))
    total_words = len(words)
    unique_words = len(frequency)
    avg_word_length = sum(len(word) for word in words) / total_words

    top_words = frequency.most_common(10)

    return {
        "characters": total_chars,
        "characters_no_spaces": chars_no_spaces,
        "words": total_words,
        "unique_words": unique_words,
        "average_word_length": round(avg_word_length, 2),
        "top_words": top_words
    }


def print_analysis(text: str, stats: Dict, source: str = "Texto") -> None:
    """Print formatted analysis results."""
    print("\n" + "═" * 55)
    print(f"          ANALIZADOR DE TEXTO - {source.upper()}")
    print("═" * 55)

    print(f"\n📊 Estadísticas:")
    print(f"   Caracteres: {stats['characters']}")
    print(f"   Caracteres sin espacios: {stats.get('characters_no_spaces', 0)}")
    print(f"   Palabras: {stats['words']}")
    print(f"   Palabras únicas: {stats['unique_words']}")
    print(f"   Longitud promedio de palabra: {stats['average_word_length']}")

    print("\n🏆 Top 10 palabras más usadas:")
    for word, count in stats["top_words"]:
        print(f"   • {word:<15} → {count:3d} veces")

    print("═" * 55)


def analyze_from_file(file_path: Union[str, Path]) -> None:
    """Analyze text from a file."""
    path = Path(file_path)

    if not path.exists():
        print("❌ El archivo no existe.")
        return

    if not path.is_file():
        print("❌ La ruta no es un archivo.")
        return

    try:
        text = path.read_text(encoding="utf-8")
        stats = analyze_text(text)
        print_analysis(text, stats, f"Archivo: {path.name}")
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")


def main() -> None:
    """Main function for the text analyzer."""
    print("📝 ANALIZADOR DE TEXTO")
    print("Extrae estadísticas y patrones de cualquier texto.\n")

    print("1. Analizar texto ingresado")
    print("2. Analizar archivo .txt")
    choice = input("\nSelecciona una opción (1-2): ").strip()

    if choice == "1":
        print("\nEscribe o pega el texto (presiona Enter dos veces para terminar):")
        lines = []
        while True:
            try:
                line = input()
                if line == "":
                    break
                lines.append(line)
            except EOFError:
                break
        text = "\n".join(lines)
        stats = analyze_text(text)
        print_analysis(text, stats)

    elif choice == "2":
        file_path = input("\nIngresa la ruta del archivo .txt: ").strip()
        analyze_from_file(file_path)
    else:
        print("❌ Opción inválida.")


if __name__ == "__main__":
    main()
