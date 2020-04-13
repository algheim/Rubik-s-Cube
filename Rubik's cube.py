import pygame as p
import time
import reverse_scramble
import beginner_method

p.init()

solve_speed = 8 #moves / second
length = 600
height = length * 5 / 4

white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
orange = (255,100,0)
yellow = (255,255,0)

win = p.display.set_mode((int(length), int(height)))
clock = p.time.Clock()

edge_list = [1, 3, 5, 7]


def check_event():
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            quit()

        if event.type == p.MOUSEBUTTONDOWN:
            return (event.pos, event.button)


def wait_for_input():
    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()

            if event.type == p.MOUSEBUTTONDOWN:
                return


def calculate_move(event):
    if event == None:
        return

    move = ""

    x = event[0][0]
    y = event[0][1]
    button = event[1]

    button_length = length / 8

    if length * 3 / 16 < x < length * 3 / 16 + button_length:

        if height * 3 / 20 < y < height * 3 / 20 + button_length:

            return "reverse scramble"

        for i in range(3):
            if height * 11 / 20 + button_length * i < y < height * 11 / 20 + button_length * (i + 1):
                if i == 0:
                    move = "L"
                elif i == 1:
                    move = "D"
                elif i == 2:
                    move = "B"

    elif length * 11 / 16 < x < length * 11 / 16 + button_length:

        if height * 3 / 20 < y < height * 3 / 20 + button_length:
            return "beginner method"

        for i in range(3):
            if height * 11 / 20 + button_length * i < y < height * 11 / 20 + button_length * (i + 1):
                if i == 0:
                    move = "R"
                elif i == 1:
                    move = "U"
                elif i == 2:
                    move = "F"

    if move == "":
        return

    if button == 3:
        move += "'"

    return move


def rotate_clock_wise(side):
    original = []
    for sticker in side:
        original.append(sticker)

    side[0] = original[6]
    side[1] = original[3]
    side[2] = original[0]
    side[3] = original[7]
    side[4] = original[4]
    side[5] = original[1]
    side[6] = original[8]
    side[7] = original[5]
    side[8] = original[2]

    return side


def rotate_counter_clock_wise(side):
    original = []
    for sticker in side:
        original.append(sticker)

    side[0] = original[2]
    side[1] = original[5]
    side[2] = original[8]
    side[3] = original[1]
    side[4] = original[4]
    side[5] = original[7]
    side[6] = original[0]
    side[7] = original[3]
    side[8] = original[6]

    return side


def move_counter_clock_wise(cube_list, swap_sides, rotate_side, swap_pieces, reverse_list = []):

    temp = []
    c = 0
    for side in swap_sides:
        temp.append([cube_list[side][swap_pieces[c][0]], cube_list[side][swap_pieces[c][1]],
                     cube_list[side][swap_pieces[c][2]]])

        c += 1

    c = -1
    for side in swap_sides:
        if c not in reverse_list or reverse_list == []:
            cube_list[side][swap_pieces[c + 1][0]] = temp[c][0]
            cube_list[side][swap_pieces[c + 1][1]] = temp[c][1]
            cube_list[side][swap_pieces[c + 1][2]] = temp[c][2]
        else:
            cube_list[side][swap_pieces[c + 1][2]] = temp[c][0]
            cube_list[side][swap_pieces[c + 1][1]] = temp[c][1]
            cube_list[side][swap_pieces[c + 1][0]] = temp[c][2]



        c += 1

    return cube_list


def move_clock_wise(cube_list, swap_sides, rotate_side, swap_pieces, reverse_list = []):

    c = 0
    temp = []
    for side in swap_sides:

        temp.append([cube_list[side][swap_pieces[c][0]], cube_list[side][swap_pieces[c][1]],
                     cube_list[side][swap_pieces[c][2]]])

        c += 1

    c = 0
    for side in swap_sides:
        if c > 2:
            c = -1

        if c not in reverse_list or reverse_list == None:
            cube_list[side][swap_pieces[c][0]] = temp[c + 1][0]
            cube_list[side][swap_pieces[c][1]] = temp[c + 1][1]
            cube_list[side][swap_pieces[c][2]] = temp[c + 1][2]
        else:
            cube_list[side][swap_pieces[c][2]] = temp[c + 1][0]
            cube_list[side][swap_pieces[c][1]] = temp[c + 1][1]
            cube_list[side][swap_pieces[c][0]] = temp[c + 1][2]

        c += 1

    return cube_list


