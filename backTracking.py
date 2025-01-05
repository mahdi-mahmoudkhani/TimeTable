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
    while True:
        value = lcv(state, course)
        if not value:
            return False
        # create a copy of the state
        new_state = state.__copy__()
        # assign the value to the course
        if not new_state.AssignValue(course, value):
            break
        # forward checking
        new_state = fc(new_state, course, value)
        # check if the assignment is valid
        if all(len(new_state.domains[c]) > 0 for c in new_state.domains if c != course):
            # recursively call backTracking
            result = backTracking(new_state)
            if result:
                return result
        # remove the value from the domain of the original state
        state.domains[course].remove(value)
