from core import Repository
from core.sql_query_builder import SelectQuery


class CategoryRepo(Repository):

    def getCategories(self, params):
        query = SelectQuery()
        query.fields(
            'c.`id`',
            'c.`parent`',
            'c.`order`',
            'c.`added`',
            'c.`is_active`',
            'ct.`name`'
        ),
        query.table(('`categories`', 'c'))
        language = params.get('language')
        if language:
            query.leftJoin(
                ('`categories_text`', 'ct'),
                'ct.`category_id` = c.`id`'
            )
            query.where('ct.`language` = %s')
        query_string = query.render()
        connection = self._getConnection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(query_string, params['language'])
                categories_result = cursor.fetchall()
                return categories_result
        finally:
            connection.close()
