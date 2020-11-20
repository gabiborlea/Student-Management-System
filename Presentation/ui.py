from Infrastracture.repo import RepoError
from datetime import date
from Validations.validations import ValidationError
class UI:
    
    def __init__(self, servStudents, servAssignments, servGrades, servUndo):
        self._servStudents = servStudents
        self._servAssignments = servAssignments
        self._servGrades = servGrades
        self._servUndo = servUndo
    
    def _ui_print_menu(self):
        print("Choose an option")
        print("1. Add a student")
        print("2. Show students")
        print("3. Delete student")
        print("4. Update student")
        print("5. Add an assignment")
        print("6. Show assignments")
        print("7. Delete assignment")
        print("8. Update assignment")
        print("9. Assign assignment to student")
        print("10. Assign assignment to group")
        print("11. Show all grades")
        print("12. Grade student for a given assignment")
        print("13. All students who received a given assignment")
        print("14. All students who are late in handing in at least one assignment")
        print("15. Students with the best school situation")
        print("16. Exit")
        print("u: Undo")
        print("r: Redo")
        
    def _ui_add_student(self):
        studentID = input("Give id: ")
        name = input("Give name: ")
        group = input("Give group: ")
        
        errors = ""
        
        try:
            studentID = int(studentID)
        except ValueError:
            errors += "Invalid id!\n"
            
        try:
            group = int(group)
        except ValueError:
            errors += "Invald group\n"
            
        if len(errors) == 0:
            try:
                self._servStudents.add_student(studentID, name, group)
            except Exception as error:
                    print(error)
        else:
            print(errors)
            
    def _ui_show_students(self):
        for student in self._servStudents.get_students():
            print(student)
            
    def _ui_delete_student(self):
        studentID = input("Give the student's id that you want to delete: ")
        errors = ""
        try:
            studentID = int(studentID)
        except ValueError:
            errors += "invalid id\n"
            
        if len(errors) == 0:
            try:
                student = self._servStudents.get_student_by_id(studentID)
                print("Do you want to delete " + str(student) + " ? (y/n)")
        
                choice = input("(y/n): ")
                if choice == 'y':
                    self._servStudents.delete_student(studentID)
                    
            except RepoError as error:
                print(error)
        else:
            print(errors)
            
    def _ui_update_student(self):
        
        studentID = input("Give the student's id that you want to update: ")
        errors = ""
        try:
            studentID = int(studentID)
        except ValueError:
            errors += "invalid id\n"
            
        if len(errors) == 0:
            try:
                student = self._servStudents.get_student_by_id(studentID)
                print("Do you want to update " + str(student) + " ? (y/n)")
        
                choice = input("(y/n): ")
                if choice == 'y':
                        name = input("New name: ")
                        group = int(input("New group: "))
                        self._servStudents.update_student(studentID, name, group)
                        
            except ValueError:
                print("Invalid group\n")
            except Exception as error:
                print(error)
        else:
            print(errors)
    

    def _ui_add_assignment(self):
        assignmentID = input("Give id: ")
        description = input("Give description: ")
        deadl = input("Give deadline (year-month-day): ")
        deadl = deadl.split('-')
        
        errors = ""
        
        if len(deadl) == 3:
            try:
                year = int(deadl[0])
                month = int(deadl[1])
                day = int(deadl[2])
                deadline = date(year, month, day)
            except ValueError:
                errors += "invalid deadline\n"
                
        else:
            errors += "invalid deadline\n"
            
        try:
            assignmentID = int(assignmentID)
        except ValueError:
            errors += "invalid id\n"
            
        if len(errors) == 0:
            try: 
                self._servAssignments.add_assignment(assignmentID, description, deadline)
            except Exception as error:
                print(error)
        else:
            print(errors)
            
    def _ui_show_assignments(self):
        for assignment in self._servAssignments.get_assignments():
            print(assignment)
            
            
    def _ui_delete_assignment(self):
        assignmentID = input("Give the assignemnt's id that you want to delete: ")
        errors = ""
        try:
            assignmentID = int(assignmentID)
        except ValueError:
            errors += "invalid id\n"
            
        if len(errors) == 0:
            try:
                assignment = self._servAssignments.get_assignment_by_id(assignmentID)
                print("Do you want to deltele " + str(assignment) + " ?")
        
                choice = input("(y/n): ")
                if choice == 'y':
                    self._servAssignments.delete_assignment(assignmentID)
                    
            except RepoError as error:
                print(error)
        else:
            print(errors)
            
    def _ui_update_assignment(self):
        
        assignmentID = input("Give the assignment's id that you want to update: ")
        errors = ""
        try:
            assignmentID = int(assignmentID)
        except ValueError:
            errors += "invalid id\n"
            
        if len(errors) == 0:
            try:
                assignment = self._servAssignments.get_assignment_by_id(assignmentID)
                print("Do you want to update " + str(assignment) + " ?")
        
                choice = input("(y/n): ")
                if choice == 'y':
                    description = input("New description: ")
                    deadl = input("New deadline (year-month-day): ")
                    deadl = deadl.split('-')
                    
                    if len(deadl) == 3:
                        year = int(deadl[0])
                        month = int(deadl[1])
                        day = int(deadl[2])
                        deadline = date(year, month, day)
                        self._servAssignments.update_assignment(assignmentID, description, deadline)
                    
                    else:
                        raise ValueError
                        
            except ValueError:
                print("Invalid deadline\n")
            except Exception as error:
                print(error)
        else:
            print(errors)
            
    def _ui_assign_assignment_to_student(self):
        assignmentID = input("Give assignment id:")
        studentID = input("Give student id: ")
        try:
            assignmentID = int(assignmentID)
            studentID = int(studentID)
            self._servStudents.get_student_by_id(studentID)
            self._servAssignments.get_assignment_by_id(assignmentID)
            self._servGrades.assign_assignment_to_student(assignmentID, studentID)
            
        except ValueError:
            print("Invalid inputs")
            
        except Exception as error:
            print(error)
            
    def _ui_assign_assignment_to_group(self):
        assignmentID = input("Give assignment id:")
        group = input("Give group: ")
        try:
            assignmentID = int(assignmentID)
            group = int(group)
            self._servAssignments.get_assignment_by_id(assignmentID)
            self._servGrades.assign_assignment_to_group(group, assignmentID, self._servStudents)
            
        except ValueError:
            print("Invalid inputs\n")
            
        except Exception as error:
            print(error)
   
            
    def _ui_show_grades(self):
        for grade in self._servGrades.get_all_grades():
            print(grade)
            
    def _ui_show_graded(self, studentID):
        print(" ")
        print("Graded assignmnets:")
        for assignmentID in self._servGrades.get_graded(studentID):
            print(self._servAssignments.get_assignment_by_id(assignmentID))
            
    def _ui_show_ungraded(self, studentID):
        print(" ")
        print("Ungraded assignments:")
        for assignmentID in self._servGrades.get_ungraded(studentID):
            print(self._servAssignments.get_assignment_by_id(assignmentID))
            
    def _ui_grade_student(self):
        
        try:
            studentID = int(input("Give student's ID: "))
            the_student = self._servStudents.get_student_by_id(studentID)
            print("The student:  " + str(the_student))
            self._ui_show_graded(studentID)
            self._ui_show_ungraded(studentID)
            print(" ")
            assignmentID = int(input("Give assignment's ID: "))
            the_assignment = self._servAssignments.get_assignment_by_id(assignmentID)
            grade = int(input("Give garde: "))
            self._servGrades.update_grade(studentID, assignmentID, grade)
        except ValueError:
            print("Invalid id!")
        except RepoError as error:
            print(error)
        except Exception as error:
            print(error)
    
    def _ui_statistic_given_assignment(self):
        try:
            assignmentID = int(input("Give assignmnet id: "))
            the_assignment = self._servAssignments.get_assignment_by_id(assignmentID)
            print("The assignment: " + str(the_assignment))
            the_list = self._servGrades.get_students_by_assignment(assignmentID)
            for grade in the_list:
                print(str(self._servStudents.get_student_by_id(grade.get_student_id())) + "| grade: "+ str(grade.get_grade()))
                
        except ValueError:
            print("Invalid Id")
        except RepoError as error:
            print(error)
    
    def _ui_statistic_deadline_passed(self):
        stud_list = self._servGrades.dead_line_passed()
        for student in stud_list:
            print(str(self._servStudents.get_student_by_id(student[0])), str(self._servAssignments.get_assignment_by_id(student[1]).get_deadline()))
    
    def _ui_statistic_best_students(self):
        students_list = self._servGrades.best_students()
        for student in students_list:
            print(str(self._servStudents.get_student_by_id(student[0])) + "| avg: "+ str(student[1]))

    def _ui_undo(self):
        try:
            self._servUndo.undo()
        except Exception as error:
            print(error)

    def _ui_redo(self):
        try:
            self._servUndo.redo()
        except Exception as error:
            print(error)
    def start(self):
            
        while True:
            self._ui_print_menu()
            choice = input(">>>")
                
            if choice == '1':
                self._ui_add_student()
                    
            if choice == '2':
                self._ui_show_students()
                
            if choice == '3':
                self._ui_delete_student()
                
            if choice == '4':
                self._ui_update_student()
                    
            if choice == '5':
                self._ui_add_assignment()
                
            if choice == '6':
                self._ui_show_assignments()
                
            if choice == '7':
                self._ui_delete_assignment()
                
            if choice == '8':
                self._ui_update_assignment()
            
            if choice == '9':
                self._ui_assign_assignment_to_student()
            
            if choice == '10':
                self._ui_assign_assignment_to_group()
            
            if choice == '11':
                self._ui_show_grades()
                
            if choice == '12':
                self._ui_grade_student()
                
            if choice == '13':
                self._ui_statistic_given_assignment()
                
            if choice == '14':
                self._ui_statistic_deadline_passed()
                
            if choice == '15':
                self._ui_statistic_best_students()
                
            if choice == '16':
                break

            if choice == 'u':
                self._ui_undo()

            if choice == 'r':
                self._ui_redo()
        


