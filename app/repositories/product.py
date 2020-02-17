from core import Repository
from core.sql_query_builder import SelectQuery


class ProductRepo(Repository):

    def getProducts(self, params):
        query = SelectQuery()

        query.fields(
            'p.id',
            'p.category_id',
            'p.model',
            'p.added',
            'p.is_active',
            'pt.name',
            'pt.description',
        )

        query.table(('products', 'p'))

        if 'is_active' in params:
            query.where(('p.is_active', '=', params['is_active']))

        if 'category_id' in params:
            query.whereIn('p.category_id', params['category_id'])

        if 'language' in params:
            query.leftJoin(
                ('products_text', 'pt'),
                ('pt.product_id', '=', 'p.id')
            )
            query.where(('pt.language', '=', params['language']))

        query_string = query.render()
        connection = self._getConnection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(query_string)
                products_result = cursor.fetchall()
                return products_result
        finally:
            connection.close()