def make_move(cube_list, move):

    if move == "R":
        swap_sides = [0, 1, 5, 3]
        rotate_side = 2
        swap_pieces = [[2, 5, 8], [2, 5, 8], [2, 5, 8], [2, 5, 8]]
        cube_list = move_clock_wise(cube_list, swap_sides, rotate_side, swap_pieces)
        cube_list[rotate_side] = rotate_clock_wise(cube_list[rotate_side])

    elif move == "R'":
        swap_sides = [0, 1, 5, 3]
        rotate_side = 2
        swap_pieces = [[2, 5, 8], [2, 5, 8], [2, 5, 8], [2, 5, 8]]
        cube_list = move_counter_clock_wise(cube_list, swap_sides, rotate_side, swap_pieces)
        cube_list[rotate_side] = rotate_counter_clock_wise(cube_list[rotate_side])

    elif move == "U":
        swap_sides = [1, 4, 3, 2]
        rotate_side = 0
        swap_pieces = [[0, 1, 2], [2, 5, 8], [6, 7, 8], [0, 3, 6]]
        cube_list = move_counter_clock_wise(cube_list, swap_sides, rotate_side, swap_pieces, [-1, 1])
        cube_list[rotate_side] = rotate_clock_wise(cube_list[rotate_side])

    elif move == "U'":
        swap_sides = [1, 4, 3, 2]
        rotate_side = 0
        swap_pieces = [[0, 1, 2], [2, 5, 8], [6, 7, 8], [0, 3, 6]]
        cube_list = move_clock_wise(cube_list, swap_sides, rotate_side, swap_pieces, [-1, 1])
        cube_list[rotate_side] = rotate_counter_clock_wise(cube_list[rotate_side])

    elif move == "F":
        swap_sides = [0, 2, 5, 4]
        rotate_side = 1
        swap_pieces = [[6, 7, 8], [6, 7, 8], [0, 1, 2], [6, 7, 8]]
        cube_list = move_counter_clock_wise(cube_list, swap_sides, rotate_side, swap_pieces, [1, 2])
        cube_list[rotate_side] = rotate_clock_wise(cube_list[rotate_side])

    elif move == "F'":
        swap_sides = [0, 2, 5, 4]
        rotate_side = 1
        swap_pieces = [[6, 7, 8], [6, 7, 8], [0, 1, 2], [6, 7, 8]]
        cube_list = move_clock_wise(cube_list, swap_sides, rotate_side, swap_pieces, [1, 2])
        cube_list[rotate_side] = rotate_counter_clock_wise(cube_list[rotate_side])

    elif move == "L":
        swap_sides = [0, 1, 5, 3]
        rotate_side = 4
        swap_pieces = [[0, 3, 6], [0, 3, 6], [0, 3, 6], [0, 3, 6]]
        cube_list = move_counter_clock_wise(cube_list, swap_sides, rotate_side, swap_pieces)
        cube_list[rotate_side] = rotate_clock_wise(cube_list[rotate_side])

    elif move == "L'":
        swap_sides = [0, 1, 5, 3]
        rotate_side = 4
        swap_pieces = [[0, 3, 6], [0, 3, 6], [0, 3, 6], [0, 3, 6]]
        cube_list = move_clock_wise(cube_list, swap_sides, rotate_side, swap_pieces)
        cube_list[rotate_side] = rotate_counter_clock_wise(cube_list[rotate_side])

    elif move == "D":
        swap_sides = [1, 4, 3, 2]
        rotate_side = 5
        swap_pieces = [[6, 7, 8], [0, 3, 6], [0, 1, 2], [2, 5, 8]]
        cube_list = move_clock_wise(cube_list, swap_sides, rotate_side, swap_pieces, [1, -1])
        cube_list[rotate_side] = rotate_clock_wise(cube_list[rotate_side])

    elif move == "D'":
        swap_sides = [1, 4, 3, 2]
        rotate_side = 5
        swap_pieces = [[6, 7, 8], [0, 3, 6], [0, 1, 2], [2, 5, 8]]
        cube_list = move_counter_clock_wise(cube_list, swap_sides, rotate_side, swap_pieces, [1, -1])
        cube_list[rotate_side] = rotate_counter_clock_wise(cube_list[rotate_side])

    elif move == "B":
        swap_sides = [0, 4, 5, 2]
        rotate_side = 3
        swap_pieces = [[0, 1, 2], [0, 1, 2], [6, 7, 8], [0, 1, 2]]
        cube_list = move_counter_clock_wise(cube_list, swap_sides, rotate_side, swap_pieces, [2, 1])
        cube_list[rotate_side] = rotate_clock_wise(cube_list[rotate_side])

    elif move == "B'":
        swap_sides = [0, 4, 5, 2]
        rotate_side = 3
        swap_pieces = [[0, 1, 2], [0, 1, 2], [6, 7, 8], [0, 1, 2]]
        cube_list = move_clock_wise(cube_list, swap_sides, rotate_side, swap_pieces, [2, 1])
        cube_list[rotate_side] = rotate_counter_clock_wise(cube_list[rotate_side])


    return cube_list


