import pymssql as db


class dbconn:
    def __init__(self):
        try:
            self.conn = db.connect(
                server='61.252.138.43',
                user='sa',
                password='kit@)!)',
                database='wm_obs',
                charset='utf8',
                # charset='ISO-8859-1',
                autocommit=True
            )
        except db.Error as err:
            print(f'db connect error : {err}')

    def selectquery(self, strqry):
        try:
            cs = self.conn.cursor()
            cs.execute(strqry)
            result = cs.fetchall()
            return result
        except db.Error as err:
            print(f'db error: {err}')

    def executes(self, strqry):
        try:
            cs = self.conn.cursor()
            cs.execute(strqry)
            self.conn.commit()
        except db.Error as err:
            print(f'db error: {err}')

    def executem(self, strqry, listdata):
        try:
            cs = self.conn.cursor()
            cs.executemany(strqry, listdata)
            self.conn.commit()
        except db.Error as err:
            print(f'db error: {err}')

    def close(self):
        self.conn.close()
