#Clear the farm
clear()

#Harvest the Farm

while True:
    for row in range(get_world_size()):
        for column in range(get_world_size()):

            if can_harvest():
                harvest()
                plant(Entities.Bush)
                move(East)
        move(North)

