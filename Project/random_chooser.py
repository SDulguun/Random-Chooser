#!/usr/bin/env python3
"""Random Chooser - Pick randomly from saved lists."""

import json
import random
import sys
from pathlib import Path

DATA_FILE = Path(__file__).parent / "chooser_lists.json"


def load_lists() -> dict:
    """Load saved lists from file."""
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text())
    return {}


def save_lists(lists: dict) -> None:
    """Save lists to file."""
    DATA_FILE.write_text(json.dumps(lists, indent=2))


def show_lists(lists: dict) -> None:
    """Display all saved lists."""
    if not lists:
        print("No lists saved yet. Create one with: add <list_name> <item>")
        return
    print("\n📋 Your Lists:")
    print("-" * 40)
    for name, items in lists.items():
        print(f"  {name}: {', '.join(items)}")
    print()


def pick_random(lists: dict, list_name: str) -> None:
    """Pick a random item from a list."""
    if list_name not in lists:
        print(f"List '{list_name}' not found. Use 'lists' to see available lists.")
        return
    if not lists[list_name]:
        print(f"List '{list_name}' is empty.")
        return
    choice = random.choice(lists[list_name])
    print(f"\n🎲 From '{list_name}': {choice}\n")


def add_item(lists: dict, list_name: str, item: str) -> None:
    """Add an item to a list (creates list if needed)."""
    if list_name not in lists:
        lists[list_name] = []
    if item in lists[list_name]:
        print(f"'{item}' already in '{list_name}'")
        return
    lists[list_name].append(item)
    save_lists(lists)
    print(f"Added '{item}' to '{list_name}'")


def remove_item(lists: dict, list_name: str, item: str) -> None:
    """Remove an item from a list."""
    if list_name not in lists:
        print(f"List '{list_name}' not found.")
        return
    if item not in lists[list_name]:
        print(f"'{item}' not in '{list_name}'")
        return
    lists[list_name].remove(item)
    save_lists(lists)
    print(f"Removed '{item}' from '{list_name}'")


def delete_list(lists: dict, list_name: str) -> None:
    """Delete an entire list."""
    if list_name not in lists:
        print(f"List '{list_name}' not found.")
        return
    del lists[list_name]
    save_lists(lists)
    print(f"Deleted list '{list_name}'")


def print_help() -> None:
    """Show usage instructions."""
    print("""
Random Chooser - Pick randomly from your saved lists

Commands:
  pick <list>              Pick random item from a list
  add <list> <item>        Add item to a list (creates list if new)
  remove <list> <item>     Remove item from a list
  delete <list>            Delete an entire list
  lists                    Show all saved lists
  help                     Show this help message
  quit                     Exit the program

Examples:
  add food Pizza
  add food "Pad Thai"
  add movies "The Matrix"
  pick food
  pick movies
""")


def interactive_mode() -> None:
    """Run in interactive mode."""
    lists = load_lists()
    print("\n🎲 Random Chooser - Type 'help' for commands\n")

    while True:
        try:
            user_input = input(">>> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break

        if not user_input:
            continue

        # Parse input respecting quotes
        parts = []
        current = ""
        in_quotes = False
        for char in user_input:
            if char == '"' and not in_quotes:
                in_quotes = True
            elif char == '"' and in_quotes:
                in_quotes = False
            elif char == ' ' and not in_quotes:
                if current:
                    parts.append(current)
                    current = ""
            else:
                current += char
        if current:
            parts.append(current)

        if not parts:
            continue

        cmd = parts[0].lower()

        if cmd in ('quit', 'exit', 'q'):
            print("Bye!")
            break
        elif cmd == 'help':
            print_help()
        elif cmd == 'lists':
            show_lists(lists)
        elif cmd == 'pick':
            if len(parts) < 2:
                print("Usage: pick <list_name>")
            else:
                pick_random(lists, parts[1])
        elif cmd == 'add':
            if len(parts) < 3:
                print("Usage: add <list_name> <item>")
            else:
                add_item(lists, parts[1], ' '.join(parts[2:]))
        elif cmd == 'remove':
            if len(parts) < 3:
                print("Usage: remove <list_name> <item>")
            else:
                remove_item(lists, parts[1], ' '.join(parts[2:]))
        elif cmd == 'delete':
            if len(parts) < 2:
                print("Usage: delete <list_name>")
            else:
                delete_list(lists, parts[1])
        else:
            print(f"Unknown command: {cmd}. Type 'help' for commands.")


def main() -> None:
    """Main entry point."""
    args = sys.argv[1:]

    # If no args, run interactive mode
    if not args:
        interactive_mode()
        return

    lists = load_lists()
    cmd = args[0].lower()

    if cmd == 'help':
        print_help()
    elif cmd == 'lists':
        show_lists(lists)
    elif cmd == 'pick' and len(args) >= 2:
        pick_random(lists, args[1])
    elif cmd == 'add' and len(args) >= 3:
        add_item(lists, args[1], ' '.join(args[2:]))
    elif cmd == 'remove' and len(args) >= 3:
        remove_item(lists, args[1], ' '.join(args[2:]))
    elif cmd == 'delete' and len(args) >= 2:
        delete_list(lists, args[1])
    else:
        print("Invalid command. Run with 'help' or no arguments for interactive mode.")


if __name__ == "__main__":
    main()
