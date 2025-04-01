# main.py

# This file is required by the TFWR game engine.
# Runtime logic will call into simulate_tick or action functions here.

# Logic is modular and lives in /src

RUN_MODE = "play"  # or "play"

if RUN_MODE == "test":
    import test_farming
    test_farming.run_tests()

elif RUN_MODE == "play":
    while True:
        for column in range(get_world_size()):
            for row in range(get_world_size()):
                if can_harvest():
                    harvest()

                move(North)
            move(East)
