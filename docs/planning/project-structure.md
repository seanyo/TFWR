# TFWR Project Structure (V2)

**Version:** 2.0.0-alpha  
**Status:** Active (WIP)

This document defines the canonical project layout for Version 2 (V2) of *The Farmer Was Replaced* (TFWR). It includes directory conventions, architectural rationale, and guidance on where different types of content should live.

> V1 was exploratory; V2 is architectural.

---

## 📁 Top-Level Layout

```text
TFWR/
├── src/          # Core logic and system code
├── tests/        # Test files and fixtures
├── docs/         # Project documentation
├── main.py       # Entry point (sim runner or CLI)
├── save.json     # Game save file (external input)
├── README.md     # High-level project intro
├── requirements.txt  # Optional, for tooling/dev
```


## 🔧 `/src/` — Core Logic
Modular, layered architecture organized by domain and purpose.

```text
src/
├── actions/      # Core verbs the drone can perform (e.g. plant, move)
├── crops/        # Crop-specific behaviors and constants
├── maze/         # Maze-solving strategies (optional)
├── farm_state.py # Sparse grid model of farm tiles
├── render.py     # Glyph-based rendering layer
├── config.py     # Constants, enums, entity aliases
```


## 🧪 `/tests/` — Automated Tests
Home for test cases, fixtures, and test-only utilities.

```text
tests/
├── fixtures/          # Reusable test states (e.g. cactus_grid.json)
├── test_farm_state.py
├── test_cactus.py
├── test_movement.py
├── test_maze.py
```

> Future tests may include snapshot-based simulation flows once `simulate` is fully unlocked.


## 🧾 `/docs/` — Project Documentation
Split into logical categories to support modular growth and long-term maintainability.

```text
docs/
├── architecture/       # System blueprints, design patterns
├── planning/           # Roadmaps, structure specs, decision logs
├── crops/              # Domain-specific notes on game mechanics
├── tests/              # Test strategy, examples, and TDD seed prompts
```

### Examples:
- `architecture/farm_state.md` → Design and layering of the tile model
- `planning/v1-roadmap.md` → V1 closure summary
- `planning/project-structure.md` → This file
- `tests/tdd-seed.md` → Structured prompt for test-driven thinking


## 📚 Conventions

| Area               | Rule                                                       |
|--------------------|------------------------------------------------------------|
| Code Style         | PEP8-ish, but optimized for clarity over dogma             |
| File Naming        | `snake_case.py` for code, `kebab-case.md` for docs         |
| Testing            | `pytest` + manual simulation snapshots                     |
| Versioning         | Follows SemVer (`v2.0.0-alpha`, etc)                       |
| Commit Messages    | Uses structured prefixes (`feat:`, `fix:`, `pause:`, etc) |


## 🔜 Future Work
- Add `/tools/` if helper scripts emerge
- Add `/scripts/` if packaging or CLI automation is required
- Add `/sim/` or `/replays/` if storing snapshot test results or demo runs

---

> This structure is maintained and versioned under `docs/planning/project-structure.md`.
> Updated in alignment with `v2.0.0-alpha` kick-off.

