from Infrastracture.repo import Repository, RepoError
import pickle

class BinaryRepository(Repository):
    def __init__(self, file_name, init_list):
        super().__init__(init_list)
        self._file_name = file_name
        self._load_file()

    def add(self, elem):
        Repository.add(self, elem)
        self._save_file()

    def delete(self, elem):
        Repository.delete(self, elem)

        self._save_file()

    def update(self, element, new_elem):
        self._load_file()
        Repository.update(self, element, new_elem)
        self._save_file()


    def _save_file(self):
        try:
            with open(self._file_name, "wb") as pickle_file:
                elem_list = Repository.get_all(self)
                pickle.dump(elem_list, pickle_file)
        except IOError:
            raise RepoError("Error saving file")
        finally:
            pickle_file.close()


    def _load_file(self):

        try:
            with open(self._file_name, "rb") as pickle_file:
                elem_list = pickle.load(pickle_file)
                for elem in elem_list:
                    Repository.add(self, elem)

        except IOError:
            raise RepoError("Error saving file")
        except EOFError:
            pickle_file.close()
        finally:
            pickle_file.close()

