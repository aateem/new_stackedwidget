#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

DATABASE_NAME = 'data_files/qtrainer.db'

def singleton(cls):
    def instance(data_base_name):
        if not '__instance' in cls.__dict__:
            cls.__dict__['instance'] = cls(data_base_name)
        return cls.__dict__['instance']
    return instance

@singleton
class DataBaseProcess:

    def __init__(self, data_base_name):
        self.conn = lite.connect(data_base_name)
        self.cur = self.conn.cursor()
            
        if not self.conn:
            raise Exception("Error: connection faild!")

    def getCurrentUserId(self, user_login, user_pass):
        self.cur.execute("select userid from user_login where user_login=? and user_pass=?", (user_login, user_pass))
        self.current_user_id = self.cur.fetchone()

        return self.current_user_id

    def closeConnection(self):
        if self.conn:
            self.conn.close()


dbp = DataBaseProcess(DATABASE_NAME)







