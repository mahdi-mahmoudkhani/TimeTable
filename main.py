from givenData import instructors, classrooms, time_slots
from State import State
from backTracking import backTracking
from format import format_Solution


def main():
    initialState = State(instructors.keys(),
                         instructors.values(), classrooms, time_slots)
    solution = backTracking(initialState)
    table = format_Solution(solution)
    print(table)


if __name__ == "__main__":
    main()
