# ────────────────────────────────────────────
# FILE: test_farming.py
# PURPOSE: Sense-driven test suite for farming logic
# RUN MODE: Only executed when RUN_MODE == "test" in main.py
# NOTES: Uses print-based PASS/FAIL feedback for in-engine TDD
# ────────────────────────────────────────────

def run_tests():
    print("\U0001F50D Running sense-based test suite...\n")

    test_harvest_hay()

    print("\n✅ All tests completed.")

def test_harvest_hay():
    print("▶️ Test: harvests hay if ready")

    initial = num_items(Items.Hay)

    if get_entity_type() != Entities.Hay:
        print("❌ FAIL: No hay under drone")
        return

    if not can_harvest():
        print("⚠️  Skipped: Hay not ready to harvest")
        return

    harvest()

    after = num_items(Items.Hay)
    if after == initial + 1:
        print("✅ PASS: Hay harvested successfully")
    else:
        print(f"❌ FAIL: Expected {initial + 1} hay, found {after}")
