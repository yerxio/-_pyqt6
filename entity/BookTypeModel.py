"""
图书类别实体类
"""

class BookType:
    # 编号 主键ID
    id = None
    # 图书类别名称
    bookTypeName = None
    # 图书类别描述
    bookTypeDesc = None

    def __init__(self, bookTypeName, bookTypeDesc):
        self.bookTypeName = bookTypeName
        self.bookTypeDesc = bookTypeDesc