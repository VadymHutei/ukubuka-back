class SQLQuery():

    _JOIN_TYPES = ('LEFT', 'RIGHT', 'INNER')
    _ORDER = ('ASC', 'DESC')

    def __init__(self):
        self._query = None
        self._query_parts = []

    def _table_handler(self, table):
        return f'{self._quote(table[0])} AS {self._quote(table[1])}' \
            if type(table) is tuple \
            else table

    def _quote(self, string):
        return '.'.join(f'`{word}`'
            for word in map(
                lambda x: x.strip('`'),
                string.split('.')
            )
        )
