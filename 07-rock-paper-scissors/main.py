#!/usr/bin/env python3
"""
Project 07: Rock, Paper, Scissors ✂️
====================================

A complete Rock-Paper-Scissors game against the computer:
- Best of 3 (first to 3 wins)
- Input validation
- Score tracking
- Clear round and final results
- Professional code structure with functions

This is the seventh project, introducing game logic with win conditions,
score tracking across multiple rounds, and input validation.
"""

import random
from typing import Tuple


def get_player_choice() -> str:
    """Get and validate the player's choice."""
    options = ["piedra", "papel", "tijera"]
    while True:
        choice = input("\nElige (piedra, papel o tijera): ").lower().strip()
        if choice in options:
            return choice
        print("❌ Opción inválida. Por favor elige 'piedra', 'papel' o 'tijera'.")


def get_computer_choice() -> str:
    """Return a random choice for the computer."""
    options = ["piedra", "papel", "tijera"]
    return random.choice(options)


def determine_winner(player: str, computer: str) -> str:
    """Determine the winner of a single round."""
    if player == computer:
        return "Empate"

    winning_combinations = {
        ("piedra", "tijera"),
        ("papel", "piedra"),
        ("tijera", "papel"),
    }

    if (player, computer) in winning_combinations:
        return "Ganaste"

    return "Perdiste"


def print_round_result(player: str, computer: str, result: str) -> None:
    """Print the result of a single round."""
    print(f"\nTú elegiste: {player}")
    print(f"La computadora eligió: {computer}")

    if result == "Ganaste":
        print("🎉 ¡Ganaste la ronda!")
    elif result == "Perdiste":
        print("💀 Perdiste la ronda.")
    else:
        print("🤝 Empate.")


def main() -> None:
    """Main game loop - first to 3 wins."""
    player_score = 0
    computer_score = 0

    print("🎮 PIEDRA, PAPEL O TIJERA")
    print("El primero en llegar a 3 puntos gana.\n")

    while player_score < 3 and computer_score < 3:
        print(f"\nMarcador → Tú: {player_score} | Computadora: {computer_score}")

        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)

        print_round_result(player_choice, computer_choice, result)

        if result == "Ganaste":
            player_score += 1
        elif result == "Perdiste":
            computer_score += 1

    print("\n" + "=" * 40)
    if player_score == 3:
        print("🏆 ¡FELICIDADES! GANASTE EL JUEGO")
    else:
        print("💻 LA COMPUTADORA GANÓ EL JUEGO")
    print("=" * 40)
    print(f"Marcador final: {player_score} - {computer_score}\n")


if __name__ == "__main__":
    main()
