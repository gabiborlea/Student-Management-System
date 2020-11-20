class FunctionCall:
    def __init__(self, function, *parameters):
        self._function = function
        self._parameters = parameters

    def call(self):
        self._function(*self._parameters)

class Operation:
    def __init__(self, undo_operation, redo_operation):
        self._undo = undo_operation
        self._redo = redo_operation

    def undo(self):
        self._undo.call()

    def redo(self):
        self._redo.call()

class CascadedOperation:
    def __init__(self):
        self._list = []

    def record_operation(self, operation):
        self._list.append(operation)

    def undo(self):
        for operation in self._list:
            operation.undo()

    def redo(self):
        for operation in self._list:
            operation.redo()
