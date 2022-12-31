import random                                                                 # Import random module for random choices

wins = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]] # The possible win sequences
corners = [1, 3, 7, 9]                                                        # The corner positions


def take_chance(level, urgency):                                              # Function for making mistakes
    x = random.random() * 100                                                 # Random number from 0 to 100
    if urgency == 1:                                                          # If computer can win immediately,
        return False                                                          # Don't make mistake
    else:                                                                     # If computer cannot win immediately,
        if x > level:                                                         # If random number is more than level,
            return True                                                       # Make mistake
        else:                                                                 # If random number is less than level,
            return False                                                      # Don't make mistake


def XO():                                                                     # Function to make choice of player
    while True:                                                               # Until break statement,
        choice = input("Would you like to play as X or O or EITHER? ").upper() # Ask for input: X, O or EITHER
        if choice == "X" or choice == "O":                                    # If X or O inputted,
            break                                                             # Break
        if choice == "EITHER":                                                # If EITHER inputted,
            rand = random.randint(1, 2)                                       # Make random choice: 1 or 2
            if rand == 1:                                                     # If random choice is 1,
                choice = "X"                                                  # Player is X
            else:                                                             # If random choice is 0,
                choice = "O"                                                  # Player is O
            print("You are playing as", choice + '.')                         # Output the random choice for player
            break                                                             # Break
        print("Please choose X or O or EITHER only.")                         # Error message if neither X, O or EITHER
    print()                                                                   # Leave blank line
    if choice == 'X':
        comp_choice = 'O'
    else:
        comp_choice = 'X'
    return choice, comp_choice                                                             # Return the player's choice


def prioritise(Empty, priority, ans):                                         # Function for priorities of each position
    for i in Empty:                                                           # Among the empty positions,
        try:                                                                  # Try to:
            k = ans[i]                                                        # Get value of position key in ans
            ans[i] = k + priority                                             # Add priority to the value
        except:                                                               # If position key is not in ans,
            ans[i] = priority                                                 # Add the priority as its value
    return ans                                                                # Return modified ans dictionary


def potential_win(given_board, turn):                                         # Function to plan for wins
    board = given_board.copy()                                                # Copy board to avoid modifications
    ans = {}                                                                  # Dictionary of position : priority pairs
    for win in wins:                                                          # For each possible win sequence,
        X = []                                                                # List of X marked positions
        O = []                                                                # List of O marked positions
        Empty = []                                                            # List of empty positions
        for key in win:                                                       # For each key in win sequence,
            x = board[key]                                                    # Value of board position
            if x == "X":                                                      # If it is X,
                X.append(key)                                                 # Add to X list
            elif x == "O":                                                    # If it is O,
                O.append(key)                                                 # Add to O list
            else:                                                             # If it is empty (neither X nor O),
                Empty.append(key)                                             # Add to Empty list
        if len(Empty) == 0:                                                   # If no empty spaces in this win sequence,
            continue                                                          # Go to next win sequence
        if turn == "X":                                                       # If it is X's turn,
            if len(X) == 2:                                                   # If two out of three are X,
                ans = prioritise(Empty, 10000000, ans)                        # Maximum priority for the third space
            elif len(O) == 2:                                                 # If two out of three are O,
                ans = prioritise(Empty, 100000, ans)                          # High priority for the third space
            elif len(X) == 1:                                                 # If one out of three is X,
                ans = prioritise(Empty, 100, ans)                             # Low priority for the other two
            elif len(O) == 1:                                                 # If one out of three is O,
                ans = prioritise(Empty, 1, ans)                               # Very low priority for the other two
        elif turn == "O":                                                     # If it is O's turn,
            if len(O) == 2:                                                   # If two out of three are O,
                ans = prioritise(Empty, 10000000, ans)                        # Maximum priority for the third space
            elif len(X) == 2:                                                 # If two out of three are X,
                ans = prioritise(Empty, 100000, ans)                          # High priority for the third space
            elif len(O) == 1:                                                 # If one out of three is O,
                ans = prioritise(Empty, 100, ans)                             # Low priority for the other two
            elif len(X) == 1:                                                 # If one out of three is X,
                ans = prioritise(Empty, 1, ans)                               # Very low priority for the other two
    position_s = list(ans.keys())                                             # List of positions in ans dictionary
    priorities = list(ans.values())                                           # List of priorities in ans dictionary
    PRIORITIES = sorted(priorities, reverse = True)                           # List of priorities in reverse order
    final_priorities = []                                                     # List of final priorities (ordered)
    final_positions = []                                                      # List of final positions (ordered)
    for i in PRIORITIES:                                                      # For each priority,
        temporary_list = []                                                   # List of positions having that priority
        while i in priorities:                                                # While that priority is in priorities,
            ind = priorities.index(i)                                         # Find index of it
            priorities.pop(ind)                                               # Remove it
            temporary_list.append(position_s[ind])                            # Add its position to temporary_list
            position_s.pop(ind)                                               # Remove it from position_s also
        final_priorities.append(i)                                            # Add the priority to final_priorities
        final_positions.append(temporary_list)                                # Add the position to final_positions
    if len(final_priorities) != 0:                                            # If final_priorities is non-empty,
        if final_priorities[0] >= 100000:                                     # If maximum priority is more than 100000,
            urgency = 1                                                       # Mark as urgent (immediate win)
        else:                                                                 # Otherwise,
            urgency = 0                                                       # Mark as not urgent (not immediate win)
    else:                                                                     # If final_priorities is empty,
        urgency = 0                                                           # Mark as not urgent
    return final_positions, urgency                                           # Return tuple of final_positions and urgency


