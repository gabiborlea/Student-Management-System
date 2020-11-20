from Infrastracture.repo import Repository, RepoError

class TextRepository(Repository):
    def __init__(self, file_name, elem_create, init_list):
        super().__init__(init_list)
        self._file_name = file_name
        self._elem_create = elem_create
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
            for element in self.get_all():
                file.write(str(element)+"\n")
        except IOError:
            raise  RepoError("Error saving file")
        finally:
            file.close()

    def _load_file(self):
        file = open(self._file_name, "r")
        if file.read() != "":
            try:
                file = open(self._file_name, "r")
                line = file.readline().strip()
                while line != "":
                    params = line.split()
                    elem = self._elem_create(params[0], params[1], params[2])
                    Repository.add(self, elem)
                    line = file.readline().strip()
            except IOError:
                raise RepoError("Error saving file")
            finally:
                file.close()

