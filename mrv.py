
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
            
    
## Sample state for testing
# state = {
#     "domains": {
#         "AI": [("9:00-10:00 Room1", "Dr.Moosavi"), ("10:00-11:00 Room2", "Dr.Shahabi")],
#         "Physics": [("9:00-10:00 Room1", "Dr.Pouzesh"), ("10:00-11:00 Room2", "Dr.Pouzesh")],
#         "Chemistry": [("10:00-11:00 Room2", "Dr.Fathi")],
#     }
# }
# state = mrv(state)
# print(f"Selected variable by MRV: {state}")


