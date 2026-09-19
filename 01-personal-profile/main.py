#!/usr/bin/env python3
"""
Project 01: Personal Profile with Inputs
========================================

Mini-project that demonstrates:
- Use of input() to collect user data
- Type conversion (str → int)
- f-strings for advanced formatting
- Structured information presentation
- Good structure with main() function and execution guard

This is the first project in the series and sets the foundation for user interaction.
"""

from typing import Tuple

def collect_user_data() -> Tuple[str, int, str, str]:
  """Collects personal information from the user through inputs.

  Returns:
    Tuple with (name, age, city, profession)
  """
  name = input("¿Cuál es tu nombre? ").strip()
  while True:
    try:
      age_str = input("¿Cuántos años tienes? ").strip()
      age = int(age_str)
      if age < 0:
        print("La edad no puede ser negativa. Inténtalo de nuevo.")
        continue
      break
    except ValueError:
      print("Por favor ingresa un número válido para la edad.")

  city = input("¿En qué ciudad vives? ").strip()
  profession = input("¿Cuál es tu profesión? ").strip()

  return name, age, city, profession

def print_profile(name: str, age: int, city: str, profession: str) -> None:
  """Prints the profile in a professional formatted way.

  Args:
    name: User's name
    age: User's age
    city: City of residence
    profession: Profession or occupation
  """
  print("\n" + "=" * 25)
  print("     MY PROFILE")
  print("=" * 25)
  print(f"Name       : {name}")
  print(f"Age        : {age} years")
  print(f"City       : {city}")
  print(f"Profession : {profession}")
  print("=" * 25)
  print("\nProfile generated successfully!")

def main() -> int:
  """Main function of the program."""
  print("=== Personal Profile Generator ===\n")
  print("Please answer the following questions:\n")

  name, age, city, profession = collect_user_data()

  if not name or not city or not profession:
    print("\n⚠️  Some fields were left empty. The profile will still be generated.")

  print_profile(name, age, city, profession)
  return 0

if __name__ == "__main__":
  main()