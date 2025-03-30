#Project developed in reeborg.ca (Scape from the maze)

def turn_right(): 
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal(): 
    while right_is_clear():
        turn_right()
        move()
        
    while wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()