# TFWR V1 Roadmap: Discovery Engineering

## Overview
This document marks the formal closure of Version 1 (V1) of The Farmer Was Replaced (TFWR) project. V1 was the "discovery engineering" phase: an exploratory, prototype-driven journey to reverse-engineer the game mechanics, unlock capabilities, and build enough momentum to reach the simulation layer.

This version was not built for reuse—it was built for *learning*.

---

## Goals of V1
- Reverse-engineer in-game simulation mechanics
- Prototype basic automation (e.g., cactus harvesting)
- Explore moisture, tilling, planting, and harvesting behaviors
- Create working logic without abstraction, using branches as experiments
- Use manual play to unlock the game's advanced features (e.g., `simulate`)


## Key Strategies
- **Branch-by-branch learning**: Each major mechanic explored in its own Git branch (e.g., `plant`, `trees`, `water`, `speed`, `expand`)
- **Zero abstraction**: All logic lived in `main.py` for complete control and traceability
- **Unlock-focused development**: Feature exploration was tied to game unlocks
- **Visual debugging**: Used `quick_print()` 
- **Brute-force maze exploration**: Manual effort used to unlock the simulation layer

**What V1 accomplished:**
- Developed a prototype maze solution
- Navigated and partially exploited moisture, tick, and crop mechanics
- Created separate exploratory branches per mechanic or unlock
- Focused on discovery of the API and prototyping/discovery code to generate sufficient resources to unlock most of the API
- Hit the "big unlock" point and completed the core gameplay R&D loop
 - Unlocking "Simulate" to enable TDD
- Maintained minimal abstraction for full control and learning

> V2 begins with:
> - TDD
> - Modular code (actions, crops, tests, render)
> - A sparse layered `farm_state`
> - Simulation-based snapshot testing
> - Real documentation, built to scale

## 🗺️ Unlock Tree Progress

### Legend

| Status    | Symbol | Meaning                             |
|-----------|--------|-------------------------------------|
| ✅ Done    | `[✓]`  | Fully unlocked or max level reached |
| 🛠️ In Progress | `[~]`  | Currently being worked on           |
| ⏳ Not Started | `[ ]`  | Unlock path exists but untouched     |

[✓] **Loops**
├── [✓] Speed _(Upgrade)_
│   └── [✓] Expand _(Upgrade)_
│       ├── [✓] Carrots _(Max Level)_
│       │   └── [✓] Watering _(Max Level)_
│       │       └── [✓] Fertilizer _(Upgrade)_
│       └── [✓] Trees _(Max Level)_
│           ├── [✓] Sunflowers _(Unlocked)_
│           ├── [~] Cactus _(Upgrade)_
│           ├── [~] Dinosaurs _(Upgrade)_
│           └── [~] Mazes _(Upgrade)_
│               └── [ ] Polyculture _(Unlock)_
├── [✓] Grass _(Max Level)_
└── [✓] Plant _(Unlocked)_

[✓] **Debug**
├── [~] Debug_2 _(Unlock)_
│   └── [~] Simulation _(Unlock)_
│       └── [ ] Leaderboard _(Locked)_
├── [✓] Timing _(Unlocked)_

[✓] **Operators**
├── [✓] Senses _(Unlocked)_
│   └── [✓] Lists _(Unlocked)_
│       └── [✓] Dictionaries _(Unlocked)_
│           └── [✓] Costs _(Unlocked)_
│               └── [ ] Auto_Unlock _(Unlock)_
├── [✓] Variables _(Unlocked)_
│   └── [✓] Functions _(Unlocked)_
│       ├── [✓] Import _(Unlocked)_
│       └── [✓] Utilities _(Unlocked)_



## What V1 Taught
- Game unlocks are the real unit of progress—every branch and mechanic was in service of unlocking the next capability
- Building without abstraction allowed maximal learning and debugging clarity
- A systems architecture would be required to progress any further


## Transition to V2
> "This isn't about usability—it's about ritual. V1 was discovery. V2 is architecture."

V2 begins with:
- Modular code structure (e.g., `src/actions`, `src/crops`, `src/tests`)
- Sparse, layered `farm_state`
- Snapshot-driven testing
- Real documentation, systematized and extensible
- Architectural framing around automation, not just exploration