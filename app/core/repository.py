import pymysql

import config


class Repository:

    def __init__(self):
        self._conection_params = config.DB_PARAMS
        self._conection_params['cursorclass'] = pymysql.cursors.DictCursor

    def _getConnection(self):
        return pymysql.connect(**self._conection_params)
