
from backTracking import backTracking

#if u run it make sure to install tabulate by running ' pip install tabulate '
from tabulate import tabulate
def format_Solution(solution):
    '''
    Formats the solution as a table for better readability.
    Returns:
        str:  A formatted string of the solution in table form.
    '''
    table_data = []
    for course, assignment in solution['domains'].items():
        time_room, instructor = assignment[0]
        time, room = time_room.split(" ")
        table_data.append([course, instructor, room, time])
     
    headers = ["Course", "Instructor", "Classroom", "Time"]
    return tabulate(table_data, headers, tablefmt="grid")
        