def computer_move(board, available, turn, level):                             # Function for generating computer's turn
    empty = 0                                                                 # Number of empty positions available
    for i in board:                                                           # For each position,
        if board[i] == ' ':                                                   # If it is empty,
            empty += 1                                                        # Increment empty by 1
    if empty == 9 and not take_chance(level, 0):                              # If all are empty and no mistake,
        ans = 5                                                               # Take middle position
    elif empty == 8 and board[5] == ' ' and not take_chance(level, 0):        # If one is occupied (not middle one) and no mistake,
        ans = 5                                                               # Take middle position
    else:                                                                     # Otherwise,
        good_list, urgency = potential_win(board, turn)                       # Get the best moves available and urgency
        index = 0                                                             # Index of list of moves in good_list
        k = []                                                                # Best possible moves in good_list
        force_continue = False                                                # Forcibly continue
        while len(k) == 0 or force_continue:                                  # While k is empty, and not forced to continue,
            try:                                                              # Try to:
                k = good_list[index]                                          # Find moves for index in k
                index += 1                                                    # Increment index by 1
                condition = board[1] == board[9] == "X" or board[3] == board[7] == "X" # Condition for avoiding flanking
                condition = condition and board[5] == "O"                     # Also middle position must be O
                if empty == 6 and condition:                                  # If 6 positions are empty and condition is satisfied,
                    not_corner_list = []                                      # List of available not corner elements
                    for i in k:                                               # For each good position available,
                        if i not in corners:                                  # If it is not in the corners,
                            not_corner_list.append(i)                         # Add it to not_corner_list
                    if len(not_corner_list) == 0:                             # If there are no good not corner positions,
                        force_continue = True                                 # Forcibly continue next iteration
                    else:                                                     # If there are good not corner positions,
                        break                                                 # Break out of while loop
            except:                                                           # If index exceeded limit,
                break                                                         # Break out of while loop
        if k != []:                                                           # If k is non-empty,
            if not take_chance(level, urgency):                               # If no mistake to be made,
                corner_list = []                                              # List of good corner positions
                for i in k:                                                   # For each position in k,
                    if i in corners:                                          # If it is in corners,
                        corner_list.append(i)                                 # Add it to corner_list
                condition = False                                             # Condition for flanking
                for i in [2, 4, 6, 8]:                                        # For each side position,
                    condition = condition or board[i] == "O"                  # If it is O, change condition to True
                condition = board[5] == "X" and condition                     # Middle position must be X
                if condition and empty == 7:                                  # If condition is satisfied and 7 positions are empty,
                    if board[2] == "O":                                       # If 2 is O,
                        corner_list = [1, 3]                                  # Choose adjacent ones (1, 3)
                    elif board[4] == "O":                                     # If 4 is O,
                        corner_list = [1, 7]                                  # Choose adjacent ones (1, 7)
                    elif board[6] == "O":                                     # If 6 is O,
                        corner_list = [3, 9]                                  # Choose adjacent ones (3, 9)
                    elif board[8] == "O":                                     # If 8 is O,
                        corner_list = [7, 9]                                  # Choose adjacent ones (7, 9)
                if condition and empty == 5:                                  # If condition is satisfied and 5 positions are empty,
                    if board[1] == "X":                                       # If 1 is X,
                        if board[2] == "O":                                   # If 2 is O,
                            corner_list = [7]                                 # Choose 7
                        elif board[4] == "O":                                 # If 4 is O,
                            corner_list = [3]                                 # Choose 3
                    elif board[3] == "X":                                     # If 3 is X,
                        if board[2] == "O":                                   # If 2 is O,
                            corner_list = [9]                                 # Choose 9
                        elif board[6] == "O":                                 # If 5 is O,
                            corner_list = [1]                                 # Choose 1
                    elif board[7] == "X":                                     # If 7 is X,
                        if board[4] == "O":                                   # If 4 is O,
                            corner_list = [9]                                 # Choose 9
                        elif board[8] == "O":                                 # If 8 is O,
                            corner_list = [1]                                 # Choose 1
                    elif board[9] == "X":                                     # If 9 is X,
                        if board[6] == "O":                                   # If 6 is O,
                            corner_list = [7]                                 # Choose 7
                        elif board[8] == "O":                                 # If 8 is O,
                            corner_list = [3]                                 # Choose 3
                if len(corner_list) != 0:                                     # If corner_list is non-empty,
                    ans = random.choice(corner_list)                          # Choose a random position from it
                else:                                                         # If corner_list is empty,
                    ans = random.choice(k)                                    # Just choose a random position from k
            else:                                                             # If mistake is made,
                ans = random.choice(available)                                # Just choose a random available position
        else:                                                                 # If k is empty,
            ans = random.choice(available)                                    # Just choose a random available position
    return ans                                                                # Return the answer


