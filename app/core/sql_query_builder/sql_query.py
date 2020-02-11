class SQLQuery():

    _query = []
    _fields = []
    _from = None
    _join = []
    _where = []

    _JOIN_TYPES = ('LEFT', 'RIGHT', 'INNER')

    def _table_handler(self, table):
        if type(table) == str:
            return table
        if type(table) == tuple:
            result = table[0]
            if len(table) > 1:
                result += f' AS {table[1]}'
            return result
