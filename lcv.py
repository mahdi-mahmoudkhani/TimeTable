
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
            
            for otherValue in state['domains'][otherVar]:
                otherTimeRoom , otherInstructor = otherValue
                if otherTimeRoom == timeRoom or otherInstructor == instructor:
                    constraints += 1
                    
        # append the value and its constraints to the list   
        valueConstraints.append((value , constraints))
    #sort the values based on the lowest constraints
    valueConstraints.sort(key = lambda x : x[1] )
    #print(valueConstraints)

    return valueConstraints[0][0] 

# # Sample state for testing
# state = {
#     "domains": {
#         "AI": [("9:00-10:00 Room1", "Dr.Moosavi"), ("10:00-11:00 Room2", "Dr.Shahabi")],
#         "Physics": [("9:00-10:00 Room1", "Dr.Pouzesh"), ("10:00-11:00 Room2", "Dr.Pouzesh")],
#         "Chemistry": [("10:00-11:00 Room2", "Dr.Fathi")],
#     }
# }

# selected_value = lcv(state, "AI")
# print(f"Selected value by LCV: {selected_value}")
            
           