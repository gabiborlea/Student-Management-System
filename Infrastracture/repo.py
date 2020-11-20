class Repository:

    
    def __init__(self, init_list):
        self._list = init_list
    
    #This function returns the number of elements in the repository
    def size(self):
        return len(self._list)
    
    #This function searches for a key object in the repo
    #params: key- the key object
    #output: RepoError if it is not found, the object otherwise
    def search(self, key):
        if key not in self._list:
            raise RepoError("id inexistent\n")
        
        for elem in self._list:
            if elem == key:
                return elem
            
    #This function add a new object to the repo
    #params: elem- the object
    def add(self, elem):
        if elem in self._list:
            raise RepoError("id existent\n")
        self._list.append(elem)
        
    #This function returns the repo
    def get_all(self):
        return self._list

    #This function removes an object from repo
    def delete(self, element):
        self._list.remove(element)
        
    #This function updates an object from repo
    def update(self, element, new_elem):
        elem = self.search(element)
        idx = self._list.index(elem)
        self.delete(elem)
        self._list.insert(idx, new_elem)
        
class RepoError(Exception):
    pass
    
    
    


