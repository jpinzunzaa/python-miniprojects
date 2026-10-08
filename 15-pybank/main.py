#!/usr/bin/env python3
"""
Project 15: PyBank - Digital Bank 🏦
====================================

A complete banking system simulation with multiple accounts, deposits,
withdrawals, transfers, and transaction history.

Features:
- Multiple user accounts
- Create account
- Check balance
- Deposit and withdraw money
- Transfer between accounts
- Transaction history per account
- Persistent storage using JSON

This is the fifteenth project, representing a significant step toward real-world applications
with complex state management and financial logic.
"""

import json
from pathlib import Path
from typing import Dict, List, Any, Optional


FILE = Path("bank_accounts.json")


def load_accounts() -> Dict[str, Dict[str, Any]]:
    """Load accounts from JSON file or return empty dict."""
    if not FILE.exists():
        return {}

    try:
        with FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        print("⚠️  Error al leer el archivo. Iniciando con banco vacío.")
        return {}


def save_accounts(accounts: Dict[str, Dict[str, Any]]) -> None:
    """Save accounts to JSON file."""
    try:
        with FILE.open("w", encoding="utf-8") as file:
            json.dump(accounts, file, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"❌ Error al guardar las cuentas: {e}")


def create_account(accounts: Dict[str, Dict[str, Any]]) -> None:
    """Create a new bank account."""
    username = input("Nombre de usuario: ").strip().lower()

    if username in accounts:
        print("❌ El usuario ya existe.")
        return

    name = input("Nombre completo: ").strip()
    try:
        initial = float(input("Depósito inicial ($): ").strip())
        if initial < 0:
            print("❌ El depósito inicial no puede ser negativo.")
            return
    except ValueError:
        print("❌ Cantidad inválida.")
        return

    accounts[username] = {
        "name": name,
        "balance": initial,
        "transactions": []
    }

    save_accounts(accounts)
    print(f"✅ Cuenta creada para {name}.")


def get_account(accounts: Dict[str, Dict[str, Any]], username: str) -> Optional[Dict[str, Any]]:
    """Return account if it exists."""
    return accounts.get(username.lower())


def show_balance(accounts: Dict[str, Dict[str, Any]]) -> None:
    """Show account balance."""
    username = input("Usuario: ").strip()
    account = get_account(accounts, username)

    if not account:
        print("❌ Cuenta no encontrada.")
        return

    print(f"\nTitular: {account['name']}")
    print(f"Saldo actual: ${account['balance']:.2f}")


def deposit(accounts: Dict[str, Dict[str, Any]]) -> None:
    """Deposit money into an account."""
    username = input("Usuario: ").strip()
    account = get_account(accounts, username)

    if not account:
        print("❌ Cuenta no encontrada.")
        return

    try:
        amount = float(input("Cantidad a depositar: ").strip())
        if amount <= 0:
            print("❌ La cantidad debe ser mayor que 0.")
            return
    except ValueError:
        print("❌ Cantidad inválida.")
        return

    account["balance"] += amount
    account["transactions"].append({
        "type": "deposit",
        "amount": amount
    })

    save_accounts(accounts)
    print(f"✅ Depósito de ${amount:.2f} realizado. Nuevo saldo: ${account['balance']:.2f}")


def withdraw(accounts: Dict[str, Dict[str, Any]]) -> None:
    """Withdraw money from an account."""
    username = input("Usuario: ").strip()
    account = get_account(accounts, username)

    if not account:
        print("❌ Cuenta no encontrada.")
        return

    try:
        amount = float(input("Cantidad a retirar: ").strip())
        if amount <= 0:
            print("❌ La cantidad debe ser mayor que 0.")
            return
    except ValueError:
        print("❌ Cantidad inválida.")
        return

    if amount > account["balance"]:
        print("❌ Saldo insuficiente.")
        return

    account["balance"] -= amount
    account["transactions"].append({
        "type": "withdraw",
        "amount": amount
    })

    save_accounts(accounts)
    print(f"✅ Retiro de ${amount:.2f} realizado. Nuevo saldo: ${account['balance']:.2f}")


def transfer(accounts: Dict[str, Dict[str, Any]]) -> None:
    """Transfer money between accounts."""
    sender_username = input("Usuario origen: ").strip()
    sender = get_account(accounts, sender_username)

    if not sender:
        print("❌ Cuenta origen no encontrada.")
        return

    receiver_username = input("Usuario destino: ").strip()
    receiver = get_account(accounts, receiver_username)

    if not receiver:
        print("❌ Cuenta destino no encontrada.")
        return

    try:
        amount = float(input("Cantidad a transferir: ").strip())
        if amount <= 0:
            print("❌ La cantidad debe ser mayor que 0.")
            return
    except ValueError:
        print("❌ Cantidad inválida.")
        return

    if amount > sender["balance"]:
        print("❌ Saldo insuficiente en cuenta origen.")
        return

    sender["balance"] -= amount
    receiver["balance"] += amount

    sender["transactions"].append({
        "type": "transfer_out",
        "amount": amount,
        "to": receiver_username
    })

    receiver["transactions"].append({
        "type": "transfer_in",
        "amount": amount,
        "from": sender_username
    })

    save_accounts(accounts)
    print(f"✅ Transferencia de ${amount:.2f} realizada exitosamente.")


def show_transactions(accounts: Dict[str, Dict[str, Any]]) -> None:
    """Show transaction history for an account."""
    username = input("Usuario: ").strip()
    account = get_account(accounts, username)

    if not account:
        print("❌ Cuenta no encontrada.")
        return

    print(f"\n===== HISTORIAL DE {account['name'].upper()} =====")

    if not account["transactions"]:
        print("No hay movimientos registrados.")
        return

    for transaction in account["transactions"]:
        if transaction["type"] == "deposit":
            print(f"➕ Depósito     | ${transaction['amount']:.2f}")
        elif transaction["type"] == "withdraw":
            print(f"➖ Retiro       | ${transaction['amount']:.2f}")
        elif transaction["type"] == "transfer_out":
            print(f"↗️  Transferencia → {transaction.get('to', '???')} | ${transaction['amount']:.2f}")
        elif transaction["type"] == "transfer_in":
            print(f"↙️  Transferencia ← {transaction.get('from', '???')} | ${transaction['amount']:.2f}")


def main() -> None:
    """Main banking system loop."""
    accounts = load_accounts()

    print("🏦 PYBANK - Banco Digital")
    print("Gestión segura de tus finanzas.\n")

    while True:
        print("\n" + "=" * 45)
        print("1. Crear cuenta")
        print("2. Consultar saldo")
        print("3. Depositar")
        print("4. Retirar")
        print("5. Transferir")
        print("6. Ver historial")
        print("7. Salir")
        print("=" * 45)

        option = input("Selecciona una opción: ").strip()

        if option == "1":
            create_account(accounts)
        elif option == "2":
            show_balance(accounts)
        elif option == "3":
            deposit(accounts)
        elif option == "4":
            withdraw(accounts)
        elif option == "5":
            transfer(accounts)
        elif option == "6":
            show_transactions(accounts)
        elif option == "7":
            print("\n👋 Gracias por usar PyBank. ¡Hasta pronto!")
            break
        else:
            print("❌ Opción inválida.")


if __name__ == "__main__":
    main()