#------------------------------auto-solve-------------------------------------------------

def check_solved_f2l_edges(temp_cube_list):

    if temp_cube_list[1][3] != 1 or temp_cube_list[1][5] != 1:
        return False

    if temp_cube_list[2][1] != 2 or temp_cube_list[2][7] != 2:
        return False

    if temp_cube_list[3][3] != 3 or temp_cube_list[3][5] != 3:
        return False

    if temp_cube_list[4][1] != 4 or temp_cube_list[4][7] != 4:
        return False

    return True

def copy_cube_list(cube_list):
    old_cube_list = [[0,0,0,0,0,0,0,0,0]for i in range(6)]

    for side in range(len(cube_list)):
        c = 0
        for sticker in cube_list[side]:
            old_cube_list[side][c] = sticker
            c += 1

    return old_cube_list


def check_solved_edges(side, color):
    solved_edges = []

    c = 0
    for sticker in side:
        if c in edge_list and sticker == color:
            solved_edges.append(color)

        c += 1

    return solved_edges


def check_progress(temp_cube_list, move_list, step):

    old_cube_list = copy_cube_list(temp_cube_list)

    if step == 0:
        solved_edges_before = check_solved_edges(temp_cube_list[0], 5)

        for move in move_list:
            temp_cube_list = make_move(temp_cube_list, move)

        solved_edges_after = check_solved_edges(temp_cube_list[0], 5)

        if len(solved_edges_after) > len(solved_edges_before):
            return True, old_cube_list
        else:
            return False, old_cube_list


    elif step == 1 or step == 2 or step == 3 or step == 4 or step == 5:
        return True, old_cube_list


def beginnerMethod(cube_list):
    temp_cube_list = copy_cube_list(cube_list)

    solved = False
    solution = []
    step = 0

    start = time.time()

    while not solved:
        move_list, step = beginner_method.main(temp_cube_list, step)
        progress, temp_cube_list = check_progress(temp_cube_list, move_list, step)

        #print(step, temp_cube_list)
        #time.sleep(0.5)

        if progress:
            for move in move_list:
                temp_cube_list = make_move(temp_cube_list, move)
                solution.append(move)

        else:
            temp_cube_list = make_move(temp_cube_list, "U")
            solution.append("U")

        if check_if_solved(temp_cube_list):
            solved = True

    solve_time = time.time() - start

    print (solve_time, len(solution))
    return solution


def check_if_solved(cube_list):

    for side in cube_list:
        for sticker in side:
            if sticker != side[4]:
                return False

    return True


def calculate_scramble(scramble, move, solved):
    if solved:
        return []

    if move == None or move == "beginner method" or move == "reverse scramble":
        return scramble

    else:
        scramble.append(move)
        return scramble


def solve_cube(cube_list, scramble, move):
    if move != "beginner method" and move != "reverse scramble":
        return cube_list

    if move == "reverse scramble":
        solution = reverse_scramble.reverse(scramble)

    elif move == "beginner method":
        solution = beginnerMethod(cube_list)

    for move in solution:

        scramble.append(move)
        event = check_event()
        cube_list = make_move(cube_list, move)
        draw_cube(cube_list, move)
        clock.tick(solve_speed)

    return cube_list

#------------------------------Draw:------------------------------------------------------

def write_text(txt ,x, y, size, color):
    size = int(size * 0.75)
    text = p.font.SysFont('arialblack', size)
    textsurface = text.render(txt, False, color)
    win.blit(textsurface, (x,y))


def calculate_letter(c):
    if c == 0:
        return "L"
    elif c == 1:
        return "D"
    elif c == 2:
        return "B"
    elif c == 3:
        return "R"
    elif c == 4:
        return "U"
    elif c == 5:
        return "F"


def calculate_color(n):
    if n == 0:
        return white
    elif n == 1:
        return green
    elif n == 2:
        return red
    elif n == 3:
        return blue
    elif n == 4:
        return orange
    elif n == 5:
        return yellow


