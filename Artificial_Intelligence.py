# AI TO LEARN TO PLAY TIC-TAC-TOE

from random import choice, shuffle                          # Import some random module functions for random decisions

wins = ((1, 2, 3), (4, 5, 6), (7, 8, 9),
        (1, 4, 7), (2, 5, 8), (3, 6, 9),
        (1, 5, 9), (3, 5, 7))                               # The possible win sequences
corners = (1, 3, 7, 9)                                      # The corner positions
corners_and_centre = (1, 3, 5, 7, 9)                        # The corner and centre positions
sides = (2, 4, 6, 8)                                        # The side positions
flanks = ((1, 3), (1, 5), (1, 7), (1, 9),
          (3, 5), (3, 7), (3, 9), (5, 7),
          (5, 9), (7, 9))                                   # The sequences used in flank() function
anti_flanks = ((1, 9), (3, 7))                              # The sequences used in anti_flank() function
locations = {1: '1', 2: '2', 3: '3',
             4: '4', 5: '5', 6: '6',
             7: '7', 8: '8', 9: '9'}                        # All positions, numbered

type_str = type('')                                         # Variable to store <class 'str'>
type_tuple = type(())                                       # Variable to store <class 'tuple'>
type_list = type([])                                        # Variable to store <class 'list'>

original = " `1234567890-=~!@#$%^&*()_+qwertyuiop[]\\QWERTYUIOP{}|asdfghjkl;\'ASDFGHJKL:\"zxcvbnm,./ZXCVBNM<>?\n"
                                                            # Sequence of the original characters
encrypted = " ~!QAZXSW@#EDCVFR$%TGBNHY^&UJM<KI*(OL>?:P)_{\"}+|\\=]\'[-0p;/.lo98ik,mju76yhnbgt54rfvcde32wsxzaq1`\n"
                                                            # Sequence of the encrypted characters


def fxn():                                                  # No purpose, just need <class 'function'>
    return None                                             # No purpose again


type_fxn = type(fxn)                                        # Variable to store <class 'function'>


def Xs_and_Os(win, board):                                  # Function to check each position for X/O/Empty
    X, O, Empty = [], [], []                                # Variables to store X, O, Empty positions
    for key in win:                                         # For each position,
        val = board[key]                                    # Get the value
        if val == "X":                                      # If value is X,
            X.append(key)                                   # Add to the list X
        elif val == "O":                                    # If value is O,
            O.append(key)                                   # Add to the list O
        else:                                               # If value is neither X nor O,
            Empty.append(key)                               # Add to the list Empty
    return X, O, Empty                                      # Return all three lists


def sort_dict(d, negative=False, seq=True):                 # Function to sort a dictionary
                                                            # Note: Dictionaries are ordered in Python 3.7 onwards
    lst = sorted(d.values(), reverse=True)                  # Sorted list of values in descending order
    k = list(d.keys())                                      # List of all keys
    v = list(d.values())                                    # List of all values
    l = len(lst)                                            # Length of lst, i.e., length of d
    fresh_d = {}                                            # New dictionary (sorted) to be returned later
    for i in range(l):                                      # For each index of lst,
        value = lst.pop()                                   # Remove last element of lst and store in value
        ind = v.index(value)                                # Find corresponding index of element in v
        key = k[ind]                                        # Get corresponding key from k
        v.pop(ind)                                          # Remove that index from v
        k.pop(ind)                                          # and from k
        fresh_d[key] = value                                # Add that key:value pair to fresh_d
    if negative:                                            # If negative=True is specified,
        delete = []                                         # List of elements to be deleted
        for i in fresh_d:                                   # For each key in fresh_d,
            if fresh_d[i][0] < 0:                           # If the first element of the value is negative,
                delete.append(i)                            # It is to be deleted
        for j in delete:                                    # For each key:value pair to be deleted,
            del fresh_d[j]                                  # Delete that pair
    return fresh_d                                          # Return the final, sorted dictionary


