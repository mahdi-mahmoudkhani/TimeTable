
from backTracking import backTracking

def format_Solution(solution):
    '''
    Formats the solution to a more readable format.
    Returns:
        str: A formatted string of the solution.
    '''
    output = "Scheduling Solution:\n"
    output += "-" * 50 + "\n"
    output += f"{'Course':<15}{'Time':<15}{'Classroom':<10}{'Instructor':<15}\n"
    output += "-" * 50 + "\n"

    for vaiable , value in solution['domains'].items():
        timeRoom , instructor = value[0]
        time , classRoom = timeRoom.split("  ")
        output += f"{variable:<15}{time:<15}{classroom:<10}{instructor:<15}\n"
    output += "-" * 50
    return output