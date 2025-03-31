# 📊 Seed Prompt: Learning TDD Using *The Farmer Was Replaced*

---

## Part 1: TDD Philosophy and Practice (General)

I want to improve my skills in **Test-Driven Development (TDD)**. I'm especially interested in using TDD to:

- Drive better **system design** through incremental testing  
- Think in terms of **behaviors, state transitions**, and **intent**  
- Follow the **red-green-refactor** loop effectively  
- Understand when to write **unit**, **integration**, or **system** tests  
- Use **fixtures and snapshots** to structure repeatable, reliable tests  
- Create tests that act as **documentation and architecture constraints**  

**Guiding Principles:**
- Start from **expected outcomes**, not implementation  
- Know when and how to **isolate vs. compose**  
- Use **test failures as design feedback**  
- Keep tests **readable, focused**, and **low-maintenance**  
- Favor **behaviors over implementation details**

I'm using a Python-like language and writing all tests myself—no framework-specific constraints yet.  
Please help me build strong TDD instincts and architectural intuition, not just pass tests.

---

## Part 2: TDD in *The Farmer Was Replaced* (TFWR)

### 🧐 Why TDD for TFWR?

TFWR is an emergent simulation game. The drone's actions interact with a dynamic world.  
TDD helps us:
- Encode clear **game mechanics**
- Design clean **behavior modules**
- Avoid regressions as complexity increases
- Ensure **simulation logic** stays consistent across ticks

---

### 🧌 Project Context

My codebase includes:
- A **sparse layered grid** model of the farm (`farm_state`)  
- **Glyph/emoji rendering** for visual feedback  
- Modular logic for actions like `move()`, `plant()`, `harvest()`, `water()`  
- Unlockable mechanics: `simulate`, `maze`, `auto_unlock`  
- A `/tests/` directory with reusable fixtures (`/fixtures/`)  
- Full simulation snapshots for tick-by-tick verification  

---

### 🧪 TDD Questions I Want to Explore

Examples:
- How should I test that `plant()` only works on a tilled tile?  
- How can I test that `move()` avoids impassable walls or maze edges?  
- How should I write a test that verifies a full cactus harvest loop using snapshot simulation?  
- What makes a good test fixture like `cactus_grid.json` or `empty_farm.json`?  
- How do I layer tests: one for `render_glyph()`, one for `farm_state.update()`, and one for the full drone behavior?

---

### 🧱 TFWR Testing Pyramid (Heuristic)

```
        🔼 Snapshot Tests      (Tick-by-tick loops, behavior arcs)
      🔼 Integration Tests     (farm_state + rendering, unlock flow)
    🔼 Unit Tests              (move(), plant(), render_glyph())
  🔼 Pure Logic Tests          (adjacency checks, input validation, grid math)
```

Start low, verify fast. Climb the pyramid to prove behaviors.  
Snapshot tests are high value, but slow and brittle—use for milestone behaviors.

---

### ⏱ TDD + Simulation Tick

Each **tick** in the game advances the simulation. TDD should:
- Predict and assert world state **after N ticks**
- Use **simulation loops** as behavioral validators
- Anchor state changes to **expected tick transitions**

**Example:**
```
Given a drone on (3,2) and a tilled tile at (3,3)  
When `plant()` is called and a seed is in inventory  
Then after 1 tick, a seedling appears at (3,3)
```

---

