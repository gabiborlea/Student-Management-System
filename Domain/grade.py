from _operator import ge
class Grade(object):
    
    def __init__(self, studentID, assignmentID, grade):
        self._studentID = studentID
        self._assignmentID = assignmentID
        self._grade = grade

    def get_student_id(self):
        return self.__studentID


    def get_assignment_id(self):
        return self.__assignmentID


    def get_grade(self):
        return self.__grade


    def set_student_id(self, value):
        self.__studentID = value


    def set_assignment_id(self, value):
        self.__assignmentID = value


    def set_grade(self, value):
        self.__grade = value
        
    def __eq__(self, other):
        return self.get_student_id() == other.get_student_id() and self.get_assignment_id() == other.get_assignment_id()
    
    def __str__(self):
        return str(self.get_student_id()) + " " + str(self.get_assignment_id()) + " " + str(self.get_grade())

    def tuple_return(self):
        return (self.get_student_id(), self.get_assignment_id(), self.get_grade())

    _studentID = property(get_student_id, set_student_id, None, None)
    _assignmentID = property(get_assignment_id, set_assignment_id, None, None)
    _grade = property(get_grade, set_grade, None, None)
        
    


