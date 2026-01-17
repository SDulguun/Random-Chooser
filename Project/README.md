# Random Chooser

A Python tool that randomly picks from user-defined lists. Useful for deciding things like what to eat, what movie to watch, or which task to do next.

Available as both a **command-line tool** and a **web app**.

## Features

- Create and manage multiple named lists
- Randomly pick items from any list
- Persistent storage (lists are saved to a JSON file)
- Two interfaces: CLI and Web App (Streamlit)

## Requirements

- Python 3.6 or higher
- Streamlit (for web app only)

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Web App (Streamlit)

Run the web interface:

```bash
streamlit run app.py
```

This opens a browser with three tabs:
- **Pick Random** - Select a list and pick a random item
- **Manage Lists** - View and delete items/lists
- **Add Items** - Create new lists and add items

### Command-Line Mode

Run commands directly from the terminal:

```bash
python3 random_chooser.py <command> [arguments]
```

### Interactive Mode

Run without arguments to enter interactive mode:

```bash
python3 random_chooser.py
```

## CLI Commands

| Command | Description | Example |
|---------|-------------|---------|
| `add <list> <item>` | Add an item to a list | `add food Pizza` |
| `pick <list>` | Pick a random item | `pick food` |
| `remove <list> <item>` | Remove an item | `remove food Pizza` |
| `delete <list>` | Delete an entire list | `delete food` |
| `lists` | Show all saved lists | `lists` |
| `help` | Show help message | `help` |

## Examples

```bash
# Add items to a "food" list
python3 random_chooser.py add food Pizza
python3 random_chooser.py add food Sushi
python3 random_chooser.py add food "Pad Thai"

# Pick a random food
python3 random_chooser.py pick food

# View all lists
python3 random_chooser.py lists
```

## File Structure

```
Project/
├── app.py              - Streamlit web app
├── random_chooser.py   - Command-line program
├── chooser_lists.json  - Saved lists data (created automatically)
├── requirements.txt    - Project dependencies
└── README.md           - This file
```
