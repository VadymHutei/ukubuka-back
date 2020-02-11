from core.sql_query_builder import SQLQuery


class SelectQuery(SQLQuery):

    def fields(self, *fields):
        self._fields.extend(fields)

    def table(self, table):
        self._from = self._table_handler(table)

    def left_join(self, table, condition):
        self._join.append((
            'left',
            self._table_handler(table),
            condition
        ))

    def where(self, condition):
        self._where.append(condition)

    def render(self):
        self._query.append('SELECT')

        # fields
        if self._fields:
            self._query.append(', '.join(self._fields))
        else:
            self._query.append('*')

        # from
        self._query.append('FROM')
        self._query.append(self._from)

        # join
        if self._join:
            for join in self._join:
                join_type = join[0].upper()
                if join_type not in self._JOIN_TYPES:
                    continue
                self._query.append(join_type + ' JOIN')
                self._query.append(join[1])
                self._query.append('ON')
                self._query.append(join[2])

        # where
        if self._where:
            where_conditions = ' AND '.join(self._where)
            self._query.append('WHERE')
            self._query.append(where_conditions)

        return ' '.join(self._query) + ';'
