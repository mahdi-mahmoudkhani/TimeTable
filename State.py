class State:
    def __init__(self, courses, instructors, rooms, timeSlots):
        '''
        Initialize the state of the CSP.
        '''
        self.courses = courses
        self.instructors = instructors
        self.rooms = rooms
        self.timeSlots = timeSlots
        self.domains = self.GenerateDomains()
        self.roomTimeChecklist = self.GenerateRoomTimeChecklist()
        self.instructorTimeChecklist = self.GenerateInstructorTimeChecklist()

    def GenerateDomains(self):
        '''
        Generate the domain for each course.
        The domain for each course is a list of tuples. Each tuple contains an instructor and a room-time pair.
        '''
        domains = {}
        for course in self.courses:
            domains[course] = []
            for instructor in self.instructors:
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
        checklist = {}
        for instructor in self.instructors:
            for timeSlot in self.timeSlots:
                checklist[f"{instructor} at {timeSlot}"] = False
        return checklist