class Student:
    
    
    def __init__(self, studentID, name, group):
        self._studentID = studentID
        self._name = name
        self._group = group

    def get_student_id(self):
        return self.__studentID


    def get_name(self):
        return self.__name


    def get_group(self):
        return self.__group


    def set_student_id(self, value):
        self.__studentID = value


    def set_name(self, value):
        self.__name = value


    def set_group(self, value):
        self.__group = value
        
    def __eq__(self,other):
        return self._studentID == other._studentID
    
    def __str__(self):
        return str(self.get_student_id()) + " " + self.get_name() + " " + str(self.get_group())

    def tuple_return(self):
        return (self.get_student_id(), self.get_name(), self.get_group())
    def get_key(self):
        return self.get_student_id()

    _studentID = property(get_student_id, set_student_id, None, None)
    _name = property(get_name, set_name, None, None)
    _group = property(get_group, set_group, None, None)
        
    
    
    



