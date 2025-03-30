#This code should be run in reborg.ca website

def turn_right(): 
    turn_left()
    turn_left()
    turn_left()

def avoid():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear(): 
        move()   
    turn_left()
    
while at_goal() == False: 
    if front_is_clear(): 
        move()
    elif wall_in_front(): 
        avoid()
    
    
    

    

