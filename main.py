#Clear the farm
clear()

#Harvest the Farm

# TODO: Drone skips first two harvests - looks like the can_harvest value is returning false. No idea why. This is sufficient for now. 


### Brute for Maze grinding to unlock Simulate with 100 chests

till()
plant(Entities.Bush)
use_item(Items.Weird_Substance, 6)

# while True:
#     for column in range(get_world_size()): #Loop over each column
#         #print(column)
#         for row in range(get_world_size()): #Loop over each row in each column

#             # if get_water() < 0.5:
#             #     use_item(Items.Water)

#             # if get_entity_type() != Entities.Bush:
#             #     plant(Entities.Bush)
        
#             # if get_entity_type() == Entities.Bush:
#             #     for _ in range(3):  # Or however many times you want
#             #         use_item(Items.Fertilizer)

#             if get_entity_type() != Entities.Cactus:
#                 till()
#                 plant(Entities.Cactus)

#             if can_harvest() == True:
#                 harvest()
#                 till()
#                 plant(Entities.Cactus)


#             # if can_harvest():
#             #     harvest()
#             #     till()
#             #     plant(Entities.Pumpkin)
#             # else:
#             #     till()
#             #     plant(Entities.Pumpkin)

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

