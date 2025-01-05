from forwardChecking import forward_checking as fc
from State import State
from mrv import mrv
from lcv import lcv


def backTracking(state: State):
    # check if all courses are assigned
    if state.isFinalState():
        return state

    # select the course with the smallest domain
    course = mrv(state)

    # try each value for the course
    for value in lcv(state, course):
        # create a copy of the state
        new_state = state.__copy__()
        # assign the value to the course
        new_state.AssignValue(course, value)
        # forward checking
        new_state = fc(new_state, course, value)
        # check if the assignment is valid
        if all(len(new_state.domains[c]) > 0 for c in new_state.domains):
            # recursively call backTracking
            result = backTracking(new_state)
            if result:
                return result
        else:
            state.domains[course].remove(value)

    return False
