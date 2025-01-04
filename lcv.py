
def lcv(state , variable):
    '''
    Least Constraining Value (LCV) heuristic to select the best value for a variable.
    Returns:
        tuple: The value from the domain of the variable that causes the least constraints.
    
    '''
    
    valueConstraints = []
    
    # get the domain of the variable
    domain = state['domains'][variable]
    
    for value in domain:
        # initialize the constraints to 0
        constraints = 0
        # unpack the value
        timeRoom , instructor = value
        
        for otherVar in state['domains']:
            if otherVar == variable:
                continue
            
           