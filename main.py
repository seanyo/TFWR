#Clear the farm
clear()

#Harvest the Farm

# TODO: Drone skips first two harvests - looks like the can_harvest 
# value is returning false. No idea why. This is sufficient for now. 


### Brute for Maze grinding to unlock Simulate with 100 chests
### maze has been spawned - ATR Maze solve code next

DIRECTIONS = [North, East, South, West]




# We'll track your current facing as an index into DIRECTIONS
facing = 0  # Start facing "up"

def turn_right():
    global facing
    facing = (facing + 1) % 4

def turn_left():
    global facing
    facing = (facing - 1) % 4

def turn_around():
    global facing
    facing = (facing + 2) % 4

def the_saratinia_protocol():
    global facing

    while True:
        if get_entity_type() == Entities.Treasure:
            harvest()
            print("🎉 Treasure found and harvested!")
            break

        # Check the direction to the right of current facing
        turn_right()
        right_dir = DIRECTIONS[facing]

        if move(right_dir):
            continue  # Successfully moved, keep walking

        # If can't go right, try straight ahead
        turn_left()  # Undo the right turn
        forward_dir = DIRECTIONS[facing]
        if move(forward_dir):
            continue

        # If can't go straight, try left
        turn_left()
        left_dir = DIRECTIONS[facing]
        if move(left_dir):
            continue

        # Otherwise, turn around and try going back
        turn_around()
        back_dir = DIRECTIONS[facing]
        move(back_dir)


while True:
    till()
    plant(Entities.Bush)
    use_item(Items.Weird_Substance, 6)
    the_saratinia_protocol()

# while True:
#     for column in range(get_world_size()): #Loop over each column
#         #print(column)
#         for row in range(get_world_size()): #Loop over each row in each column

#             if get_water() < 0.5:
#                 use_item(Items.Water)

#             if get_entity_type() != Entities.Bush:
#                 plant(Entities.Bush)
        
#             if get_entity_type() == Entities.Bush:
#                 for _ in range(1):  # Or however many times you want
#                     use_item(Items.Fertilizer)

#             if get_entity_type() != Entities.Cactus:
#                 till()
#                 plant(Entities.Cactus)

#             if can_harvest() == True:
#                 harvest()
#                 till()
#                 plant(Entities.Cactus)


#             if can_harvest():
#                 harvest()
#                 till()
#                 plant(Entities.Pumpkin)
#             else:
#                 till()
#                 plant(Entities.Pumpkin)

#             move(North)
#         move(East)

# Farming Trees

# def should_plant_tree(x, y):
#     return ((x%2 == 0 and y%2 == 0) or (x%2 == 1 and y%2 == 1))

# while True:
#     for column in range(get_world_size()): #Loop over each column
#         for row in range(get_world_size()): #Loop over each row in each column

#             # Get current position
#             x = get_pos_x()
#             y = get_pos_y()

#             if get_water() < 0.5:
#                 use_item(Items.Water)

#             if should_plant_tree(x, y):
#                 plant(Entities.Tree)
                    
#             if can_harvest():
#                 harvest()

#         move(North)
#     move(East)