def print_board(board):                                                       # Function to output the board
    line = '--- --- ---'                                                      # Used to separate rows
    l1 = ' ' + board[1] + ' | ' + board[2] + ' | ' + board[3]                 # Row 1
    l2 = ' ' + board[4] + ' | ' + board[5] + ' | ' + board[6]                 # Row 2
    l3 = ' ' + board[7] + ' | ' + board[8] + ' | ' + board[9]                 # Row 3
    print(l1, line, l2, line, l3, sep = '\n')                                 # All three rows together in board form
    print()                                                                   # Leave a line
    return None                                                               # (No purpose)


def positions(board):                                                         # Function to output board positioning
    locations = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'} # All positions, numbered
    print("The positions are as follows:")                                    # Output
    print_board(locations)                                                    # All positions numbered in board
    print_board(board)                                                        # The board itself
    return None                                                               # (No purpose)


def win_check(board):                                                         # Function to check if someone won
    result = None                                                             # Default result (No win)
    for win in wins:                                                          # For each possible win sequence,
        if board[win[0]] == board[win[1]] == board[win[2]] == "X":            # If all three are X,
            result = "X"                                                      # X wins
            break                                                             # Break out of for loop
        elif board[win[0]] == board[win[1]] == board[win[2]] == "O":          # If all three are O,
            result = "O"                                                      # O wins
            break                                                             # Break out of for loop
    for i in range(1, 10):                                                    # For each position,
        if board[i] == ' ':                                                   # If it is empty,
            break                                                             # Break out of for loop (don't execute else clause)
    else:                                                                     # If no position is empty,
        if result != "X" and result != "O":                                   # If neither X nor O wins,
            result = 'Draw'                                                   # Draw
    return result                                                             # Return the result


def place_piece(board, available, turn, ask, level):                          # Function to place a piece on the board
    if ask:                                                                   # If it is user's turn,
        while True:                                                           # Until break statement,
            k = input("Choose position to place " + turn + " (Enter HELP for positions): ") # Ask for input
            if k.upper() == "HELP":                                           # If user requests help,
                positions(board)                                              # Show positions
                continue                                                      # Go to next iteration
            try:                                                              # Try to:
                key = int(k)                                                  # Convert input to integer type
                if key not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:                    # If key is not among positions,
                    print(k, "is not a valid position.")                      # It is not a valid position
                elif key not in available:                                    # If that position is occupied,
                    print("Position", k, "is not available.")                 # It is not available
                else:                                                         # If it is not occupied,
                    break                                                     # Break out of while loop
            except:                                                           # If error while converting k to int,
                print(k, "is not a valid position.")                          # It is not a valid position
    else:                                                                     # If it is not user's turn,
        key = computer_move(board, available, turn, level)                    # Generate computer move
        print("Computer choice: Position", key)                               # Output the computer's choice
    board[key] = turn                                                         # Place the X or O on the board
    available.remove(key)                                                     # Remove the position from available
    print_board(board)                                                        # Output the board
    return board, available                                                   # Return the board and available positions


def play():                                                                   # Function to play one game
    board = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}   # Empty board
    user_letter, comp_letter = XO()                                           # Choose X or O for user
    while True:                                                               # Until break statement,
        try:                                                                  # Try to:
            level = float(input("Enter difficulty level from 0 to 100: "))    # Ask for difficulty and convert to float
            if 0 <= level <= 100:                                             # If level is valid,
                break                                                         # Break out of while loop
        except:                                                               # If conversion not possible,
            pass                                                              # Ignore it
        print("Please enter difficulty level from 0 to 100 only.")            # Request to enter valid level
    positions(board)                                                          # Output the positions
    turn = "X"                                                                # X goes first
    available = [1, 2, 3, 4, 5, 6, 7, 8, 9]                                   # Available positions (now all)
    result = win_check(board)                                                 # Check for wins
    while result == None:                                                     # While no win or draw,
        if turn == user_letter:                                               # If it is user's chance,
            ask = True                                                        # Ask for move
        else:                                                                 # If it is computer's chance,
            ask = False                                                       # Don't ask for move
        board, available = place_piece(board, available, turn, ask, level)    # Place a piece on the board
        if turn == "X":                                                       # If this was X's turn,
            turn = "O"                                                        # Next is O's turn
        else:                                                                 # If this was O's turn,
            turn = "X"                                                        # Next is X's turn
        result = win_check(board)                                             # Check for wins
    if result == user_letter:                                                 # If result is user's letter,
        print("You win!")                                                     # User wins
    elif result == comp_letter:                                               # If result is computer's letter,
        print("You lose!")                                                    # User loses
    else:                                                                     # If result is neither,
        print("Draw!")                                                        # It is a draw
    print()                                                                   # Leave blank line


print(("TIC TAC TOE\n"))                                                      # Heading
play()                                                                        # Play a game
