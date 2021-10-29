while not on_beeper():
    if  right_is_clear():
        repeat(turn_left,3)
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
turn_off()