import json
from Infrastracture.repo import Repository, RepoError

class JsonRepository(Repository):
    def __init__(self, file_name, elem_create, init_list, fields):
        super().__init__(init_list)
        self._file_name = file_name
        self._elem_create = elem_create
        self._fields = fields
        self._load_file()


    def add(self, elem):
        Repository.add(self, elem)
        self._save_file()

    def delete(self, elem):
        Repository.delete(self, elem)
        self._save_file()

    def update(self, element, new_elem):
        Repository.update(self, element, new_elem)
        self._save_file()


    def _save_file(self):
        try:
            file = open(self._file_name, "w")
            file.write('[')
            for element in self.get_all():
                if element is not self.get_all()[0]:
                    file.write(',')
                params = element.tuple_return()
                x = {self._fields[0]: params[0], self._fields[1]: params[1], self._fields[2]: params[2]}
                json.dump(x, file)

            file.write(']')
        except IOError:
            raise  RepoError("Error saving file")
        finally:
            file.close()

    def _load_file(self):
        file = open(self._file_name, "r")
        if file.read() != "":
            file.close()
            file = None

            try:
                with open(self._file_name, "r") as file:
                    elem_list = json.load(file)
                    for elem in elem_list:
                        x = self._elem_create(elem[self._fields[0]], elem[self._fields[1]], elem[self._fields[2]])
                        Repository.add(self, x)
            except IOError:
                raise RepoError("Error saving file")
            finally:
                file.close()

