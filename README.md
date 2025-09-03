# Agentic_1

A small, hands-on playground for **agentic / function-calling workflows** in Python, plus a simple **Calculator** demo with unit tests. The repo is intended for learning and quick experiments (routing function calls, validating tool schemas, and running a tiny CLI).

> If you’re just here to run something: jump to **[Quickstart](#quickstart)**.

---

## Table of Contents
- [What is this?](#what-is-this)
- [Repo Structure](#repo-structure)
- [Requirements](#requirements)
- [Quickstart](#quickstart)
- [Running the Calculator Demo](#running-the-calculator-demo)
- [Tests](#tests)
- [Configuration & Env Vars](#configuration--env-vars)
- [Development Notes](#development-notes)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

---

## What is this?

**Agentic_1** is a learning repo that explores:
- A **function-call router** that dispatches to local Python functions ("tools").
- **Typed schemas** for tool parameters (inspired by LLM function calling / JSON schema).
- A minimal **Calculator** package used by the router for real work.
- A couple of **CLI entry points** to try things quickly.

It’s intentionally small and hackable so you can read every file and tweak freely.

---

## Repo Structure

Your exact tree may differ a bit, but the project generally looks like this:

```
agentic_1/
├─ README.md
├─ render.py                # (example) simple CLI / demo runner
├─ calculator.py            # (example) function-call router, dispatch helpers
├─ main.py                  # (example) root CLI that talks to the router
├─ calculator/
│  ├─ __init__.py
│  ├─ main.py               # calculator entry point / tool wiring
│  └─ tests.py              # unit tests (unittest)
├─ pkg/                     # (optional) shared helpers
│  └─ __init__.py
├─ requirements.txt         # (optional if you use uv)
└─ .env.example             # (optional) template for env vars
```

> If your local structure is different, treat this as a guide. The commands below still apply with minor path tweaks.

---

## Requirements

- **Python** 3.11+ (recommended)
- One of:
  - **[uv](https://github.com/astral-sh/uv)** (fast Python package manager) — **recommended**
  - or **pip** + virtualenv
- (Optional) **Make** if you like Makefile shortcuts

---

## Quickstart

Clone and enter the repo:

```bash
git clone https://github.com/anthonytobiesq/agentic_1
cd agentic_1
```

### Option A: Using `uv` (recommended)

```bash
# create/activate a virtual env managed by uv and install deps
uv sync

# run a python file (uv handles the venv automatically)
uv run main.py --help
```

### Option B: Using pip

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python main.py --help
```

---

## Running the Calculator Demo

There are a few ways to play with the calculator and the router.

### 1) Run the calculator tests directly

```bash
uv run calculator/tests.py
# or
python calculator/tests.py
```

You should see something like:

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.000s

OK
```

### 2) Run the top-level CLI

If `main.py` exposes a simple prompt interface, you can try:

```bash
uv run main.py "what files are in the root?"
```

Replace the quoted question with any supported prompt or tool call your router understands.

### 3) Call the calculator module directly

```bash
uv run calculator/main.py --help
```

(Arguments depend on how you wired the CLI; examples:)
```bash
uv run calculator/main.py add --a 2 --b 3
uv run calculator/main.py expr "2 + 3 * (7 - 4)"
```

---

## Tests

This repo uses Python’s built-in **unittest** (simple and no extra deps).

```bash
# run all tests
uv run -m unittest discover -s . -p "tests.py"

# or directly
uv run calculator/tests.py
```

If you prefer **pytest**, you can add it and run:

```bash
uv add pytest
uv run -m pytest -q
```

---

## Configuration & Env Vars

If you use env variables (e.g., API keys), copy the example file and edit:

```bash
cp .env.example .env
```

Common variables you might add:

- `LOG_LEVEL=INFO` — set to DEBUG for more logs
- `WORKING_DIRECTORY=./calculator` — some routers expect this path

> Load order can vary; if you’re using `python-dotenv`, ensure it’s imported early in your entry script.

---

## Development Notes

- **Style**: keep it simple and readable. Type hints where they help.
- **Routing**: The function-call router should:
  1. Validate args against the tool schema.
  2. **Dispatch** to the correct handler.
  3. Always inject `working_directory` if a tool expects it.
- **Schema**: If you’re using typed schemas (e.g., via a small helper), keep them near the tool definitions so they’re easy to read.
- **Testing tips**:
  - Prefer **pure functions** for core logic so tests are easy.
  - Add happy-path and edge-case tests for each tool.
- **CLI**: Make commands idempotent; print clear errors instead of stack traces for user mistakes.

---

## Troubleshooting

- **`ModuleNotFoundError`**  
  Ensure you’re running from the repo root and the venv is active:
  ```bash
  uv run python -c "import sys, pprint; pprint.pprint(sys.path)"
  ```
  If a submodule isn’t found, try running with `-m` from the repo root:
  ```bash
  uv run -m calculator.tests
  ```

- **`No such file or directory` when running a path**  
  Run from the project root or give the correct relative path:
  ```bash
  uv run calculator/tests.py
  ```

- **Tests pass locally but fail in CI**  
  Pin versions (use `uv.lock` or `requirements.txt`) and avoid relying on the current working directory.

---

## Roadmap

- [ ] Add a `Makefile` with `make test`, `make run`, etc.
- [ ] Swap to `pytest` and coverage reports.
- [ ] Add a tiny JSON-RPC or FastAPI layer to expose the tools as an API.
- [ ] Ship a few more example tools (file search, grep, summarize…).
- [ ] Improve error messages and schema validation.

---

## Contributing

PRs welcome!  
Please:
1. Keep changes small and focused.
2. Add/Update tests for any new behavior.
3. Update this README if you change CLI behavior.

---

## License

Add your preferred license here (MIT is common for small learning projects).  
Create a `LICENSE` file at the repo root.

---

### Credits

Built by **Anthony Tobi** as a learning sandbox for agentic / function-calling patterns in Python.
