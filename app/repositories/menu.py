import pymysql

from core import Repository


class MenuRepo(Repository):

    def _separateMenuItems(self, id_, items) -> list:
        menu_items: list = []
        step_counter: int = -1
        parents: list = [id_]
        while step_counter != 0:
            step_counter = 0
            for item in items:
                if item['parent'] in parents:
                    menu_items.append(item)
                    parents.append(item['id'])
                    items.remove(item)
                    step_counter += 1
        return menu_items

    def getMenuByID(self, id_, **params) -> list:
        db_connection_param = {
            'host': 'localhost',
            'user': 'root',
            'password': 'root',
            'db': 'ukubuka',
            'charset': 'utf8mb4',
            'cursorclass': pymysql.cursors.DictCursor
        }
        connection = pymysql.connect(**db_connection_param)
        menu_query = """
            SELECT
                `id`,
                `item_id`,
                `alias`
            FROM `ku_menus`
            WHERE `id` = %s
        """
        items_query = """
            SELECT
                `id`,
                `parent`,
                `link`,
                `order`,
                `added`,
                `is_active`
            FROM `ku_menu_items`
        """
        try:
            with connection.cursor() as cursor:
                cursor.execute(menu_query, (id_,))
                menu_result = cursor.fetchone()
                cursor.execute(items_query)
                items_result = cursor.fetchall()
        finally:
            connection.close()
        args = [menu_result['item_id'], items_result]
        menu_items = self._separateMenuItems(*args)
        menu_result['items'] = menu_items
        return menu_result

    def getMenuByAlias(self, alias, **params) -> list:
        return []
