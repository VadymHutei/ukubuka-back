from typing import List, Dict, Optional


class SQLQuery():

    _type: Optional[str] = None
    _table_name: Optional[str] = None
    _fields: List[str] = ['*']
    _where: List[str] = []
    _order: Dict[str, str] = {}
    _limit: Optional[int] = None

    def __init__(self) -> None:
        self._where = []
        self._order = {}

    def __repr__(self):
        return self.render()

    def _quote(self, name: str) -> str:
        return '`' + name.strip(' \'"`') + '`'

    def table(self, table_name: str) -> None:
        self._table_name = self._quote(table_name)

    def select(self, *fields: List[str]) -> None:
        self._type = 'select'
        if fields:
            self._fields = ', '.join(map(lambda x: self._quote(x), fields))

    def where(self, condition: str) -> None:
        self._where.append(condition)

    def order(self, field: str, order: str) -> None:
        self._order[self._quote(field)] = order.upper()

    def limit(self, limit: int) -> None:
        self._limit = str(limit)

    def render(self) -> str:
        if self._type == 'select':
            return self._renderSelect()

    def _renderSelect(self) -> str:
        query: List[str] = []
        query.append('SELECT')
        query.append(self._fields)
        query.append('FROM')
        query.append(self._table_name)
        for i, cond in enumerate(self._where):
            query.append('WHERE' if i == 0 else 'AND')
            query.append(cond)
        for order in self._order.items():
            query.append('ORDER BY')
            query.extend(order)
        query.append('LIMIT')
        query.append(self._limit)
        return ' '.join(query) + ';'
