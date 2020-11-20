from Domain.student import Student
from Validations.validations import ValidationStudent
from Domain.assignment import Assignment
from Domain.grade import Grade
from Infrastracture.repo import RepoError
from datetime import date, datetime
from Domain.operation import FunctionCall, Operation, CascadedOperation


class ServiceStudents:

    def __init__(self, undo_service, students_repo, grades_repo,  valid_student):
        self._undo_service = undo_service
        self._students_repo = students_repo
        self._grades_repo = grades_repo
        self._valid_student = valid_student

    # This function returns the size students repo
    def get_nr_students(self):
        return self._students_repo.size()

    # This function adds a new student to the repo
    # params: studentID, name, group
    def add_student(self, studentID, name, group):
        student = Student(studentID, name, group)
        self._valid_student.validate_student(student)
        self._students_repo.add(student)

        undo = FunctionCall(self.delete_student, studentID)
        redo = FunctionCall(self.add_student, studentID, name, group)
        self._undo_service.add_operation(Operation(undo, redo))

    # This function checks if a setudent is in the students repo
    def get_student_by_id(self, studentID):
        key = Student(studentID, None, None)
        return self._students_repo.search(key)

    # This function returns the repo of students
    def get_students(self):
        return self._students_repo.get_all()

    # This function delets a student by the id
    def delete_student(self, studentID):
        cascaded_operation = CascadedOperation()
        stud = self.get_student_by_id(studentID)
        self._students_repo.delete(stud)

        undo = FunctionCall(self.add_student, studentID, stud.get_name(), stud.get_group())
        redo = FunctionCall(self.delete_student, studentID)
        cascaded_operation.record_operation(Operation(undo, redo))

        i = 0
        while i < len(self._grades_repo.get_all()):
            if self._grades_repo.get_all()[i].get_student_id() == studentID:
                undo = FunctionCall(self._grades_repo.add, self._grades_repo.get_all()[i])
                redo = FunctionCall(self._grades_repo.delete, self._grades_repo.get_all()[i])
                cascaded_operation.record_operation(Operation(undo, redo))
                self._grades_repo.delete(self._grades_repo.get_all()[i])
            else:
                i += 1

        self._undo_service.add_operation(cascaded_operation)


    # This function updates a student's info
    def update_student(self, studentID, name, group):
        new_stud = Student(studentID, name, group)
        self._valid_student.validate_student(new_stud)
        stud = self.get_student_by_id(studentID)
        self._students_repo.update(stud, new_stud)
        undo = FunctionCall(self._students_repo.update, new_stud, stud)
        redo = FunctionCall(self._students_repo.update, stud, new_stud)
        self._undo_service.add_operation(Operation(undo, redo))


class ServiceAssignments:

    def __init__(self, undo_service, assignments_repo, grades_repo, valid_assignment):
        self._undo_service = undo_service
        self._assignments_repo = assignments_repo
        self._grades_repo = grades_repo
        self._valid_assignment = valid_assignment

    # This function adds a new assignment to the repo
    # params: assignmentID, description, deadline
    def add_assignment(self, assignmentID, description, deadline):
        assignment = Assignment(assignmentID, description, deadline)
        self._valid_assignment.validate_assignment(assignment)
        self._assignments_repo.add(assignment)

        undo = FunctionCall(self._assignments_repo.delete, assignment)
        redo = FunctionCall(self._assignments_repo.add, assignment)
        self._undo_service.add_operation(Operation(undo, redo))

    # This function returns the number of assignments from the repo
    def get_nr_assignements(self):
        return self._assignments_repo.size()

    # This function checks if a assignment is in the repo
    def get_assignment_by_id(self, assignmentID):
        key = Assignment(assignmentID, None, None)
        return self._assignments_repo.search(key)

    # This function returns the repo of assignments
    def get_assignments(self):
        return self._assignments_repo.get_all()

    # This function deletes an assignment from the repo
    def delete_assignment(self, assignmentID):
        cascaded_operation = CascadedOperation()
        assignment = self.get_assignment_by_id(assignmentID)
        self._assignments_repo.delete(assignment)

        undo = FunctionCall(self._assignments_repo.add, assignment)
        redo = FunctionCall(self._assignments_repo.delete, assignment)
        cascaded_operation.record_operation(Operation(undo, redo))

        i = 0
        while i < len(self._grades_repo.get_all()):
            if self._grades_repo.get_all()[i].get_assignment_id() == assignmentID:
                undo = FunctionCall(self._grades_repo.add, self._grades_repo.get_all()[i])
                redo = FunctionCall(self._grades_repo.delete, self._grades_repo.get_all()[i])
                cascaded_operation.record_operation(Operation(undo, redo))
                self._grades_repo.delete(self._grades_repo.get_all()[i])
            else:
                i += 1
        self._undo_service.add_operation(cascaded_operation)

    # This function updates an assignment's info
    def update_assignment(self, assignmentID, description, deadline):
        new_assignment = Assignment(assignmentID, description, deadline)
        self._valid_assignment.validate_assignment(new_assignment)
        assignment = self.get_assignment_by_id(assignmentID)
        self._assignments_repo.update(assignment, new_assignment)

        undo = FunctionCall(self._assignments_repo.update, new_assignment, assignment)
        redo = FunctionCall(self._assignments_repo.update, assignment, new_assignment)
        self._undo_service.add_operation(Operation(undo, redo))


