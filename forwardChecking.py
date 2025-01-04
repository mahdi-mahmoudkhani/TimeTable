from state import State

# Forward Checking function
def forward_checking(state , variable , value):
    '''Forward Checking function to update the domains in the state
    after assigning a value to a variable. '''
    
    #unpacked the value 
    timeRoom ,  instructor = value
    
    for course in state['domains']:
        if course == variable:
            continue #skip the course that was assigned
        newDomain = []
        
        for domain_value in state['domains'][course]:
            #unpack the domain value
            domain_instructor , domain_timeRoom = domain_value
            if domain_timeRoom == timeRoom or domain_instructor == instructor:
                continue  
            newDomain.append(domain_value) 
            
            
        state['domains'][course] = newDomain
        
        # arcs inconsistent if the domain is empty
        if not state['domains'][course]:
            return False
            
    
    return state