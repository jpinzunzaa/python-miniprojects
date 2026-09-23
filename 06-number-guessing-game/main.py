#!/usr/bin/env python3
"""
Project 06: Number Guessing Game 🎯
===================================

A complete "Guess the Number" game with:
- Random number generation
- Limited attempts (7 by default)
- Progressive hints (higher/lower)
- Attempt counter
- Win/lose conditions with engaging messages
- Clean, professional code structure

This is the sixth project, introducing randomness (`random` module),
game loops with limited attempts, and state management.
"""

import random
from typing import Tuple


def generate_secret_number(min_num: int = 1, max_num: int = 100) -> int:
    """Generate a random secret number within the given range."""
    return random.randint(min_num, max_num)


def get_player_guess() -> int:
    """Get and validate the player's guess."""
    while True:
        try:
            guess = int(input("Tu número: ").strip())
            if 1 <= guess <= 100:
                return guess
            print("Por favor ingresa un número entre 1 y 100.")
        except ValueError:
            print("Entrada inválida. Ingresa un número entero.")


def play_game() -> None:
    """Run one complete game session."""
    secret_number = generate_secret_number()
    max_attempts = 7
    attempts = 0

    print("\n🎯 ADIVINA EL NÚMERO")
    print("Estoy pensando en un número entre 1 y 100.")
    print(f"Tienes {max_attempts} intentos máximos.\n")

    while attempts < max_attempts:
        guess = get_player_guess()
        attempts += 1

        if guess == secret_number:
            print("\n🎉 ¡GANASTE!")
            print(f"Adivinaste el número en {attempts} intentos.")
            return

        if guess < secret_number:
            print("📈 El número secreto es MAYOR.")
        else:
            print("📉 El número secreto es MENOR.")

        remaining = max_attempts - attempts
        print(f"Intentos restantes: {remaining}\n")

    # Game over - ran out of attempts
    print("\n💀 GAME OVER")
    print(f"El número secreto era {secret_number}.")


def main() -> None:
    """Main function with option to play multiple rounds."""
    print("¡Bienvenido al Juego de Adivina el Número!")

    while True:
        play_game()

        play_again = input("\n¿Quieres jugar de nuevo? (s/n): ").strip().lower()
        if play_again not in ("s", "sí", "si", "y", "yes"):
            print("¡Gracias por jugar! Hasta la próxima 🎮")
            break


if __name__ == "__main__":
    main()
