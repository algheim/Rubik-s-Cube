cross_side = 5
opposite_side = 0

edge_list = [1, 3, 5, 7]
corner_list = [0, 2, 6, 8]


def decide_step(cube_list, step):
    if len(check_solved_edges(cube_list[0], 5)) < 4 and step < 1:
        return 0

    if len(check_solved_pieces(cube_list[0], 0)) == 9 and check_solved_f2l_edges(cube_list) == True:
        return 5

    if check_solved_f2l_edges(cube_list) == True and len(check_solved_edges(cube_list[5], 5)) == 4:
        return 4
    
    if (len(check_solved_pieces(cube_list[5], 5)) == 9 and cube_list[1][6] == 1 and cube_list[1][8] == 1
        and cube_list[3][0] == 3 and cube_list[3][2]):
        return 3
    
    elif len(check_solved_edges(cube_list[5], 5)) == 4:
        return 2
    else:
        return 1


def convert_sticker_order(side_number, sticker_number):
    if side_number == 0 or side_number == 1:
        return sticker_number

    elif side_number == 2:
        if sticker_number == 0:
            return 2
        elif sticker_number == 1:
            return 5
        elif sticker_number == 2:
            return 8
        elif sticker_number == 3:
            return 1
        elif sticker_number == 4:
            return 4
        elif sticker_number == 5:
            return 7
        elif sticker_number == 6:
            return 0
        elif sticker_number == 7:
            return 3
        elif sticker_number == 8:
            return 6

    elif side_number == 3:
        if sticker_number == 0:
            return 8
        elif sticker_number == 1:
            return 7
        elif sticker_number == 2:
            return 6
        elif sticker_number == 3:
            return 5
        elif sticker_number == 4:
            return 4
        elif sticker_number == 5:
            return 3
        elif sticker_number == 6:
            return 2
        elif sticker_number == 7:
            return 1
        elif sticker_number == 8:
            return 0

    elif side_number == 4:
        if sticker_number == 0:
            return 6
        elif sticker_number == 1:
            return 3
        elif sticker_number == 2:
            return 0
        elif sticker_number == 3:
            return 7
        elif sticker_number == 4:
            return 4
        elif sticker_number == 5:
            return 1
        elif sticker_number == 6:
            return 8
        elif sticker_number == 7:
            return 5
        elif sticker_number == 8:
            return 2

    else:
        return sticker_number

def move_converter(move, side_number):
    if move == "R":
        if side_number == 2:
            return "B"
        elif side_number == 3:
            return "L"
        elif side_number == 4:
            return "F"

    elif move == "R'":
        if side_number == 2:
            return "B'"
        elif side_number == 3:
            return "L'"
        elif side_number == 4:
            return "F'"

    elif move == "L":
        if side_number == 2:
            return "F"
        elif side_number == 3:
            return "R"
        elif side_number == 4:
            return "B"

    elif move == "L'":
        if side_number == 2:
            return "F'"
        elif side_number == 3:
            return "R'"
        elif side_number == 4:
            return "B'"

    elif move == "F":
        if side_number == 2:
            return "R"
        elif side_number == 3:
            return "B"
        elif side_number == 4:
            return "L"

    elif move == "F'":
        if side_number == 2:
            return "R'"
        elif side_number == 3:
            return "B'"
        elif side_number == 4:
            return "L'"

    return move
        
        
def check_solved_edges(side, color):
    solved_edges = []
    
    c = 0
    for sticker in side:
        if c in edge_list and sticker == color:
            solved_edges.append(c)

        c += 1

    return solved_edges

def check_solved_pieces(side, color):
    solved_pieces = []
    for sticker in side:
        if sticker == color:
            solved_pieces.append(sticker)

    return solved_pieces




#---------------------------------0---------------------------------------------

def cross_on_white(cube_list):
    solution = []
    
    for side in cube_list:
        if side[4] != 0:
            c = 0
            for sticker in side:
                if c in edge_list and sticker == cube_list[cross_side][4]:
                    solve_side = side[4]
                    solve_sticker = c

                c += 1

    converted_solve_sticker = convert_sticker_order(solve_side, solve_sticker)
    
    if solve_side == 5:
        if solve_sticker == 3:
            solution.append("L")
            solution.append("L")
                
        elif solve_sticker == 5:
            solution.append("R")
            solution.append("R")

        elif solve_sticker == 1:
            solution.append("F")
            solution.append("F")
                
        elif solve_sticker == 7:
            solution.append("B")
            solution.append("B")
        
    else:
        if converted_solve_sticker == 1:
            solution.append(move_converter("F", solve_side))
            solution.append(move_converter("U'", solve_side))
            solution.append(move_converter("R", solve_side))

        elif converted_solve_sticker == 3:
            solution.append(move_converter("L'", solve_side))

        elif converted_solve_sticker == 5:
            solution.append(move_converter("R", solve_side))

        elif converted_solve_sticker == 7:
            solution.append(move_converter("F'", solve_side))
            solution.append(move_converter("R", solve_side))
            solution.append(move_converter("F", solve_side))

    return solution