def pick_some(seq):                                         # Function to make a random selection from a sequence
    s = list(seq)                                           # Convert seq to a list s
    shuffle(s)                                              # Shuffle s (randomise the order of elements)
    l = len(s)                                              # Length of s, i.e. length of seq
    r = list(range(l + 1))                                  # The list [1, 2, ... l - 1]
    stop = choice(r) + 1                                    # Stop-value (for slicing) is any element of r
    s = s[0 : stop]                                         # The slice from 0 to stop-value
    return s                                                # Return the slice (random selection)


def final_choice(functional_properties, all_methods):       # Function to make a final choice from generated methods
    fxnd_fxns = list(functioned_functions)                  # List of functioned_functions
    length = len(all_methods)                               # Number of methods tried
    shuffle(fxnd_fxns)                                      # Shuffle fxnd_fxns
    properties, values = [], []                             # Lists of properties and values
    skip = False                                            # Condition to skip the analysis
    for f in functional_properties:                         # For each function,
        s = functional_properties[f]                        # Get its score (property)
        properties.append([s, f])                           # Add the [score, function] pair to properties
        values.append(s)                                    # Add the score to values
    if length <= 10:                                        # If number of methods tried is <= 10,
        skip = True                                         # Change skip condition to True (i.e. skip analysis)
    else:                                                   # If skip is still False,
        for i in functioned_functions:                      # For each function,
            condition = False                               # Condition for a particular function
            for j in all_methods:                           # For each key (each used method),
                if i in j:                                  # If the particular function was used in the method,
                    condition = True                        # Change condition to True
            if condition is False:                          # If condition is still False (if any function is unused),
                skip = True                                 # Change skip condition to True (i.e. skip analysis)
                break                                       # Sufficient for skip to be True even once; break out
    if not skip:                                            # If skip condition is False (i.e. don't skip),
        values = list(set(values))                          # List of all values; set() is used to remove repetition
        values.sort(reverse=True)                           # Sort values in descending order
        prop = []                                           # Temporary variable to take some elements of properties
        for value in values:                                # For each score/value,
            lst = []                                        # List of all [score, function] pairs with this score
            for i in properties:                            # For each [score, function] pair,
                if i[0] == value:                           # If 1st element (score) is equal to value,
                    lst.append(i[1])                        # Add 2nd element (function) to lst
            prop.append(lst)                                # Add the entire lst to prop
        properties = prop.copy()                            # The list properties is now changed
        count = 0                                           # Count of attempts to create a new method
        final = []                                          # Final method chosen
        condition = True                                    # Condition to use a shortcut
        for i in properties:                                # For each list of functions in properties,
            if len(i) != 1:                                 # If there is more than one function,
                condition = False                           # Change condition to False
                break                                       # Sufficient for even one to be False; break out of loop
        if condition:                                       # If condition is True (i.e. all lists have 1 element)
            for i in properties:                            # For each list,
                final.extend(i)                             # Add its single element to final
            for i in range(len(properties)):                # For each index,
                if tuple(final) not in all_methods:         # If the chosen sequence is not used yet,
                    final = tuple(final)                    # Convert final to tuple
                    break                                   # Break out of for loop
                elif i <= 2:                                # This can happen at most 3 times (0, 1, 2)
                    final.pop()                             # Remove last function from chosen sequence
            else:                                           # If none of the attempted sequences were unused,
                final = None                                # Give up; choose a random one later
        else:                                               # If condition is False (i.e. some lists have multiple ele)
            while count <= 10:                              # This can happen at most 11 times (0, 1, 2, ..., 10)
                for i in properties:                        # For each list,
                    shuffle(i)                              # Shuffle it
                    final.extend(i)                         # Add all its elements to final
                final = tuple(final)                        # Convert final to tuple
                if final not in all_methods:                # If the chosen sequence is not used yet,
                    break                                   # Break out of while loop
                else:                                       # If the chosen sequence has been used,
                    final = []                              # Start over; make final an empty list
                count += 1                                  # Increment count by 1
            else:                                           # If none of the attempted sequences were unused,
                final = None                                # Give up; choose a random one later
    else:                                                   # If skip condition is True (i.e. skip analysis),
        final = None                                        # Just choose a random method later
    return final                                            # Return the tuple/NoneType final


