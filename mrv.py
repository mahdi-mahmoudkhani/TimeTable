

def mrv(state ):
    '''
    Minimum Remaining Values (MRV) heuristic to select the variable with the smallest domain.  
    Returns:
        str: The variable with the smallest domain, or None if all variables are assigned.
'''
    minVar = None
    minDomain = float('inf') #due to comparison
    
    for variable in state['domains']:
        if len(state['domains'][variable]) < minDomain and len(state['domains'][variable]) > 1:
            minVar = variable
            minDomain = len(state['domains'][variable])
            
    return minVar
            
    
    