# NEcessary OBjects
assignments = []


def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [s + t for s in A for t in B]


def get_unitlist(solving_diag=False):
    if solving_diag:
        return row_units + column_units + square_units + diag_units
    else:
        return row_units + column_units + square_units


rows = 'ABCDEFGHI'
cols = '123456789'

boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [
    cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI')
    for cs in ('123', '456', '789')
]
diag_units = [[rows[i] + cols[i]
               for i in range(9)], [rows[::-1][i] + cols[i] for i in range(9)]]
unitlist = get_unitlist(solving_diag=True)

units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s], [])) - set([s])) for s in boxes)


def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    """
    Don't waste memory appending actions that don't actually change any values
    """
    if values[box] == value:
        return values

    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values


def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    # First select boxes with 2 entries
    potential_twins = [box for box in values.keys() if len(values[box]) == 2]

    # Collect boxes that have the same elements
    naked_twins = [[box1, box2]
                   for box1 in potential_twins for box2 in peers[box1]
                   if set(values[box1]) == set(values[box2])]
    # Now we have our Naked_twins, we need to loop through them
    for twin_set in naked_twins:
        # Gather the individual twins and fetch their peers
        box1 = twin_set[0]
        box2 = twin_set[1]
        peers1 = peers[box1]
        peers2 = peers[box2]
        # Now that we have their peers, let's grab their shared peers
        tot_peers = peers1.intersection(peers2) & peers2.intersection(peers1)
        # and define a list of peers we want to remove values from
        peers_to_update = [
            peer for peer in tot_peers if len(values[peer]) >= 2
        ]
        # Let's loop through the twins' shared two digits
        digits = set(values[box1])
        # and replace them with nothing!
        for peer in peers_to_update:
            for digit in digits:
                values = assign_value(values, peer, values[peer].replace(
                    digit, ''))
    return values


def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    all_values = '123456789'
    values = []  # New list to replace Grid
    for i in grid:
        if i == '.':
            values.append(all_values)
        elif i in all_values:
            values.append(i)
    return dict(zip(boxes, values))


def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1 + max(len(values[s]) for s in boxes)
    line = '+'.join(['-' * (width * 3)] * 3)
    for r in rows:
        print(''.join(values[r + c].center(width) + ('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF':
            print(line)
    return


def eliminate(values):
    """
    When a box is already solved, i.e. only has one value, then we can and
    should remove that value from it's peers
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]

    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values = assign_value(values, peer, values[peer].replace(
                digit, ''))
    return values


def only_choice(values):
    """
    Assign a box a value that only appears as an option for a certain box
    among a set of peers
    """
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
    return values


def reduce_puzzle(values):
    """
    Iterate eliminate() and only_choice(). If at some point, there is a box with no available values, return False.
    If the sudoku is solved, return the sudoku.
    If after an iteration of both functions, the sudoku remains the same, return the sudoku.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    stalled = False
    while not stalled:
        solved_values_before = len(
            [box for box in values.keys() if len(values[box]) == 1])
        values = eliminate(values)
        values = only_choice(values)
        values = naked_twins(values)

        solved_values_after = len(
            [box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values


def search(values):
    """
    Using depth-first search and propagation, try all possible values.
    """

    # First we want ot reduce the puzzle wtih our previous methods.
    values = reduce_puzzle(values)
    if values is False:
        return False  # The puzzle previously Failed
    if all(len(values[s]) == 1 for s in boxes):
        return values  # The puzzle is solved! ALL boxes have one value

    # Now we must choose one of the unfilled squares with the fewest possibilities
    # This will be our starting point for our search tree.
    n, s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each of the resulting sudokus
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt


def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values = grid_values(grid)
    puzzle_solved = search(values)
    if puzzle_solved:
        return puzzle_solved
    else:
        return False


if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print(
            'We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.'
        )
