#Clear the farm
clear()

#Harvest the Farm

# TODO: Drone skips first two harvests - looks like the can_harvest value is returning false. No idea why. This is sufficient for now. 
while True:
    for column in range(get_world_size()): #Loop over columns first
            for row in range(get_world_size()): #Loop over rows in each column

            if can_harvest():
                harvest()
                plant(Entities.Bush)

        move(North)
    move(East)

