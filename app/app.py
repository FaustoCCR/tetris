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

    screen = move_piece(screen, Movement.DOWN)
    screen = move_piece(screen, Movement.DOWN)
    screen = move_piece(screen, Movement.DOWN)
    screen = move_piece(screen, Movement.RIGHT)
    screen = move_piece(screen, Movement.RIGHT)
    screen = move_piece(screen, Movement.DOWN)
    screen = move_piece(screen, Movement.LEFT)
    screen = move_piece(screen, Movement.LEFT)
    screen = move_piece(screen, Movement.LEFT)
    


def print_screen(screen: list):
    print("\nTetris\n")
    for row in screen:
        print("".join(map(str, row)))


def move_piece(screen: list, movement: Movement) -> list:

    new_screen = [["🔲"] * 10 for _ in range(10)]

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
                        pass
                if new_row_index <= 9 and new_column_index >= 0 and new_column_index <= 9:
                    new_screen[new_row_index][new_column_index] = "🔳"
                else:
                    return screen

    print_screen(new_screen)
    return new_screen
