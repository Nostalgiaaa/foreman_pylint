def a():
    pass


def get_user_name_api():
    pass


# 不显示自定义检查
def t():  # pylint: disable=W0001
    pass


def raw_sql(sql):
    return sql


def get_name():
    raw_sql()


def get_user_by_id_api(u_id):
    raw_sql("select id from user where id = {0}".format(u_id))
    _tmp = []
