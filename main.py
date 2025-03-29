#Clear the farm
clear()

#Harvest the Farm

# TODO: Drone skips first two harvests - looks like the can_harvest value is returning false. No idea why. This is sufficient for now. 
while True:
    for column in range(get_world_size()): #Loop over each column
            for row in range(get_world_size()): #Loop over each row in each column
                 
                if can_harvest():
                    harvest()
                    #till()
                    plant(Entities.Tree)

            move(North)
    move(East)

