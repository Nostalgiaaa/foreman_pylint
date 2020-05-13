from functools import wraps


class Rule(object):
    def __init__(self, *, name: str, priority: int):
        """
        :param name: 全局唯一名称
        :param priority: 优先级
        """
        self._name = name
        self._priority = priority
        self._funcs = []
        self._msg = {}

    def _add_func(self, func):
        self._funcs.append(func)

    @property
    def funcs(self):
        return self._funcs

    @property
    def name(self):
        return self._name

    @property
    def priority(self):
        return self._priority

    def bind_msg(self, msg):
        self._msg.update(msg.get_msg())

    @property
    def msg(self):
        return self._msg

    def bind_def(self):
        def decorate(func):
            self._add_func(func=func)

            @wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            return wrapper

        return decorate
