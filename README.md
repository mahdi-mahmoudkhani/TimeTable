
# 📅 TimeTable Scheduler

## 🚀 Project Overview
This project is an intelligent scheduling system designed to allocate courses, instructors, classrooms, and time slots while avoiding conflicts. The system employs advanced algorithms to ensure constraints are satisfied and optimal scheduling is achieved.

✨ **Key Features**:
- Automatically schedules multiple courses while adhering to constraints.
- Utilizes advanced algorithms for efficient scheduling:
  - **MRV**: Chooses the variable with the smallest remaining values in its domain.
  - **LCV**: Selects the value that imposes the fewest constraints on other variables.
  - **Forward Checking**: Eliminates inconsistent values from domains.
- Outputs the schedule in a clear, tabular format.

---

## 🔍 Problem Statement
### Definition:
- Each course must be assigned:
  1. An **instructor**.
  2. A **classroom**.
  3. A **time slot**.

### Constraints:
1. A classroom cannot host more than one course at the same time.
2. An instructor cannot teach more than one course at the same time.
3. Each course's domain is limited by predefined instructors, classrooms, and time slots.

---

## 🛠️ Prerequisites
To run the project, ensure the following:
1. **Python 3.7 or later** is installed.
2. Install the required libraries:
   ```bash
   pip install tabulate

📁 File Structure
```
├── backTracking.py       # Backtracking algorithm for solving CSP
├── forwardChecking.py    # Implementation of Forward Checking
├── mrv.py                # Minimum Remaining Values heuristic
├── lcv.py                # Least Constraining Value heuristic
├── format.py             # Formatting output as a table
├── givenData.py          # Input data (courses, instructors, classrooms, time slots)
├── State.py              # State management and domain handling
├── main.py               # Main entry point for the project
└── README.md             # Project documentation
```

📝 Project Workflow

🌟 1. GenerateDomains
	•	Purpose: Generate the possible domains for each course.
	•	Input: List of courses, instructors, classrooms, and time slots.
	•	Output: A dictionary mapping each course to its list of possible values (instructor, classroom-time pairs).

🌟 2. AssignValue
	•	Purpose: Assign a value to a course and update the state.
	•	Input: Course name, assigned value (instructor, classroom-time).
	•	Output: True if the assignment is valid, otherwise False.

🌟 3. MRV
	•	Purpose: Select the variable with the smallest number of possible values (domain size).
	•	Input: Current state of the problem.
	•	Output: The name of the course to be assigned next.

🌟 4. LCV
	•	Purpose: Select the value that imposes the least constraints on other variables.
	•	Input: Current state of the problem, target course.
	•	Output: The value to be assigned.

🌟 5. Forward Checking
	•	Purpose: Remove inconsistent values from domains after assigning a value to a variable.
	•	Input: Current state, course, and assigned value.
	•	Output: Updated state.

🌟 6. Backtracking
	•	Purpose: Recursively explore assignments to variables, backtracking when conflicts arise.
	•	Input: Current state of the problem.
	•	Output: The final state if a solution is found, or None if no solution exists.

🎯 How to Run
	1.	Execute the main.py file:

python main.py
	2.	Input data, including courses, instructors, classrooms, and time slots, is defined in the ``` givenData.py ``` file.

💡 Sample Output

After running the project, the generated schedule will be displayed in a table format:
```
+-----------+-------------+------------+-----------+
| Course    | Instructor  | Classroom  | Time      |
+-----------+-------------+------------+-----------+
| AI        | Dr.Moosavi  | Room1      | 9:00-10:00|
| Physics   | Dr.Pouzesh  | Room2      | 10:00-11:00|
| Chemistry | Dr.Fathi    | Room3      | 11:00-12:00|
+-----------+-------------+------------+-----------+
```
🔬 How to Test

You can define new inputs in the givenData.py file for testing. Example:
```
state = State(
    courses=["Math", "Physics"],
    instructors={
        "Math": ["Dr.A", "Dr.B"],
        "Physics": ["Dr.C"]
    },
    rooms=["Room1", "Room2"],
    timeSlots=["9:00-10:00", "10:00-11:00"]
)
```

⚙️ Limitations
	•	Increasing the number of variables (courses) and constraints may significantly increase runtime.
	•	If domains are overly restrictive, the algorithm may fail to find a solution.

🌟 Future Enhancements
	1.	Add a graphical user interface (GUI) for modifying inputs and viewing results.
	2.	Optimize algorithms using advanced techniques like Local Search.

✨ Authors
	•	Name: Mahsa Haghnevis  , Mahdi Mahmoudkhani

---
