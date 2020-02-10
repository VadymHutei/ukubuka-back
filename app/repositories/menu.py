from core import Repository


class MenuRepo(Repository):

    def _separateMenuItems(self, id_, items) -> list:
        menu_items = []
        step_counter = -1
        parents = [id_]
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
        connection = self._getConnection()
        try:
            with connection.cursor() as cursor:
                menu_query = """
                    SELECT
                        `id`,
                        `item_id`,
                        `alias`
                    FROM `menus`
                    WHERE `id` = %s
                """
                items_query = """
                    SELECT
                        mi.`id`,
                        mi.`parent`,
                        mi.`link`,
                        mi.`order`,
                        mi.`added`,
                        mi.`is_active`,
                        mit.`name`
                    FROM `menu_items` mi
                    LEFT JOIN `menu_items_text` mit
                        ON mit.`item_id` = mi.`id`
                        AND mit.`language` = %s
                """
                cursor.execute(menu_query, (id_,))
                menu_result = cursor.fetchone()
                cursor.execute(items_query, (params['language'],))
                items_result = cursor.fetchall()
        finally:
            connection.close()
        args = [menu_result['item_id'], items_result]
        menu_result['items'] = self._separateMenuItems(*args)
        return menu_result

    def getMenuByAlias(self, alias, **params) -> list:
        connection = self._getConnection()
        try:
            with connection.cursor() as cursor:
                menu_query = """
                    SELECT
                        `id`,
                        `item_id`,
                        `alias`
                    FROM `menus`
                    WHERE `alias` = %s
                """
                items_query = """
                    SELECT
                        mi.`id`,
                        mi.`parent`,
                        mi.`link`,
                        mi.`order`,
                        mi.`added`,
                        mi.`is_active`,
                        mit.`name`
                    FROM `menu_items` mi
                    LEFT JOIN `menu_items_text` mit
                        ON mit.`item_id` = mi.`id`
                        AND mit.`language` = %s
                """
                cursor.execute(menu_query, (alias,))
                menu_result = cursor.fetchone()
                cursor.execute(items_query, (params['language'],))
                items_result = cursor.fetchall()
        finally:
            connection.close()
        args = [menu_result['item_id'], items_result]
        menu_result['items'] = self._separateMenuItems(*args)
        return menu_result