#--------------------------------1------------------------------------                

def cross_on_yellow(cube_list):
    solution = []
    solve_stickers = []
    
    c = 0
    for sticker in cube_list[0]:
        if c in edge_list and sticker == 5:
            solve_stickers.append(c)
        c += 1

    for solve_sticker in solve_stickers:
    
        if solve_sticker == 1:
            if cube_list[3][7] == cube_list[3][4]:
                solution.append("B")
                solution.append("B")

        elif solve_sticker == 3:
            if cube_list[4][5] == cube_list[4][4]:
                solution.append("L")
                solution.append("L")

        elif solve_sticker == 5:
            if cube_list[2][3] == cube_list[2][4]:
                solution.append("R")
                solution.append("R")

        elif solve_sticker == 7:
            if cube_list[1][1] == cube_list[1][4]:
                solution.append("F")
                solution.append("F")

    if len(solution) == 0:
        solution.append("U")
    
    return solution

#------------------------------------2------------------------------------

def calculate_corner_colors(cube_list, solve_side, converted_solve_sticker):

    if solve_side == 1:
        if converted_solve_sticker == 0:
            return (cube_list[0][6], cube_list[4][8])
        elif converted_solve_sticker == 2:
            return (cube_list[0][8], cube_list[2][6])

    elif solve_side == 2:
        if converted_solve_sticker == 0:
            return (cube_list[0][8], cube_list[1][2])
        elif converted_solve_sticker == 2:
            return (cube_list[0][2], cube_list[3][8])

    elif solve_side == 3:
        if converted_solve_sticker == 0:
            return (cube_list[0][2], cube_list[2][0])
        elif converted_solve_sticker == 2:
            return (cube_list[0][0], cube_list[4][2])

    elif solve_side == 4:
        if converted_solve_sticker == 0:
            return (cube_list[0][0], cube_list[3][6])
        elif converted_solve_sticker == 2:
            return (cube_list[0][6], cube_list[1][0])


    
def insert_corner(cube_list, solve_side, converted_solve_sticker):
    corner_colors = calculate_corner_colors(cube_list, solve_side, converted_solve_sticker)
    solve_side -= 1
    if solve_side < 1:
        solve_side = 4
        
    c = 0
    while True:
        if corner_colors[1] == solve_side:
            return ["U" for i in range(c)], solve_side
        else:
            solve_side -= 1
            if solve_side < 1:
                solve_side = 4

            c += 1


def calculate_empty_spots(cube_list):
    empty_spots = []
    c = 0
    for sticker in cube_list[5]:
        if c in corner_list and sticker != 5:
            if c == 0:
                empty_spots.append(6)
            elif c == 2:
                empty_spots.append(8)
            elif c == 6:
                empty_spots.append(0)
            elif c == 8:
                empty_spots.append(2)

        c += 1

    return empty_spots

    
def move_to_empty_spot(cube_list, converted_solve_sticker):
    solution = []
    
    empty_spots = calculate_empty_spots(cube_list)

    if converted_solve_sticker == 0:
        side = 3
    elif converted_solve_sticker == 2:
        side = 2
    elif converted_solve_sticker == 6:
        side = 4
    elif converted_solve_sticker == 8:
        side = 1

    
    while True:
        #print empty_spots, converted_solve_sticker
        if converted_solve_sticker in empty_spots:
            solution.append(move_converter("R", side))
            solution.append(move_converter("U", side))
            solution.append(move_converter("U", side))
            solution.append(move_converter("R'", side))
            return solution

        else:
            if converted_solve_sticker == 0:
                converted_solve_sticker = 2
            elif converted_solve_sticker == 2:
                converted_solve_sticker = 8
            elif converted_solve_sticker == 8:
                converted_solve_sticker = 6
            elif converted_solve_sticker == 6:
                converted_solve_sticker = 2
            solution.append("U")
            side -= 1
            if side < 1:
                side = 4
            
        

    
