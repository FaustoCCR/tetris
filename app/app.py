from app.movement import Movement
import keyboard


def tetris():
    # initial dashboard
    screen = [
        ["🔳", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
        ["🔳", "🔳", "🔳", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
        ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
        ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
        ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
        ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
        ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
        ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
        ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
        ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"]
    ]
    print_screen(screen)

    # the rotation will be initialized with 0 value
    rotation = 0

    while (True):
        event = keyboard.read_event()
        if event.name == "esc":
            break
        elif event.event_type == keyboard.KEY_DOWN:  # an other key has been pressed
            if event.name == "down":
                movement = Movement.DOWN
            elif event.name == "right":
                movement = Movement.RIGHT
            elif event.name == "left":
                movement = Movement.LEFT
            elif event.name == "space":
                movement = Movement.ROTATE
            else:
                continue
            (screen, rotation) = move_piece(screen, movement, rotation)


def print_screen(screen: list):
    print("\nTetris\n")
    for row in screen:
        # use join to concatenate a list of strings
        print("".join(map(str, row)))


def move_piece(screen: list, movement: Movement, rotation: int) -> (list, int):

    new_screen = [["🔲"] * 10 for _ in range(10)]  # create a 10 x 10 matrix

    rotation_item = 0
    # how many a piece have to move in each rotation
    rotations = [
        [(1, 1), (0, 0), (-2, 0), (-1, -1)],
        [(0, 1), (-1, 0), (0, -1), (1, -2)],
        [(0, 2), (1, 1), (-1, 1), (-2, 0)],
        [(0, 1), (1, 0), (2, -1), (1, -2)]
    ]

    new_rotation = rotation
    if movement is Movement.ROTATE:
        # increment or reset the rotation for each iteration
        new_rotation = 0 if rotation == 3 else rotation + 1

    for row_index, row in enumerate(screen):
        for column_index, item in enumerate(row):

            if item == "🔳":

                new_row_index = 0
                new_column_index = 0

                match movement:
                    case Movement.DOWN:
                        new_row_index = row_index + 1
                        new_column_index = column_index
                    case Movement.RIGHT:
                        new_row_index = row_index
                        new_column_index = column_index + 1
                    case Movement.LEFT:
                        new_row_index = row_index
                        new_column_index = column_index - 1
                    case Movement.ROTATE:
                        new_row_index = row_index + \
                            rotations[new_rotation][rotation_item][0]
                        new_column_index = column_index + \
                            rotations[new_rotation][rotation_item][1]
                        rotation_item += 1

                if new_row_index <= 9 and new_column_index >= 0 and new_column_index <= 9:
                    new_screen[new_row_index][new_column_index] = "🔳"
                else:
                    print("📢Movement not allowed")
                    return (screen, rotation)

    print_screen(new_screen)
    return (new_screen, new_rotation)
