from State import State

# Forward Checking function
def forward_checking(state , variable , value):
    '''Forward Checking function to update the domains in the state
    after assigning a value to a variable. '''
    
    #unpacked the value 
    timeRoom ,  instructor = value
    assignedTime , assignedRoom = timeRoom.split(" ")
    
    for course in state['domains']:
        if course == variable:
            continue #skip the course that was assigned
        newDomain = []
        
        for domain_value in state['domains'][course]:
            #unpack the domain value
            domainTimeRoom , domainInstructor = domain_value
            domainTime , domainRoom = domainTimeRoom.split(" ")
            
            #check if the domain value is consistent with the assigned value
            if domainTime == assignedTime and domainRoom == assignedRoom :
                continue  
            if  domainTime == assignedTime and domainInstructor == instructor  :
                continue
            
            newDomain.append(domain_value) 
            
            
        state['domains'][course] = newDomain
        
        # arcs inconsistent if the domain is empty
        if not state['domains'][course]:
            return False
            
    
    return state