def yellow_corners(cube_list):
    solution = []
    upper_corner_sides = [0, 2]
    solve_side = None
    solve_sticker = None
    
    for side in cube_list:
        c = 0
        for sticker in side:
            if c in corner_list and side[4] != 0 and side[4] != 5 and sticker == 5:
                if convert_sticker_order(side[4], c) in upper_corner_sides:
                    solve_side = side[4]
                    solve_sticker = c
                    converted_solve_sticker = convert_sticker_order(solve_side, solve_sticker)

            c += 1


    if solve_side != None:
        solution, side = insert_corner(cube_list, solve_side, converted_solve_sticker)
        if converted_solve_sticker == 0:
            solution.append(move_converter("R", side))
            solution.append(move_converter("U", side))
            solution.append(move_converter("R'", side))
            
        elif converted_solve_sticker == 2:
            solution.append(move_converter("L'", side))
            solution.append(move_converter("U'", side))
            solution.append(move_converter("L", side))   

    else:
        for side in cube_list:
            c = 0
            for sticker in side:
                if c in corner_list and sticker == 5:
                    if side[4] == 0:
                        solution = move_to_empty_spot(cube_list, c)
                    else:
                        if convert_sticker_order(side[4], c) == 6:
                            solution.append(move_converter("L'", side[4]))
                            solution.append(move_converter("U", side[4]))
                            solution.append(move_converter("L", side[4]))
                        elif convert_sticker_order(side[4], c) == 8:
                            solution.append(move_converter("R", side[4]))
                            solution.append(move_converter("U'", side[4]))
                            solution.append(move_converter("R'", side[4]))
                        return solution

                c += 1

    return solution

#----------------------------3----------------------------------------------

def check_solved_f2l_edges(temp_cube_list):
    if temp_cube_list[1][3] != 1:
        return (1, 0)
    if temp_cube_list[1][5] != 1:
        return (1, 1)
    if temp_cube_list[2][1] != 2:
        return (2, 1)
    if temp_cube_list[2][7] != 2:
        return (2, 0)
    if temp_cube_list[3][3] != 3:
        return (3, 1)
    if temp_cube_list[3][5] != 3:
        return (3, 0)
    if temp_cube_list[4][1] != 4:
        return (4, 0)
    if temp_cube_list[4][7] != 4:
        return (4, 1)

    return True
    

def correct_solve_side(solve_side):
    if solve_side > 4:
        solve_side = 1

    if solve_side < 1:
        solve_side = 4

    return solve_side


def find_edge(cube_list):

    if cube_list[0][1] != 0 and cube_list[3][7] != 0:
            return(cube_list[0][1], cube_list[3][7]), 3

    elif cube_list[0][3] != 0 and cube_list[4][5] != 0:
            return(cube_list[0][3], cube_list[4][5]), 4

    elif cube_list[0][5] != 0 and cube_list[2][3] != 0:
            return(cube_list[0][5], cube_list[2][3]), 2

    elif cube_list[0][7] != 0 and cube_list[1][1] != 0:
            return(cube_list[0][7], cube_list[1][1]), 1

    else:
        return None, None


def insert_edge(cube_list, edge, solve_side):
    solution = []
    
    c = 0
    while True:
        if edge[1] == solve_side:
            next_solve_side = correct_solve_side(solve_side + 1)
            if edge[0] == next_solve_side:
                move_list = ["U", "R", "U'", "R'", "F", "R'", "F'", "R"]
            else:
                move_list = ["U'", "L'", "U", "L", "F'", "L", "F", "L'"]

            for move in move_list:
                solution.append(move_converter(move, solve_side))

            return solution

        solution.append("U'")
        solve_side = correct_solve_side(solve_side + 1)
    
    
def f2l_edges(cube_list):
    solution = []
    edge, solve_side = find_edge(cube_list)

    if edge != None:
        solution = insert_edge(cube_list, edge, solve_side)

    else:
        edge_pos = check_solved_f2l_edges(cube_list)
        if edge_pos[1] == 0:
            move_list = ["L'", "U", "L", "F'", "L", "F", "L'"]
        elif edge_pos[1] == 1:
            move_list = ["R", "U'", "R'", "F", "R'", "F'", "R"]

        for move in move_list:
            solution.append(move_converter(move, edge_pos[0]))

    return solution

#-----------------------------4---------------------------------------------
def check_solved_corners(side, color):
    solved_corners = []
    c = 0
    for sticker in side:
        if c in corner_list and sticker == color:
            solved_corners.append(c)
        c += 1

    return solved_corners
    
