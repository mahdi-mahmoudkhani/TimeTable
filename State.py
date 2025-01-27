class State:
    def __init__(self, courses: dict, instructors: dict, rooms: list, timeSlots: list):
        '''
        Initialize the state of the CSP.
        '''
        self.courses = list(courses)
        self.instructors = list(instructors)
        self.rooms = rooms
        self.timeSlots = timeSlots
        self.domains = self.GenerateDomains()
        self.roomTimeChecklist = self.GenerateRoomTimeChecklist()
        self.instructorTimeChecklist = self.GenerateInstructorTimeChecklist()
        self.assigned = set()

    def GenerateDomains(self):
        '''
        Generate the domain for each course.
        The domain for each course is a list of tuples. Each tuple contains an instructor and a room-time pair.
        '''
        domains = {}
        for course in self.courses:
            domains[course] = []
            for instructor in self.instructors[self.courses.index(course)]:
                for room in self.rooms:
                    for timeSlot in self.timeSlots:
                        domains[course].append((instructor, f"{room} at {timeSlot}"))
        return domains
    
    def GenerateRoomTimeChecklist(self):
        '''
        Generate a checklist to track room-time pairs that are already assigned using Boolean values.
        At the beginning, all room-time pairs are unassigned; hence, all values are False.
        '''
        checklist = {}
        for room in self.rooms:
            for timeSlot in self.timeSlots:
                checklist[f"{room} at {timeSlot}"] = False
        return checklist
    
    def GenerateInstructorTimeChecklist(self):
        '''
        Generate a checklist to track instructor-time pairs that are already assigned using Boolean values.
        At the beginning, all instructor-time pairs are unassigned; hence, all values are False.
        '''
        allIntructors = set()
        for instructors in self.instructors:
            allIntructors = allIntructors.union(set(instructors))
        checklist = {}
        for instructor in allIntructors:
            for timeSlot in self.timeSlots:
                checklist[f"{instructor} at {timeSlot}"] = False
        return checklist
    
    def AssignValue(self, course, value):
        '''
        Assign a value to a course. The value is a tuple of instructor and room-time pair.
        Check if the room-time pair and instructor-time pair are already assigned.
        If not, assign the value to the course and update the checklists.
        '''
        instructor, roomTime = value
        if self.roomTimeChecklist[roomTime] or self.instructorTimeChecklist[f"{instructor} at {roomTime.split(' at ')[1]}"]:
            return False
        self.roomTimeChecklist[roomTime] = True
        self.instructorTimeChecklist[f"{instructor} at {roomTime.split(' at ')[1]}"] = True
        self.domains[course] = [value]
        self.assigned.add(course)
        return True
    
    def isFinalState(self):
        '''
        Check if the state is a final state.
        A state is a final state if all courses are assigned.
        '''
        return len(self.assigned) == len(self.courses)
    
    def __copy__(self):
        '''
        Create a copy of the state.
        '''
        newState = State(self.courses, self.instructors, self.rooms, self.timeSlots)
        newState.domains = self.domains.copy()
        newState.roomTimeChecklist = self.roomTimeChecklist.copy()
        newState.instructorTimeChecklist = self.instructorTimeChecklist.copy()
        newState.assigned = self.assigned
        return newState