def draw_buttons():
    x = int(length * 3 / 16)
    Y = int(height * 11 / 20)
    button_length = length / 8
    text_size = button_length / 2

    c = 0
    for i in range(3):
        y = Y + button_length * i
        p.draw.rect(win, (200,200,200), (x, y, button_length, button_length))
        p.draw.lines(win, (0,0,0), True, [(int(x), int(y)), (x + button_length, y), (x + button_length, y + button_length),
                                          (x, y + button_length)], 2)

        write_text(calculate_letter(c), x + button_length * 0.35, y + button_length * 0.28, text_size, (0,0,0))

        c += 1

    x = length * 11 / 16

    for i in range(3):
        y = Y + button_length * i
        p.draw.rect(win, (200,200,200), (x, y, button_length, button_length))
        p.draw.lines(win, (0,0,0), True, [(x, y), (x + button_length, y), (x + button_length, y + button_length),
                                          (x, y + button_length)], 2)

        write_text(calculate_letter(c), x + button_length * 0.35, y + button_length * 0.28, text_size, (0,0,0))

        c += 1

    y = height * 3 / 20

    p.draw.rect(win, (0, 220, 100), (x, y, button_length, button_length))
    p.draw.lines(win, (0,0,0), True, [(x, y), (x + button_length, y), (x + button_length, y + button_length),
                                      (x, y + button_length)], 2)

    write_text("beginner", x + (button_length * 0.07), y + (button_length * 0.18), int(text_size * 0.55), (0,0,0))
    write_text("method", x + (button_length * 0.13), y + (button_length * 0.49), int(text_size * 0.55), (0,0,0))

    x = length * 0.18
    y = height * 0.93

    write_text("Leftclick = clockwise, Right click = counter clockwise", x, y, int(text_size * 0.5), (0,0,0))

    x = length * 3 / 16
    y = height * 3 / 20

    p.draw.rect(win, (0, 220, 100), (x, y, button_length, button_length))
    p.draw.lines(win, (0,0,0), True, [(x, y), (x + button_length, y), (x + button_length, y + button_length),
                                      (x, y + button_length)], 2)

    write_text("reverse", x + (button_length * 0.13), y + (button_length * 0.18), int(text_size * 0.55), (0,0,0))
    write_text("scramble", x + (button_length * 0.05), y + (button_length * 0.5), int(text_size * 0.55), (0,0,0))



def draw_sticker(x, y, color, sticker_length):
    line_size = int(sticker_length * 0.08)
    if line_size < 1:
        line_size = 1

    p.draw.rect(win, color, (x, y, sticker_length, sticker_length))

    p.draw.lines(win, (0,0,0), True, [(x, y), (x + sticker_length, y), (x + sticker_length, y + sticker_length),
                                      (x, y + sticker_length)], line_size)



def draw_side(x, y, side):
    x = x - length / 8
    y = y - height / 10

    sticker_length = (length / 4) / 3

    c = 0

    for Y in range(3):
        for X in range(3):
            color = calculate_color(side[c])

            sticker_x = x + sticker_length * X
            sticker_y = y + sticker_length * Y
            draw_sticker(sticker_x, sticker_y, color, sticker_length)

            c += 1


def draw_cube(cube_list, move = ""):
    win.fill((255,255,255))

    c = 0
    for side in cube_list:
        if c == 0 or c == 1 or c == 3 or c == 5:
            x = length * 0.5
        elif c == 2:
            x = length * 0.75
        elif c == 4:
            x = length * 0.25

        if c == 3:
            y = height * 0.2
        elif c == 0 or c == 2 or c == 4:
            y = height * 0.4
        elif c == 1:
            y = height * 0.6
        elif c == 5:
            y = height * 0.8

        draw_side(x, y, side)

        c += 1

    draw_buttons()
    write_text(move, length * 0.48, height * 0.02, int(length / 16), (0,0,0))

    p.display.update()


#----------------------------main:---------------------------------------------------

def main():

    cube_list = [[] for i in range(6)]
    c = 0
    for side in cube_list:
        for i in range(9):
            side.append(c)
        c += 1

    draw_cube(cube_list)

    scramble = []

    while True:

        event = check_event()
        move = calculate_move(event)
        cube_list = make_move(cube_list, move)
        draw_cube(cube_list)

        solved = check_if_solved(cube_list)
        scramble = calculate_scramble(scramble, move, solved)
        cube_list = solve_cube(cube_list, scramble, move)

        clock.tick(30)

    
main()
