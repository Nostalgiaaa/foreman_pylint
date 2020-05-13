from typing import List, Dict, Any, Optional
from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker


class ImplementsType(object):
    astroid_implements = 0

    @classmethod
    def get_implements(cls, implements_type: int) -> Optional[IAstroidChecker]:
        implements_map = {
            cls.astroid_implements: IAstroidChecker
        }
        return implements_map.get(implements_type, None)


class _BaseChecker(BaseChecker):
    def __init__(self, linter=None):
        super(_BaseChecker, self).__init__(linter)

    @property
    def current_file(self):
        return self.linter.current_file

    @property
    def current_name(self):
        return self.linter.current_name

    # 以下是全部的visit函数

    def visit_raise(self, node):
        ...

    def visit_assignattr(self, node):
        ...

    def visit_importfrom(self, node):
        ...

    def visit_subscript(self, node):
        ...

    def visit_print(self, node):
        ...

    def visit_classdef(self, node):
        ...

    def visit_functiondef(self, node):
        ...

    def visit_listcomp(self, node):
        ...

    def visit_excepthandler(self, node):
        ...

    def visit_repr(self, node):
        ...

    def visit_ifexp(self, node):
        ...

    def visit_binop(self, node):
        ...

    def visit_attribute(self, node):
        ...

    def visit_call(self, node):
        ...

    def visit_if(self, node):
        ...

    def visit_arguments(self, node):
        ...

    def visit_module(self, node):
        ...

    def visit_delattr(self, node):
        ...

    def visit_name(self, node):
        ...


class CheckerFactory(object):
    @staticmethod
    def init_checker(*, name: str, priority: int, msgs: Dict, options: tuple, funcs: List[Any],
                     implements_type: int) -> type:
        func_dict = {i.__name__: i for i in funcs}
        func_dict.update(name=name, __implements__=ImplementsType.get_implements(implements_type), priority=priority,
                         msgs=msgs, options=options)

        checker = type(name, (_BaseChecker,), func_dict)
        return checker
