from .checker import CheckerFactory
from .checker import ImplementsType
from .rule import Rule
from .msgs import Msg
from typing import List

name = "flint"


def rule_bind_msg(r: Rule, msg: Msg):
    r.bind_msg(msg.get_msg())


def rule_reg_func(rules: List[Rule], linter, options=()):
    for r in rules:
        _checker = CheckerFactory.init_checker(name=r.name, priority=r.priority, msgs=r.msg, options=options,
                                               funcs=r.funcs,
                                               implements_type=ImplementsType.astroid_implements)
        linter.register_checker(_checker(linter))
