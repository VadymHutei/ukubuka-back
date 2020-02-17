class SQLQuery():

    _JOIN_TYPES = ('LEFT', 'RIGHT', 'INNER')

    def __init__(self):
        self._query = None
        self._query_parts = []

    def _valueHandle(self, value):
        if type(value) is str:
            return f'\'{value}\''
        elif type(value) is int:
            return str(value)
        else:
            return str(value)

    def _fieldHandle(self, field):
        if type(field) is str:
            return self._quote(field)
        if type(field) is tuple and len(field) == 2:
            return f'{self._quote(field[0])} AS {self._quote(field[1])}'
        return ''

    def _tableHandle(self, table):
        if type(table) is str:
            return self._quote(table)
        if type(table) is tuple and len(table) == 2:
            return f'{self._quote(table[0])} AS {self._quote(table[1])}'
        return ''

    def _joinConditionHandle(self, cond):
        if type(cond) is str:
            return cond
        if type(cond) is tuple:
            if len(cond) == 2:
                return f'{self._quote(cond[0])} {cond[1]}'
            if len(cond) == 3:
                return f'{self._quote(cond[0])} {cond[1]} {self._quote(cond[2])}'
        return ''

    def _whereConditionHandle(self, cond):
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