def analyse(all_methods, fxn_scores=False):                 # Function to analyse all past methods and generate new one
    if all_methods:                                         # If this is not the first time (we have played before),
        good_methods = sort_dict(all_methods, negative=True)  # Arrange methods in descending order, excluding negatives
        if fxn_scores or not good_methods:                  # If fxn_scores=True specified or there are no good methods,
            bad_methods = sort_dict(all_methods)            # Arrange methods in descending order
            special_data = {}                               # Dictionary of method: score pairs
            for method in bad_methods:                      # For each used method,
                special_data[method] = bad_methods[method][2]  # Take the score value (3rd element) and add it to dict
            special_data = sort_dict(special_data)          # Arrange special_data in descending order
            used_methods = tuple(special_data.keys())       # All previously used methods
            functional_properties = {}                      # Dictionary of function: score pairs
            for i in functioned_functions:                  # For each function available,
                functional_properties[i] = 0                # Set initial score to zero
            for steps in used_methods:                      # For each previously used method,
                value = special_data[steps]                 # Get the corresponding score
                l = len(steps)                              # Number of functions in that method
                for i in range(l):                          # For each index of function in steps
                    step = steps[i]                         # The function corresponding to that index
                    L = len(functioned_functions)           # Total number of functions
                    addition = (2 ** (L - (i + 1))) * value  # Value to be added, priority-wise
                    functional_properties[step] += addition  # Add that value to that function's score
            final_process = final_choice(functional_properties, all_methods)  # Generate the final method to be used
        if fxn_scores:                                      # If dev tools were used to get function scores,
            for i in functional_properties:                 # For each function,
                print(i, functional_properties[i])          # Print function: score
        if not good_methods:                                # If there are no good methods
            if final_process is None:                       # If the final process wasn't generated at all,
                final_process = pick_some(functioned_functions)  # Pick a random method from the available functions
        else:                                               # If there are some good methods,
            options = list(good_methods.keys())             # Make a list of the good methods
            final_process = choice(options)                 # Choose any of them
    else:                                                   # If this is the first time (no previous methods),
        final_process = pick_some(functioned_functions)     # Pick a random method from the available functions
    return list(final_process)                              # Return a list of the chosen method


def filter(options, pick_me):                               # Function to filter options based on preferences
    maxx = 0                                                # Occurrence of most frequent position in pick_me
    for i in pick_me:                                       # For each prioritised position,
        c = pick_me.count(i)                                # Count its occurrence
        if c > maxx:                                        # If it's greater than maxx,
            maxx = c                                        # Set the maximum to it
    filtrate = []                                           # List of most frequent positions
    no_rep = list(set(pick_me))                             # To remove duplicates in pick_me
    for i in no_rep:                                        # For each prioritised position,
        if pick_me.count(i) == maxx:                        # If it occurred most frequently,
            filtrate.append(i)                              # Add it to filtrate
    filtered_options = []                                   # List of the filtered options
    for option in filtrate:                                 # For each preferred choice,
        if option in options:                               # If it is an available option,
            filtered_options.append(option)                 # Add it to filtered_options
    filtered_options = list(set(filtered_options))          # To remove duplicates
    if len(filtered_options) == 0:                          # If there are no options fitting the condition,
        return options                                      # Return the original options
    else:                                                   # If there are satisfactory options
        return filtered_options                             # Return the filtered options


