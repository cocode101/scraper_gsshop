import pymysql
import pandas as pd


class MyInfo:
    def __init__(self):
        # Login Information
        self.host = "127.0.0.1"
        self.dbname = "items"
        self.port = 3306
        self.user_id = "root"
        self.user_pw = "1234"


class MyDb:
    def __init__(self):
        login_info = MyInfo()

        # MySQL Connection
        self.db_conn = pymysql.connect(host=login_info.host,
                                       port=login_info.port,
                                       user=login_info.user_id,
                                       password=login_info.user_pw,
                                       db=login_info.dbname,
                                       charset='utf8')

        # Create Cursor: 커서 오브젝트 가져오기
        # self.cursor = self.db_conn.cursor()
        print("DB Connected")

    def db_select(self, query, *args):
        try:
            with self.db_conn.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
        finally:
            print("selected")

        return result

    def db_execute(self, query):
        try:
            with self.db_conn.cursor() as cursor:
                cursor.execute(query)
                self.db_conn.commit()
        finally:
            print("executed")

    def db_executemany(self, query, args):
        try:
            with self.db_conn.cursor() as cursor:
                cursor.executemany(query, args)
                self.db_conn.commit()
        finally:
            print("executed")

    def __del__(self):
        if self.db_conn.open:
            self.db_conn.close()
            print("DB Close")




