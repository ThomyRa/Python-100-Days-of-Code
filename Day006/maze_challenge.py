# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def turn_around():
#     turn_left()
#     turn_left()
    
# def right_side():
#     while not wall_on_right():
#         turn_right()

# def walls_check():
#     if right_is_clear():
#         turn_right()    
#     elif wall_in_front() and wall_on_right():
#         turn_left()
#         if wall_in_front() and wall_on_right():
#             turn_left()
#     elif wall_in_front() and not wall_on_right():
#         turn_right()
#     elif front_is_clear():
#         move()
    
# while front_is_clear():
#     move()
# right_side()
# while not at_goal():
#     if front_is_clear():
#         move()
#         walls_check()
#     else:
#         walls_check()