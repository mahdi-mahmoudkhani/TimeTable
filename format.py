from tabulate import tabulate
from State import State


def format_Solution(solution: State):
    '''
    Formats the solution as a table for better readability.
    Returns:
        str:  A formatted string of the solution in table form.
    '''
    table_data = []
    for course, assignment in solution.domains.items():
        instructor, room_time = assignment[0]
        room, time = room_time.split(" at ")
        table_data.append([course, instructor, room, time])

    headers = ["Course", "Instructor", "Classroom", "Time"]
    return tabulate(table_data, headers, tablefmt="grid")
