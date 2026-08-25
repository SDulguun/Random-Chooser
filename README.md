# Random Chooser

A Python tool that randomly picks from user-defined lists — what to eat, what to
watch, which task to do next. Available as **both a command-line tool and a
Streamlit web app**, sharing the same persistent JSON storage.

## Features

- Create and manage multiple named lists
- Randomly pick an item from any list
- Lists persist to a JSON file between runs
- Two interfaces over one data layer: CLI and web

## Run it

```bash
pip install -r Project/requirements.txt
```

```bash
streamlit run Project/app.py
```

```bash
python Project/random_chooser.py
```

## Layout

| File | Role |
|---|---|
| `Project/app.py` | Streamlit web interface |
| `Project/random_chooser.py` | Command-line interface |
| `Project/chooser_lists.json` | Saved lists |

---

*Early practice project — archived. See [Project/README.md](Project/README.md) for
the original notes.*
