from core.sql_query_builder import SQLQuery


class SelectQuery(SQLQuery):

    def fields(self, *fields):
        self._fields.extend(fields)

    def table(self, table):
        self._from = self._table_handler(table)

    def left_join(self, table, condition):
        self._join.append((
            'LEFT',
            self._table_handler(table),
            condition
        ))

    def where(self, condition):
        self._where.append(condition)

    def group(self, field):
        self._group.append(field)

    def order(self, field, order='ASC'):
        order = order.upper()
        if order in self._ORDER:
            self._order.append((field, order))

    def limit(self, limit):
        self._limit = limit

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
                if join[0] not in self._JOIN_TYPES:
                    continue
                self._query.append(join[0] + ' JOIN')
                self._query.append(join[1])
                self._query.append('ON')
                self._query.append(join[2])

        # where
        if self._where:
            where_conditions = ' AND '.join(self._where)
            self._query.append('WHERE')
            self._query.append(where_conditions)

        # group by
        if self._group:
            self._query.append('GROUP BY')
            self._query.append(', '.join(self._group))

        # order by
        if self._order:
            self._query.append('ORDER BY')
            order_fields = [' '.join(order) for order in self._order]
            self._query.append(', '.join(order_fields))

        # limit
        if self._limit:
            self._query.append('LIMIT')
            self._query.append(str(self._limit))

        return ' '.join(self._query) + ';'
