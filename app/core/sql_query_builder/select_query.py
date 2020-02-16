from core.sql_query_builder import SQLQuery


class SelectQuery(SQLQuery):

    def __init__(self):
        super().__init__()

        self._fields = []
        self._from = None
        self._join = []
        self._where = []
        self._group = []
        self._order = []
        self._limit = None

        self._query_parts.append('SELECT')

    def fields(self, *fields):
        for field in fields:
            self._fields.append(self._field_handle(field))

    def table(self, table):
        self._from = self._table_handle(table)

    def leftJoin(self, table, condition):
        self._join.append((
            'LEFT',
            self._table_handle(table),
            self._join_condition_handle(condition)
        ))

    def where(self, condition):
        self._where.append(self._where_condition_handle(condition))

    def whereInSelect(self, field, subquery):
        self._where.append(f'{self._field_handle(field)} IN ({subquery.render()})')

    def group(self, field):
        self._group.append(self._field_handle(field))

    def order(self, order):
        self._order.append((
            self._field_handle('order'),
            order.upper()
        ))

    def orderBy(self, order_by):
        for order in order_by:
            self._order.append((
                self._field_handle(order[0]),
                order[1].upper()
            ))

    def limit(self, limit):
        self._limit = limit

    def _buildFields(self):
        if self._fields:
            self._query_parts.append(', '.join(self._fields))
        else:
            self._query_parts.append('*')

    def _buildFrom(self):
        self._query_parts.append('FROM')
        self._query_parts.append(self._from)

    def _buildJoin(self):
        if self._join:
            for join in self._join:
                if join[0] not in self._JOIN_TYPES:
                    continue
                self._query_parts.append(join[0] + ' JOIN')
                self._query_parts.append(join[1])
                self._query_parts.append('ON')
                self._query_parts.append(join[2])

    def _buildWhere(self):
        if self._where:
            where_conditions = ' AND '.join(self._where)
            self._query_parts.append('WHERE')
            self._query_parts.append(where_conditions)

    def _buildGroupBy(self):
        if self._group:
            self._query_parts.append('GROUP BY')
            self._query_parts.append(', '.join(self._group))

    def _buildOrderBy(self):
        if self._order:
            self._query_parts.append('ORDER BY')
            order_fields = [f'{order[0]} {order[1]}' for order in self._order]
            self._query_parts.append(', '.join(order_fields))

    def _buildLimit(self):
        if self._limit:
            self._query_parts.append('LIMIT')
            self._query_parts.append(str(self._limit))

    def _build(self):
        self._query = ' '.join(self._query_parts)

    def render(self):
        self._buildFields()
        self._buildFrom()
        self._buildJoin()
        self._buildWhere()
        self._buildGroupBy()
        self._buildOrderBy()
        self._buildLimit()
        self._build()

        return self._query
