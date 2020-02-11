class SQLQuery():

    _JOIN_TYPES = ('LEFT', 'RIGHT', 'INNER')
    _ORDER = ('ASC', 'DESC')

    def __init__(self):
        self._query = None
        self._query_parts = []

    def _table_handler(self, table):
        if type(table) == str:
            return table
        if type(table) == tuple:
            result = table[0]
            if len(table) > 1:
                result += f' AS {table[1]}'
            return result