def win_lose_etc(board, options, turn, tup):                # Function used by the next 4 functions
    a, b, val = tup                                         # Unpacking the tuple argument (tup gives us the condition)
    filtered_options = []                                   # Options which satisfy the condition
    for win in wins:                                        # For each win sequence,
        X, O, Empty = Xs_and_Os(win, board)                 # Positions occupied by X, O, none resp.
        if len(Empty) == 0:                                 # If no positions are empty in this win sequence,
            continue                                        # Continue to next win sequence
        elif turn == a:                                     # If comp's turn is a (whatever a is),
            if len(X) == val:                               # And if there are val X's in the seq (whatever val is),
                filtered_options.extend(Empty)              # Add the empty positions to filtered_options
        elif turn == b:                                     # If comp's turn is b (whatever b is),
            if len(O) == val:                               # And if there are val O's in the seq (whatever val is),
                filtered_options.extend(Empty)              # Add the empty positions to filtered_options
    return filter(options, filtered_options)                # Filter the options and return them


def next_win(board, options, turn, previous_move):          # Function to check if comp can win in 1 move
    tup = ("X", "O", 2)                                     # Check for 2 positions occupied with comp's letter
    return win_lose_etc(board, options, turn, tup)          # Return the filtered options


def next_lose(board, options, turn, previous_move):         # Function to check if user can win in 1 move
    tup = ("O", "X", 2)                                     # Check for 2 positions occupied with user's letter
    return win_lose_etc(board, options, turn, tup)          # Return the filtered options


def possible_win(board, options, turn, previous_move):      # Function to check if comp can win in 2 moves
    tup = ("X", "O", 1)                                     # Check for 1 position occupied with comp's letter
    return win_lose_etc(board, options, turn, tup)          # Return the filtered options


def possible_lose(board, options, turn, previous_move):     # Function to check if user can win in 2 moves
    tup = ("O", "X", 1)                                     # Check for 1 position occupied with user's letter
    return win_lose_etc(board, options, turn, tup)          # Return the filtered options


def centre(board, options, turn, previous_move):            # Function to choose the centre position
    return filter(options, (5,))                            # Filter the options according to the condition


def flank_not_flank_etc(board, options, turn, flank_yes):
    filtered_options = []                                   # Options which satisfy the condition
    if turn == "X":                                         # If comp's turn is X,
        not_turn = "O"                                      # User's turn is O
    else:                                                   # If comps' turn is O,
        not_turn = "X"                                      # User's turn is X
    if flank_yes:                                           # If function is flank()
        for i in flanks:                                    # For each flank sequence,
            if board[i[0]] == board[i[1]] == turn:          # If both positions occupied by computer,
                filtered_options.extend(corners_and_centre)  # Add 1, 3, 5, 7, 9 to filtered_options
    else:                                                   # If function is anti_flank()
        for i in anti_flanks:                               # For each anti-flank sequence,
            if board[i[0]] == board[i[1]] == not_turn:      # If both positions occupied by user,
                filtered_options.extend(sides)              # Add 2, 4, 6, 8 to filtered_options
    return filter(options, filtered_options)                # Filter the options according to the condition


def flank(board, options, turn, previous_move):             # Function to flank the opponent
    return flank_not_flank_etc(board, options, turn, True)  # Return the filtered options


def anti_flank(board, options, turn, previous_move):        # Function to avoid being flanked by the opponent
    return flank_not_flank_etc(board, options, turn, False)  # Return the filtered options


def just_opposite(board, options, turn, previous_move):     # Function to return the position just opposite to previous move
    return filter(options, (10 - previous_move,))           # Return the filtered options


def XO():                                                   # Function to make choice of X or O
    while True:                                             # Until break statement,
        s = input("Would you like to play as X or O or EITHER? ").upper()  # Ask for input: X, O or EITHER
        if s == "X" or s == "O":                            # If X or O inputted,
            break                                           # Break
        if s == "EITHER":                                   # If EITHER inputted,
            s = choice(["X", "O"])                          # Choose X or O randomly
            print("You are playing as", s + '.')            # Output the random choice for player
            break                                           # Break
        print("Please choose X or O or EITHER only.")       # Error message if neither X, O or EITHER
    print()                                                 # Leave blank line
    if s == 'X':                                            # If player chooses X,
        comp_choice = 'O'                                   # Computer chooses O
    else:                                                   # If player chooses O,
        comp_choice = 'X'                                   # Computer chooses X
    return s, comp_choice                                   # Return the player's choice


