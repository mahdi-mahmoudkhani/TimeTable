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
    