---
title: Release Notes
description: Historical version log and unlock state for TFWR.
---

# Release Notes

## v0.9.9 – Closure of V1: Discovery Engineering Complete

- This tag marks the formal end of the discovery-driven prototyping phase (V1), the start of V2: systems engineering, and the official adoption of Semantic Versioning.
 - https://semver.org/

**What V1 accomplished:**
- Developed a prototype maze solution
- Navigated and partially exploited moisture, tick, and crop mechanics
- Created separate exploratory branches per mechanic or unlock
- Focused on discovery of the API and prototyping/discovery code to generate sufficient resources to unlock most of the API
- Hit the "big unlock" point and completed the core gameplay R&D loop
 - Unlocking "Simulate" to enable TDD
- Maintained minimal abstraction for full control and learning

**Why mark this now:**
This isn't about usability—it's about ritual. V1 was discovery. V2 is architecture. A clean tag and release let me archive what worked, own what didn't, and move forward without rewriting the past.

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


---

## v1.6.0-pumpkins

- The overall structure of using unlocks for versions seems sufficient. Feels like there's a better way, but I'll likely need to finish the game to see that better way
- The timing of each branch was on unlock - but I don't think I've been exhausting the opportunity for each unlock
- Starting with this branch, I'm going to focus on "finishing" an unlock before merging it back into main. 

### The Big Unlock
- Hit a tipping point in resource gen that allowed some investment of run time to produce enough mats to mostly unlock the game. 
- Unlocks  
  (done)
    - watering  
    - fertilizer  
    - sunflowers  
    - debug  
    - operators  
    - senses  
    - variables  
    - lists  
    - functions  
  (to do)
    - cactus  
    - dinosaurs  
    - mazes  
    - dictionaries  
    - import  
    - utilities  
