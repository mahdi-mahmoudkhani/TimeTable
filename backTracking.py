

def backTracking(state):
    '''
    Backtracking algorithm to solve the CSP using MRV, LCV, and Forward Checking.
    Returns:
        dict or None: The completed assignment if successful, otherwise None.
    '''
    # check if the state is complete
    if all(len(state['domains'][variable]) == 1 for variable in state['domains']):
        return state