def computer_move(board, available, turn, methods, previous_move):  # Function for generating computer's move
    options = available.copy()                              # To avoid making changes in original
    for method in methods:                                  # For each function in the chosen methods,
        options = method(board, options, turn, previous_move)  # Filter out some of them according to the function
        if len(options) == 1:                               # If there is exactly one option left,
            break                                           # Break out of for loop (done; that's the one to choose)
    key = choice(options)                                   # Choose a random one from the options left
    return key                                              # Return that random choice


def print_board(board):                                     # Function to output the board
    line = '--- --- ---'                                    # Used to separate rows
    l1 = ' ' + board[1] + ' | ' + board[2] + ' | ' + board[3]  # Row 1
    l2 = ' ' + board[4] + ' | ' + board[5] + ' | ' + board[6]  # Row 2
    l3 = ' ' + board[7] + ' | ' + board[8] + ' | ' + board[9]  # Row 3
    print(l1, line, l2, line, l3, sep='\n')                 # All three rows together in board form
    print()                                                 # Leave a line


def positions(board):                                       # Function to output board positioning
    print("The positions are as follows:")                  # Output
    print_board(locations)                                  # All positions numbered in board
    print_board(board)                                      # The board itself


def win_check(board):                                       # Function to check if someone won
    result = None                                           # Default result (No win)
    for win in wins:                                        # For each possible win sequence,
        if board[win[0]] == board[win[1]] == board[win[2]] == "X":  # If all three are X,
            result = "X"                                    # X wins
            break                                           # Break out of for loop
        elif board[win[0]] == board[win[1]] == board[win[2]] == "O":  # If all three are O,
            result = "O"                                    # O wins
            break                                           # Break out of for loop
    for i in range(1, 10):                                  # For each position,
        if board[i] == ' ':                                 # If any position is empty,
            break                                           # Break out of for loop (don't execute else clause)
    else:                                                   # If no position is empty,
        if result != "X" and result != "O":                 # If neither X nor O wins,
            result = 'Draw'                                 # Draw
    return result                                           # Return the result


def place_piece(board, available, turn, ask, methods, previous_move):  # Function to place a piece on the board
    if ask:                                                 # If it is user's turn,
        while True:                                         # Until break statement,
            k = input("Choose position to place " + turn + " (Enter HELP for positions): ")  # Ask for input
            if k.upper() == "HELP":                         # If user requests help,
                positions(board)                            # Show positions
                continue                                    # Go to next iteration
            try:                                            # Try to:
                key = int(k)                                # Convert input to integer type
                if key not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:  # If key is not among positions,
                    print(k, "is not a valid position.")    # It is not a valid position
                elif key not in available:                  # If that position is occupied,
                    print("Position", k, "is not available.")  # It is not available
                else:                                       # If it is not occupied,
                    break                                   # Break out of while loop
            except ValueError:                              # If error while converting k to int,
                print(k, "is not a valid position.")        # It is not a valid position
    else:                                                   # If it is not user's turn,
        key = computer_move(board, available, turn, methods, previous_move)  # Generate computer move
        print("Computer choice: Position", key)             # Output the computer's choice
    board[key] = turn                                       # Place the X or O on the board
    available.remove(key)                                   # Remove the position from available
    print_board(board)                                      # Output the board
    return board, available, key                            # Return the board and available positions


