class dbRepository:
    def __init__(self,db, cursor,table, fields, create):
        self._db = db
        self._cursor = cursor
        self._table = table
        self._fields = fields
        self._create = create

    def search(self, key):
        f_key = key.tuple_return()[0]
        s_key = key.tuple_return()[1]
        if type(s_key) == "<class 'int'>":
            sql_select = "SELECT * FROM " + self._table + " WHERE " + self._fields[0] + " = " + str(f_key) + " AND " + self._fields[1] + " = " + str(s_key)
        else:
            sql_select = "SELECT * FROM " + self._table + " WHERE " + self._fields[0] + " = " + str(f_key)

        self._cursor.execute(sql_select)

        result = self._cursor.fetchall()
        result = result[0]
        return self._create(result[0], result[1], result[2])


    def add(self, element):
        sql_add = "INSERT INTO " + self._table + "(" + self._fields[0] + "," + self._fields[1] + "," + self._fields[2] + ")" + "VALUES(%s, %s, %s)"
        element = element.tuple_return()
        self._cursor.execute(sql_add, element)
        self._db.commit()

    def delete(self, element):
        f_key = element.tuple_return()[0]
        s_key = element.tuple_return()[1]
        if type(s_key) == "<class 'int'>":
            sql_delete = "DELETE FROM " + self._table + " WHERE " + self._fields[0] + " = " + str(f_key) + " AND " + self._fields[1] + " = " + str(s_key)
        else:
            sql_delete = "DELETE FROM " + self._table + " WHERE " + self._fields[0] + " = " + str(f_key)

        self._cursor.execute(sql_delete)
        self._db.commit()

    def update(self, element, new_element):
        f_key = element.tuple_return()[0]
        s_key = element.tuple_return()[1]
        field_1 = new_element.tuple_return()[1]
        field_2 = new_element.tuple_return()[2]
        if type(s_key) == "<class 'int'>":
            sql_update = "UPDATE " + self._table + " SET " + self._fields[1] +" = '" + field_1  + "' AND " + self._fields[2] +" = '" + str(field_2) + "' " +"  WHERE " + self._fields[0] + " = " + str(f_key) + " AND " + \
                         self._fields[1] + " = " + str(s_key)
        else:
            sql_update = "UPDATE " + self._table + " SET " + self._fields[1] + " = '" + str(field_1) + "' " + "WHERE " + \
                         self._fields[0] + " = " + str(f_key)
            self._cursor.execute(sql_update)
            self._db.commit()

            sql_update = "UPDATE " + self._table + " SET " + self._fields[2] + " = " + str(field_2) + " WHERE " + \
                         self._fields[0] + " = " + str(f_key)
            self._cursor.execute(sql_update)
            self._db.commit()

    def get_all(self):
        sql_get_all = "SELECT * FROM " + self._table
        self._cursor.execute(sql_get_all)

        list = self._cursor.fetchall()
        result_list = []
        for result in list:
            result_list.append(self._create(result[0], result[1], result[2]))

        return result_list


