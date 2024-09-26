"""
数据库操作工具类
"""
from pymysql import Connection


def getCon():
    """
     获取数据库连接
    """
    con = Connection(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        database='db_book3',
        autocommit=True # 自动提交
    )
    return con

def closeCon(con: Connection):
    """
    关闭数据库连接
    """
    if con:
        print('关闭数据库连接')
        con.close()


if __name__ == '__main__':
    try:
        con = getCon()
        cursor = con.cursor()
        # 执行查询
        cursor.execute('select * from t_user')
        print(cursor.fetchone())
    except Exception as e:
        print(e)
    finally:
        closeCon(con)