from app.movement import Movement


def tetris():
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

    rotation = 0

    screen, rotation = move_piece(screen, Movement.ROTATE, rotation)
    screen, rotation = move_piece(screen, Movement.ROTATE, rotation)
    screen, rotation = move_piece(screen, Movement.ROTATE, rotation)
    screen, rotation = move_piece(screen, Movement.ROTATE, rotation)


def print_screen(screen: list):
    print("\nTetris\n")
    for row in screen:
        print("".join(map(str, row)))


def move_piece(screen: list, movement: Movement, rotation: int) -> (list, int):

    new_screen = [["🔲"] * 10 for _ in range(10)]

    rotation_item = 0
    rotations = [
        [(1, 1), (0, 0), (-2, 0), (-1, -1)],
        [(0, 1), (-1, 0), (0, -1), (1, -2)],
        [(0, 2), (1, 1), (-1, 1), (-2, 0)],
        [(0, 1), (1, 0), (2, -1), (1, -2)]
    ]

    new_rotation = rotation
    if movement is Movement.ROTATE:
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
                        new_row_index = row_index + rotations[new_rotation][rotation_item][0]
                        new_column_index = column_index + rotations[new_rotation][rotation_item][1]
                        rotation_item += 1

                if new_row_index <= 9 and new_column_index >= 0 and new_column_index <= 9:
                    new_screen[new_row_index][new_column_index] = "🔳"
                else:
                    return (screen, rotation)

    print_screen(new_screen)
    return (new_screen, new_rotation)