def play(dev, fxn_scores, forced_choice, show_think, proceed, letter_lock):  # Function to play one game
    board = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}  # Empty board
    if dev:                                                 # If this is the first game of the session,
        t = input("Enter anything to start: ")              # Trick question for inputting the password
        if t == "!unlock d3v t00lz":                        # If the correct password was entered,
            while True:                                     # Until break statement,
                s = input(">>> ")                           # Ask for input
                if s == "function scores":                  # If user inputs 'function scores',
                    fxn_scores = True                       # Output the function scores later
                elif s == "refresh":                        # If user inputs 'refresh',
                    f = open('Storage.txt', 'w')            # Open the file of data (i.e. wipe it)
                    f.close()                               # Close the file
                elif s == "try this":                       # If user inputs 'try this',
                    forced_choice = True                    # Force the program to choose the entered method only
                    lst = eval(input())                     # Enter the method to be used
                elif s == "show thinking":                  # If user inputs 'show thinking',
                    show_think = True                       # Output the chosen method later
                elif s == "always continue":                # If user inputs 'always continue',
                    proceed = True                          # Make the program proceed directly to the next game
                elif s == "this letter":                    # If user inputs 'this letter',
                    letter_lock = input()                   # Permanently set the user's letter to the input
                elif s == "back":                           # If user inputs 'back',
                    break                                   # Break out of while loop
    if letter_lock:                                         # If user had used 'this letter',
        user_letter = letter_lock                           # Set user's letter to the inputted one
        if user_letter == "X":                              # If it was X,
            comp_letter = "O"                               # Computer is O
        else:                                               # If it was O,
            comp_letter = "X"                               # Computer is X
    else:                                                   # If 'this letter' was not used,
        user_letter, comp_letter = XO()                     # Assign the letters X, O to user and computer
    all_methods = superdecrypt()                            # Get all previous history from file
    available = [1, 2, 3, 4, 5, 6, 7, 8, 9]                 # Available positions (now all)
    positions(board)                                        # Output the positions
    turn = "X"                                              # X goes first
    if forced_choice:                                       # If user had used 'try this',
        methods = lst                                       # Use only the method that user entered
    else:                                                   # If user had not used 'try this',
        methods = analyse(all_methods, fxn_scores=fxn_scores)  # Use normal way of analysing and finding a method
    if show_think:                                          # If user had used 'show thinking',
        print(methods)                                      # Output the methods used for this game
    result = win_check(board)                               # Check for wins (now it is None)
    moves = 0                                               # Number of moves for which the game was played
    move = 0                                                # Number of moves so far
    while result == None:                                   # While no win or draw,
        if turn == user_letter:                             # If it is user's chance,
            ask = True                                      # Ask for move
        else:                                               # If it is computer's chance,
            ask = False                                     # Don't ask for move
        board, available, move = place_piece(board, available, turn, ask, methods, move)  # Place a piece on the board
        if turn == "X":                                     # If this was X's turn,
            turn = "O"                                      # Next is O's turn
        else:                                               # If this was O's turn,
            turn = "X"                                      # Next is X's turn
        moves += 1                                          # Increment number of moves by 1
        result = win_check(board)                           # Check for wins
    if result == user_letter:                               # If result is user's letter,
        result = '-1'                                       # To be written to file later
        print("You win!")                                   # User wins
    elif result == comp_letter:                             # If result is computer's letter,
        result = '1'                                        # To be written to file later
        print("You lose!")                                  # User loses
    else:                                                   # If result is neither,
        result = '0'                                        # To be written to file later
        print("Draw!")                                      # It is a draw
    print()                                                 # Leave blank line
    if not forced_choice:                                   # Unless user had used 'try this',
                                                            # Note: If 'try this' was used, don't write it into the file
                                                            # (to avoid contamination of thinking process)
        superencrypt(methods, result, moves)                # Encrypt and write the data into the file
    return fxn_scores, forced_choice, show_think, proceed, letter_lock  # Return all the dev tool values (except 'try this')


