#!/usr/bin/env python3
"""
Project 08: Password Generator 🔐
================================

A professional password generator that:
- Uses cryptographically secure random (secrets module)
- Allows user to choose length
- Includes letters, digits and special characters
- Validates minimum length (8 characters)
- Clean, professional output with visual formatting

This is the eighth project, introducing secure randomness, string constants,
and a more polished user experience.
"""

import secrets
import string
from typing import Optional


def generate_password(length: int = 16) -> str:
    """Generate a secure random password of the specified length.

    Args:
        length: Desired password length (minimum 8)

    Returns:
        A randomly generated password
    """
    if length < 8:
        length = 8

    characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    password = "".join(secrets.choice(characters) for _ in range(length))
    return password


def main() -> None:
    """Main function for the password generator."""
    print("🔐 GENERADOR DE CONTRASEÑAS SEGURAS")
    print("=" * 40)
    print("Este generador usa criptografía segura (secrets).\n")

    while True:
        try:
            length_input = input("¿Cuántos caracteres deseas? (mínimo 8): ").strip()
            length = int(length_input)
            break
        except ValueError:
            print("❌ Por favor ingresa un número válido.")

    if length < 8:
        print("⚠️  La longitud mínima recomendada es 8 caracteres.")
        length = 8

    password = generate_password(length)

    print("\n" + "=" * 40)
    print("     CONTRASEÑA GENERADA")
    print("=" * 40)
    print(password)
    print("=" * 40)
    print(f"\nLongitud: {length} caracteres")
    print("¡Mantén esta contraseña en un lugar seguro!")


if __name__ == "__main__":
    main()
