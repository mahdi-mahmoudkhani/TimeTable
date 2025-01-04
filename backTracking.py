
from mrv import mrv
from lcv import lcv
from forwardChecking import forward_checking as fc

def backTracking(state):
    '''
    Backtracking algorithm to solve the CSP using MRV, LCV, and Forward Checking.
    Returns:
        dict or None: The completed assignment if successful, otherwise None.
    '''
    # check if the state is complete
    if all(len(state['domains'][variable]) == 1 for variable in state['domains']):
        return state
    
    # select the variable with the smallest domain
    variable = mrv(state)
    
    if variable is None:
        return None
    
    # iterate over the values in the domain of the variable
    for value in state['domains'][variable]:
        # check if the value is consistent with the assignment
        original_domains = state['domains'].copy()
        
        state['domains'][variable] = [value]
        
        #forward checking
        if fc(state , variable , value) :
            result = backTracking(state)
            if result is not None:
                return result