def encrypt(normal):                                        # Function to encrypt a string/list/function
    if type(normal) == type_str:                            # If argument is a string,
        crypted = ''                                        # Blank string (to add characters one by one)
        for i in normal:                                    # For each character,
            crypted += encrypted[original.index(i)]         # Add the encrypted version to crypted
        return crypted                                      # Return the encrypted string
    elif type(normal) == type_list:                         # If argument is a list,
        allcrypted = ''                                     # Blank string (to add strings one by one)
        if type(normal[0]) == type_str:                     # If the first element of list is a string,
            for s in normal:                                # For each element,
                allcrypted += (encrypt(str(s)) + "\n")      # Add the encrypted version to allcrypted
            return allcrypted                               # Return the encrypted string
        elif type(normal[0]) == type_fxn:                   # If the first element of list is a funciton,
            for f in normal:                                # For each element,
                allcrypted += (encrypt(f) + "\n")           # Add the encrypted version to allcrypted
            return allcrypted                               # Return the encrypted string
    elif type(normal) == type_fxn:                          # If argument is a function,
        ind = functioned_functions.index(normal)            # Find index of function in functioned_functions
        st = stringed_functions[ind]                        # Find corresponding string version in stringed_functions
        st = encrypt(st)                                    # Encrypt the string
        return st                                           # Return the encrypted string


def decrypt(crypted):                                       # Function to decrypt an encrypted string
    if type(crypted) == type_str:                           # If argument is a string,
        normal = ''                                         # Blank string (to add characters one by one)
        for i in crypted:                                   # For each character,
            if i != '\n':                                   # If character is not newline,
                normal += original[encrypted.index(i)]      # Add the decrypted version to normal
        if normal in stringed_functions:                    # If the decrypted string matches a function,
            ind = stringed_functions.index(normal)          # Find index of that function in stringed_functions
            normal = functioned_functions[ind]              # Find corresponding function in functioned_functions
        return normal                                       # Return the decrypted data


def superencrypt(methods, result, moves):                   # Function to write encrypted data to the file
    a, b, c = encrypt(result), encrypt(str(moves)), encrypt(methods)  # Encrypted versions of all three arguments
    final_string = a + "\n" + b + "\n" + c + "\n"           # Add newlines in between
    file = open("Storage.txt", 'a')                         # Open the file in append mode
    file.write(final_string)                                # Write the data to the file
    file.close()                                            # Close the file


