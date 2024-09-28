"""
图书类别数据访问对象
"""
from entity.BookTypeModel import BookType
from util import dbUtil


def add(bookType:BookType):
    """
    图书类别添加
    :param bookType: 图书类别实体
    :return: 返回执行的条数
    """
    con = None
    try:
        con = dbUtil.getCon()
        cursor = con.cursor()
        cursor.execute(f"insert into t_booktype values(null, '{bookType.bookTypeName}', '{bookType.bookTypeDesc}')")
        return cursor.rowcount
    except Exception as e:
        con.rollback()
        print(e)
        return None
    finally:
        dbUtil.closeCon(con)

def list(s_bookTypeName:str):
    """
    根据条件查询或搜索图书类别信息
    :param s_bookTypeName: 图书类别名称
    :return: 返回查询的图书类别信息集合 ->> list
    """
    con = None
    try:
        con = dbUtil.getCon()
        cursor = con.cursor()
        sql = "select * from t_booktype where 1=1"
        if s_bookTypeName.strip() != '':
            sql += " and bookTypeName like + '%" + s_bookTypeName + "%'"
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return None
    finally:
        dbUtil.closeCon(con)