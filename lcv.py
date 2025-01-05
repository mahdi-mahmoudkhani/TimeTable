from State import State


def lcv(state: State, variable):
    '''
    Least Constraining Value (LCV) heuristic to select the best value for a variable.
    Returns:
        tuple: The value from the domain of the variable that causes the least constraints.

    '''
    valueConstraints = []
    # get the domain of the variable
    domain = state.domains[variable]

    for value in domain:
        # initialize the constraints to 0
        constraints = 0
        # unpack the value
        instructor, roomTime = value
        for otherVar in state.domains.keys():
            if otherVar == variable:
                continue
            for otherValue in state.domains[otherVar]:
                otherInstructor, otherRoomTime = otherValue
                if otherRoomTime == roomTime or otherInstructor == instructor:
                    constraints += 1
        # append the value and its constraints to the list
        valueConstraints.append((value, constraints))
    # sort the values based on the lowest constraints
    valueConstraints.sort(key=lambda x: x[1])

    # print(valueConstraints)
    return valueConstraints[0][0]