def superdecrypt():                                         # Function to get data from file and decrypt it
    file = open("Storage.txt")                              # Open the file in read mode
    lines = file.readlines()                                # List of all the lines in the file
    file.close()                                            # Close the file
    start_points = [0]                                      # The first starting point is zero (first line)
    for ind in range(len(lines)):                           # For each index of lines,
        line = lines[ind]                                   # Get the corresponding line
        if line == "\n":                                    # If line is just newline character (i.e. blank line),
            start_points.append(ind + 1)                    # Add the index of next line to start_points
        line = decrypt(line)                                # Decrypt the line
        try:                                                # Try to:
            lines[ind] = int(line)                          # Convert line to an integer and replace the original one
        except (ValueError, TypeError):                     # If line cannot be converted to integer,
            lines[ind] = line                               # Just replace the original one by line
    last = start_points.pop()                               # Remove and store last starting point (nothing after it)
    start_stop_points = []                                  # The starting and stopping points
    for ind in range(len(start_points)):                    # For index of each starting point,
        start = start_points[ind]                           # The corresponding starting point
        try:                                                # Try to:
            stop = start_points[ind + 1] - 1                # Make the stop point the line before the next start point
        except IndexError:                                  # If this was the last start point,
            stop = last - 1                                 # Make the last stop point the previous line
        tup = (start, stop)                                 # Tuple of start and stop points
        start_stop_points.append(tup)                       # Add the tuple to start_stop_points
    final_dict = {}                                         # Dictionary to store all the data
    for start_stop in start_stop_points:                    # For each (start, stop) tuple,
        start, stop = start_stop                            # Unpack the tuple
        slic = lines[start : stop]                          # Slice of the lines from start to stop
        slic = slic.copy()                                  # Copy to avoid making changes in lines
        result = int(slic.pop(0))                           # The first line will be the result (0, 1, -1)
        moves = int(slic.pop(0))                            # The second line will be the number of moves
        if result == 1:                                     # If comp won that game,
            score = 10                                      # Add a score of 10
        elif result == 0:                                   # If that game was a draw,
            score = 3                                       # Add a score of 3
        else:                                               # If comp lost that game,
            score = -1                                      # Add a score of -1 (negative marking)
        t = (result, moves, score)                          # Tuple of result, moves, score
        sliced = tuple(slic)                                # Must convert to tuple in order to use as a dict key
        if sliced in final_dict:                            # If the tuple sliced is already in final_dict,
            final_dict[sliced].append(t)                    # Append the tuple t to the value (which is a list)
        else:                                               # If the tuple sliced is not in final_dict,
            final_dict[sliced] = [t]                        # Assign the list of the tuple t to the value
    real_final_dict = {}                                    # Final dictionary to be returned
    for key in final_dict:                                  # For each key (i.e. each method),
        value = final_dict[key]                             # The list of tuples of (result, moves, score)
        length = len(value)                                 # The length of the list
        sum_moves = sum_result = sum_score = 0              # Initial values of these variables is zero
        for t in value:                                     # For each tuple of (result, moves, score),
            result, moves, score = t                        # Unpack the tuple
            sum_moves += moves                              # Add the moves to sum_moves
            sum_result += result                            # Add the result to sum_result
            sum_score += score                              # Add the score to sum score
        avg_moves = sum_moves / length                      # Average number of moves taken by this method
        avg_result = sum_result / length                    # Average result of this method
        real_final_dict[key] = (avg_result, avg_moves, sum_score)  # Add the method:tuple pair to real_final_dict
    return real_final_dict                                  # Return the final dictionary of data


stringed_functions = ('next_win', 'next_lose', 'possible_win',
                      'possible_lose', 'centre', 'flank',
                      'anti_flank', 'just_opposite')        # Tuple of all the function names (in string form)
functioned_functions = (next_win, next_lose, possible_win,
                        possible_lose, centre, flank,
                        anti_flank, just_opposite)          # Tuple of all the functions (in function form)


print("TIC TAC TOE\n")                                      # Heading
try:                                                        # Try to:
    f = open("Storage.txt")                                 # Open the file
except FileNotFoundError:                                   # If file does not exist,
    f = open("Storage.txt", "w")                            # Create the file
f.close()                                                   # Close the file
c = 0                                                       # Initial count is zero
BREAK = False                                               # Condition to exit the program
fxn_scores, forced_choice, show_think, proceed, letter_lock = False, False, False, False, False
while not BREAK:                                            # Until BREAK = True,
    if c == 0:                                              # If count is zero (first time),
        fxn_scores, forced_choice, show_think, proceed, letter_lock = play(True, fxn_scores, forced_choice, show_think, proceed, letter_lock)
                                                            # Play with option of dev tools enabled
        c += 1                                              # Increment count by 1 (count is no longer zero)
    else:                                                   # If count is not zero (not the first time),
        play(False, fxn_scores, forced_choice, show_think, proceed, letter_lock)  # Play without option of dev tools enabled
    if not proceed:                                         # If dev had not specified 'always continue',
        while True:                                         # Until break statement,
            s = input("Would you like to play again? Enter 'YES' or 'NO': ")  # Ask whether user wants another game
            if s.upper() == "YES":                          # If user entered YES,
                break                                       # Break out of inner while loop; goes to next game
            elif s.upper() == "NO":                         # If user entered NO,
                BREAK = True                                # Condition to break out of outer while loop; ends program
                break                                       # Break out of inner while loop
            else:                                           # If user entered neither YES nor NO,
                print("Please enter 'YES' or 'NO' only.")   # Request YES or NO only; go to next iteration
