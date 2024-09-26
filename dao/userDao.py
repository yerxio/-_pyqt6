"""
用户模块-数据访问对象
"""
from entity.UserModel import User
from util import dbUtil

# 记录当前登录用户
currentUser = None

def login(user: User):
    """
    用户登录判断
    :param user: 用户实体
    :return: 登录成功返回用户信息实体, 登录失败返回None
    """
    try:
        con = dbUtil.getCon()
        cursor = con.cursor()
        # 执行查询
        cursor.execute(f'select * from t_user where `userName` = "{user.username}" and `password` = "{user.password}"')
        return cursor.fetchone()
    except Exception as e:
        con.rollback()
        print(e)
    finally:
        dbUtil.closeCon(con)
        print(cursor.fetchone())