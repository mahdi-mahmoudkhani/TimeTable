from backTracking import backTracking
from format import format_Solution
from State import State

def main():
    # Sample input state
    state = {
        "domains": {
            "AI": [("9:00-10:00 Room1", "Dr.Moosavi"), ("10:00-11:00 Room2", "Dr.Shahabi")],
            "Physics": [("9:00-10:00 Room1", "Dr.Pouzesh"), ("10:00-11:00 Room3", "Dr.Pouzesh")],
            "Chemistry": [("10:00-11:00 Room2", "Dr.Fathi"), ("9:00-10:00 Room3", "Dr.Karimi")],
        }
    }
    
    # state = {
    # "domains": {
    #     "AI": [("9:00-10:00 Room1", "Dr.Moosavi"), ("10:00-11:00 Room2", "Dr.Shahabi")],
    #     "Physics": [("9:00-10:00 Room2", "Dr.Pouzesh"), ("10:00-11:00 Room1", "Dr.Pouzesh")],
    #     "Chemistry": [("10:00-11:00 Room3", "Dr.Fathi"), ("9:00-10:00 Room3", "Dr.Karimi")],
    # }
    #  }
    # state = {
    # "domains": {
    #     "Math": [("9:00-10:00 Room1", "Dr.A"), ("10:00-11:00 Room2", "Dr.B")],
    #     "Biology": [("9:00-10:00 Room1", "Dr.A"), ("10:00-11:00 Room3", "Dr.C")],
    #     "History": [("10:00-11:00 Room1", "Dr.D"), ("11:00-12:00 Room2", "Dr.E")],
    #     "Physics": [("9:00-10:00 Room2", "Dr.A"), ("10:00-11:00 Room3", "Dr.B")],
    # }
    # }

    # Run the backtracking algorithm
    solution = backTracking(state)
     # Print the solution in a formatted table
    if solution:
        print("|||||  Scheduling Solution:\n")
        print("---->  Solution Found:")
        print(format_Solution(solution))
    else:
        print("No solution found.")
        

if __name__ == "__main__":
    main()