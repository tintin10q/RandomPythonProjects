

def print_board(board_input):
    print(f'''
    -------------
    | {board_input[0]} | {board_input[1]} | {board_input[2]} |
    -------------
    | {board_input[3]} | {board_input[4]} | {board_input[5]} |
    -------------
    | {board_input[6]} | {board_input[7]} | {board_input[8]} |
    -------------''')


q = 'y'
while q == 'y':
    board_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    turn = "X"
    winner = None
    print_board(board_data)
    while winner is None:
         # display the board
        user_input = input('Where do you want to put:')
        if not user_input.isnumeric():
            print('Please put in a number!')
            continue
        user_input = int(user_input)
        if user_input not in board_data:
            print(f"Cell {user_input} is already taken")
            continue
        user_input -= 1
        board_data[user_input] = turn
        print_board(board_data)
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

        # Winner detection
        if board_data[0] == board_data[1] == board_data[2]:
            winner = board_data[0]
        elif board_data[3] == board_data[4] == board_data[5]:
            winner = board_data[3]
        elif board_data[6] == board_data[7] == board_data[8]:
            winner = board_data[6]
        elif board_data[0] == board_data[3] == board_data[6]:
            winner = board_data[0]
        elif board_data[1] == board_data[4] == board_data[5]:
            winner = board_data[1]
        elif board_data[2] == board_data[5] == board_data[8]:
            winner = board_data[2]
        elif board_data[0] == board_data[4] == board_data[8]:
            winner = board_data[0]
        elif board_data[2] == board_data[4] == board_data[6]:
            winner = board_data[2]
    print(f'{winner} has won!')
    q = input('Do you want to play again (y/n):').lower()
print('End of program')
