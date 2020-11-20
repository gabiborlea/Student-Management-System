from datetime import *
class ValidationError(Exception):
    pass

class ValidationStudent:
    
    #This function checks if the given student is valid
    def validate_student(self, student):
        errors = ""
        if student.get_student_id() < 0:
            errors += "invalid id!\n"
        
        if student.get_name() == "":
            errors += "invalid name!\n"
             
        if student.get_group() < 0:
            errors += "invalid group!\n"
            
        if len(errors) > 0:
            raise ValidationError(errors)

class ValidationAssignment:
    
    #This function checks if the given assignment is valid
    def validate_assignment(self, assignment):
        errors = ""
        if assignment.get_assignment_id() < 0:
            errors += "invalid id!\n"
            
        if assignment.get_description() == "":
            errors += "invalid description!\n"
            
            
        if len(errors) > 0:
            raise ValidationError(errors)


class ValidationGrade:
    def validate_grade(self, grade):
        errors = ""
        if grade.get_student_id() < 0:
            errors += "invalid student id!\n"
            
        if grade.get_assignment_id() < 0:
            errors += "invalid assignment id!\n"
            
        if grade.get_grade() < 0 or grade.get_grade() > 10:
            errors += "invalid grade!\n"
            
        if len(errors) > 0:
            raise ValidationError(errors)


