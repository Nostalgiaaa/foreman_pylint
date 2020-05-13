from .func_name_rule import rule as func_rule
from .orm_rule import rule as orm_rule
from flint import rule_reg_func


# 此处注册所有生成的checker
def register(linter):
    rule_reg_func([func_rule, orm_rule], linter)
