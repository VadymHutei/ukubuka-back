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

        if 'is_active' in params:
            query.where(f'c.`is_active` = "{params["is_active"]}"')

        if 'parent' in params:
            if params['parent'] is None:
                query.where('c.`parent` IS NULL')
            else:
                query.where(f'c.`parent` = {params["parent"]}')

        if 'language' in params:
            query.leftJoin(
                ('`categories_text`', 'ct'),
                'ct.`category_id` = c.`id`'
            )
            query.where(f'ct.`language` = "{params["language"]}"')

        query_string = query.render()
        connection = self._getConnection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(query_string)
                categories_result = cursor.fetchall()
                return categories_result
        finally:
            connection.close()
