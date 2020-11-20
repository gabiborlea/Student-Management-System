class Assignment:
    
    
    def __init__(self, assignmentID, description, deadline):
        self._assignmentID = assignmentID
        self._description = description
        self._deadline = deadline

    def get_assignment_id(self):
        return self.__assignmentID


    def get_description(self):
        return self.__description


    def get_deadline(self):
        return self.__deadline


    def set_assignment_id(self, value):
        self.__assignmentID = value


    def set_description(self, value):
        self.__description = value


    def set_deadline(self, value):
        self.__deadline = value
        
    def __eq__(self, other):
        return self._assignmentID == other._assignmentID
    
    def __str__(self):
        date_time = self.get_deadline().strftime("%Y-%m-%d")
        return str(self.get_assignment_id()) + " " + str(self.get_description()) + " " + str(date_time)

    def tuple_return(self):
        date_time = self.get_deadline().strftime("%Y-%m-%d")
        return (self.get_assignment_id(), self.get_description(), date_time)

    def get_key(self):
        return self.get_assignment_id()
    _assignmentID = property(get_assignment_id, set_assignment_id, None, None)
    _description = property(get_description, set_description, None, None)
    _deadline = property(get_deadline, set_deadline, None, None)
    
    
    



