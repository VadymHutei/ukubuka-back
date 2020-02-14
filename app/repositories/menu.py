from core import Repository
from core.sql_query_builder import SelectQuery


class MenuRepo(Repository):

    def getMenus(self, params):
        query = SelectQuery()

        query.fields(
            'mi.id',
            'mi.parent',
            'mi.link',
            'mi.order',
            'mi.added',
            'mi.is_active',
            'mit.name',
        )

        query.table(('menu_items', 'mi'))

        if 'is_active' in params:
            query.where(('mi.is_active', '=', params['is_active']))

        if 'language' in params:
            query.leftJoin(
                ('menu_items_text', 'mit'),
                ('mit.item_id', '=', 'mi.id')
            )
            query.where(('mit.language', '=', params['language']))

        if 'order' in params:
            query.order(params['order'])

        query_string = query.render()
        print(query_string)
        connection = self._getConnection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(query_string)
                categories_result = cursor.fetchall()
                return categories_result
        finally:
            connection.close()
