from State import State


def mrv(state: State):
    '''
    Minimum Remaining Values (MRV) heuristic to select the course with the smallest domain.  
    Returns:
        str: The course with the smallest domain, or None if all courses are assigned.
    '''
    minVar = None
    minDomain = float('inf')  # due to comparison

    for course in state.domains.keys():
        # if the course has only one value in its domain, it is already assigned
        if len(state.domains[course]) < minDomain and course not in state.assigned:
            minVar = course
            minDomain = len(state.domains[course])

    return minVar