class ServiceGrades:

    def __init__(self, undo_service, students_repo, assignments_repo, grade_repo, valid_grade):
        self._undo_service = undo_service
        self._students_repo = students_repo
        self._assignments_repo = assignments_repo
        self._grade_repo = grade_repo
        self._valid_grade = valid_grade

    # This function adds a new grade to the repository
    # parameters: assignmentID, studentID, grade
    def add_grade(self, assignmentID, studentID, grade):
        grade = Grade(studentID, assignmentID, grade)
        self._valid_grade.validate_grade(grade)
        self._grade_repo.add(grade)

    # This function searches for a student in the student repository by it's id
    # parameters: studentID
    def get_student_by_id(self, studentID):
        key = Student(studentID, None, None)
        return self._students_repo.search(key)

    # This function searches for an assignment in the assignment reposiroty by it's id
    # parameters: assignmentId
    def get_assignment_by_id(self, assignmentID):
        key = Assignment(assignmentID, None, None)
        return self._assignments_repo.search(key)

    # This function returns a list with all the grades objects
    def get_all_grades(self):
        return self._grade_repo.get_all()


    # This fuunction assigns an assignment to a student
    # parameters: studentID, assignmentID
    def assign_assignment_to_student(self, studentID, assignmentID):
        self.add_grade(studentID, assignmentID, 0)

        undo = FunctionCall(self._grade_repo.delete, Grade(assignmentID, studentID, 0))
        redo = FunctionCall(self.add_grade, studentID, assignmentID, 0)

        self._undo_service.add_operation(Operation(undo, redo))


    def delete_by_group(self, group, assignmentID, added_grades):
        i = 0
        while i < len(self._grade_repo.get_all()):
            studentID = self._grade_repo.get_all()[i].get_student_id()
            student = self.get_student_by_id(studentID)
            if student.get_group() == group and self._grade_repo.get_all()[i].get_assignment_id() == assignmentID and self._grade_repo.get_all()[i] in added_grades:
                self._grade_repo.delete(self._grade_repo.get_all()[i])
            else:
                i += 1




    # This function assigns an assignmnet to a group
    # parameters: group, assignmentID
    def assign_assignment_to_group(self, group, assignmentID, stud_service):
        stud_repo = stud_service.get_students()
        added_grades = []
        for student in stud_repo:
            if student.get_group() == group:
                grade = Grade(student.get_student_id(), assignmentID, 0)
                if grade not in self._grade_repo.get_all():
                    self._grade_repo.add(grade)
                    added_grades.append(grade)

        undo = FunctionCall(self.delete_by_group, group, assignmentID, added_grades)
        redo = FunctionCall(self.assign_assignment_to_group, group, assignmentID, stud_service)
        self._undo_service.add_operation(Operation(undo, redo))

    # This function gets a grade by the studentID and assignmentID
    # parameters: studentID, assignmentID
    def get_assignment_by_IDs(self, studentID, assignmentID):
        key = Grade(studentID, assignmentID, None)
        return self._grade_repo.search(key)

    # This function updates the grade of the grade object
    # parameters: studentID, assignmentID, grade
    def update_grade(self, studentID, assignmentID, grade):
        new_garde = Grade(studentID, assignmentID, grade)
        self._valid_grade.validate_grade(new_garde)
        found_grade = self.get_assignment_by_IDs(studentID, assignmentID)

        if found_grade.get_grade() != 0:
            raise Exception("grade already set!")

        self._grade_repo.update(found_grade, new_garde)
        undo = FunctionCall(self._grade_repo.update, new_garde, found_grade)
        redo = FunctionCall(self._grade_repo.update, found_grade, new_garde)
        self._undo_service.add_operation(Operation(undo, redo))



    # This function returns a list with the assignments that are graded for a given studentID
    # parameters: studentID
    def get_graded(self, studentID):
        graded_assignments = []
        for grade in self.get_all_grades():
            if grade.get_student_id() == studentID and grade.get_grade() != 0:
                graded_assignments.append(grade.get_assignment_id())

        return graded_assignments

    # This function returns a list with the assignments that are ungraded for a given studentID
    # parameters: studentID
    def get_ungraded(self, studentID):
        ungraded_assignments = []
        for grade in self.get_all_grades():
            if grade.get_student_id() == studentID and grade.get_grade() == 0:
                ungraded_assignments.append(grade.get_assignment_id())

        return ungraded_assignments

    def get_students_by_assignment(self, assignmentID):
        list_grades = []
        for grade in self.get_all_grades():
            if grade.get_assignment_id() == assignmentID:
                list_grades.append(grade)

        list_grades = sorted(list_grades, key=lambda elem: elem._grade)

        '''       
        for i in range (len(list_grades)-1):
            for j in range(i+1, len(list_grades)):
                if list_grades[i].get_grade < list_grades[j].get_grade:
                    list_grades[i], list_grades[j] = list_grades[j], list_grades[i]
        '''

        return list_grades

    def compare_dates(self, assignmentID):
        assignment = self.get_assignment_by_id(assignmentID)
        date1 = assignment.get_deadline()
        date2 = datetime.now()
        if (date1.year < date2.year) or (date1.year == date2.year and date1.month < date2.month) or (
                date1.year == date2.year and date1.month == date2.month and date1.day < date2.day):
            return False
        else:
            return True

    def dead_line_passed(self):
        stud_list = []
        for grade in self.get_all_grades():
            if grade.get_grade() == 0:
                if self.compare_dates(grade.get_assignment_id()) == False and [grade.get_student_id(),
                                                                               grade.get_assignment_id()] not in stud_list:
                    stud_list.append([grade.get_student_id(), grade.get_assignment_id()])

        return stud_list

    def get_graded_grades(self):
        graded = []
        for grade in self.get_all_grades():
            if grade.get_grade() != 0:
                graded.append(grade)

        return graded

    def avg_grades(self, studentID):
        summ = 0
        no = 0
        for grade in self.get_graded_grades():
            if grade.get_student_id() == studentID:
                summ += grade.get_grade()
                no += 1

        return summ / no

    def best_students(self):
        stud_list = []
        for grade in self.get_graded_grades():
            if [grade.get_student_id(), self.avg_grades(grade.get_student_id())] not in stud_list:
                stud_list.append([grade.get_student_id(), self.avg_grades(grade.get_student_id())])

        stud_list = sorted(stud_list, key=lambda elem: elem[1], reverse=True)

        return stud_list


class SeviceUndo:
    def __init__(self):
        self._undo_history = []
        self._redo_history = []
        self._during_undo = False

    def add_operation(self, operation):
        if self._during_undo == False:
            self._undo_history.append(operation)
            self._redo_history.clear()

    def undo(self):
        if len(self._undo_history) == 0:
            raise Exception("no more undos!")

        self._during_undo = True
        operation = self._undo_history.pop()
        operation.undo()
        self._redo_history.append(operation)
        self._during_undo = False

    def redo(self):
        if len(self._redo_history) == 0:
            raise Exception("no more redos!")

        self._during_undo = True
        operation = self._redo_history.pop()
        operation.redo()
        self._undo_history.append(operation)
        self._during_undo = False