def orient_top_edges(cube_list):
    if cube_list[0][1] == 0 and cube_list[0][7] == 0:
        move_list = ["U", "F", "R", "U", "R'", "U'", "F'"]

    elif cube_list[0][3] == 0 and cube_list[0][5] == 0:
        move_list = ["F", "R", "U", "R'", "U'", "F'"]

    elif cube_list[0][7] == 0 and cube_list[0][5] == 0:
        move_list = ["F", "R", "U", "R'", "U'", "F'"]

    else:
        move_list = ["U"]

    return move_list
    

def solve_oll(cube_list):
    if len(check_solved_corners(cube_list[0], 0)) == 2:
        return ["R", "U", "U", "R'", "U'", "R", "U'", "R'"]

    if len(check_solved_corners(cube_list[0], 0)) == 0:
        if cube_list[3][8] == 0 and cube_list[1][2] == 0:
            if cube_list[1][0] == 0:
                return ["R", "U", "U", "R'", "U'", "R", "U", "R'", "U'", "R", "U'", "R'"]
            else:
                return ["R", "U", "U", "R", "R", "U'", "R", "R", "U'", "R", "R", "U", "U", "R"]
    
    if cube_list[0][2] == 0:
        if cube_list[2][6] == 0:
            return ["R", "U", "U", "R'", "U'", "R", "U'", "R'"]
        else:
            return ["U", "U", "R", "U", "R'", "U", "R", "U", "U", "R'"]

    return "U"

    
def oll(cube_list):
    oriented_edges = check_solved_edges(cube_list[0], 0)
    solution = []
    #print oriented_edges
    if len(oriented_edges) == 0:
        solution = ["F", "R", "U", "R'", "U'", "F'"]

    elif len(oriented_edges) == 2:
        solution = orient_top_edges(cube_list)

    elif len(oriented_edges) == 4:
        solution = solve_oll(cube_list)

    return solution

#------------------------------5-------------------------------------------

def check_head_lights(cube_list):
    head_lights_list = []
    if cube_list[1][0] == cube_list[1][2]:
        head_lights_list.append(1)
    if cube_list[2][0] == cube_list[2][6]:
        head_lights_list.append(2)
    if cube_list[3][6] == cube_list[3][8]:
        head_lights_list.append(3)
    if cube_list[4][2] == cube_list[4][8]:
        head_lights_list.append(4)

    return head_lights_list

        
def check_bar(cube_list):
    if cube_list[1][0] == cube_list[1][1]:
        return 1
    if cube_list[2][0] == cube_list[2][3]:
        return 2
    if cube_list[3][6] == cube_list[3][7]:
        return 3
    if cube_list[4][2] == cube_list[4][5]:
        return 4

    return None


def u_perm(cube_list):
    if cube_list[1][1] == cube_list[4][5]:
        move_list = ["R", "R", "U", "R", "U", "R'", "U'", "R'", "U'", "R'", "U", "R'"]
    else:
        move_list = ["R", "U'", "R", "U", "R", "U", "R", "U'", "R'", "U'", "R", "R"]

    return move_list
        
    
def pll(cube_list):
    head_lights_list = check_head_lights(cube_list)
    move_list = ["U"]
    if len(head_lights_list) == 4:
        bar_pos = check_bar(cube_list)
        if bar_pos == None:
            move_list = ["R", "R", "U", "R", "U", "R'", "U'", "R'", "U'", "R'", "U", "R'"]
        elif bar_pos == 3:
            move_list = u_perm(cube_list)
        else:
            move_list = ["U"]

    elif len(head_lights_list) == 1:
        if 4 in head_lights_list:
            move_list = ["R", "U", "R'", "U'", "R'", "F", "R", "R", "U'", "R'", "U'", "R", "U", "R'", "F'"]
        else:
            move_list = ["U"]

    elif len(head_lights_list) == 0:
        move_list = ["F", "R", "U'", "R'", "U'", "R", "U", "R'", "F'", "R", "U", "R'", "U'", "R'", "F", "R", "F'"]

    return move_list

    
        
#---------------------------main-------------------------------------------


def main(cube_list, step):
    solution = []
    step = decide_step(cube_list, step)

    if step == 0:
        solution = cross_on_white(cube_list)

    elif step == 1:
        solution = cross_on_yellow(cube_list)

    elif step == 2:
        solution = yellow_corners(cube_list)

    elif step == 3:
        solution = f2l_edges(cube_list)

    elif step == 4:
        solution = oll(cube_list)

    elif step == 5:
        solution = pll(cube_list)

    return solution, step

    









