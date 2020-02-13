class SQLQuery():

    _JOIN_TYPES = ('LEFT', 'RIGHT', 'INNER')
    _ORDER = ('ASC', 'DESC')

    def __init__(self):
        self._query = None
        self._query_parts = []

    def _field_handle(self, field):
        if type(field) is str:
            return self._quote(field)
        if type(field) is tuple and len(field) == 2:
            return f'{self._quote(field[0])} AS {self._quote(field[1])}'
        return ''

    def _table_handle(self, table):
        if type(table) is str:
            return self._quote(table)
        if type(table) is tuple and len(table) == 2:
            return f'{self._quote(table[0])} AS {self._quote(table[1])}'
        return ''

    def _join_condition_handle(self, cond):
        if type(cond) is str:
            return cond
        if type(cond) is tuple:
            if len(cond) == 2:
                return f'{self._quote(cond[0])} {cond[1]}'
            if len(cond) == 3:
                return f'{self._quote(cond[0])} {cond[1]} {self._quote(cond[2])}'
        return ''

    def _where_condition_handle(self, cond):
        if type(cond) is str:
            return cond
        if type(cond) is tuple:
            if len(cond) == 2:
                return f'{self._quote(cond[0])} {cond[1]}'
            if len(cond) == 3:
                if type(cond[2]) is str:
                    val = f'\'{cond[2]}\''
                elif type(cond[2]) is int:
                    val = str(cond[2])
                else:
                    val = str(cond[2])
                return f'{self._quote(cond[0])} {cond[1]} {val}'
        return ''

    def _quote(self, string):
        return '.'.join(f'`{word}`'
            for word in map(
                lambda x: x.strip('`'),
                string.split('.')
            )
        )
