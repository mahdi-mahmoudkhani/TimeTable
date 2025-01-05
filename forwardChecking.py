from State import State


def forward_checking(state: State, variable, value):
    '''
    Forward Checking function to update the domains in the state
    after assigning a value to a variable.
    '''

    # unpacked the value
    instructor, roomTime = value

    for course in state.domains.keys():
        if course == variable:
            continue  # skip the course that was assigned
        newDomain = []

        for domain_value in state.domains[course]:
            # unpack the domain value
            domainInstructor, domainRoomTime = domain_value
            # check if the domain value is consistent with the assigned value
            if domainRoomTime == roomTime:
                continue
            if domainRoomTime.split(" at ")[1] == roomTime.split(" at ")[1] and domainInstructor == instructor:
                continue
            # if the domain value is consistent, add it to the new domain
            newDomain.append(domain_value)
        state.domains[course] = newDomain

    return state
