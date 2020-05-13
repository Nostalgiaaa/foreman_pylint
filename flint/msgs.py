from .exception import ErrorCodeNotValid


class Msg(object):
    def __init__(self):
        self._msgs = {}

    def get_msg(self):
        return self._msgs

    def add_msg(self, error_code: str, display: str, symbol: str, help_str: str=""):
        """
        添加一条报错信息
        :param error_code: 全局唯一错误码 示例：W0001，首位必须为大写字母C/W/E/F/R
        :param display: 显示给用户的消息
        :param symbol: 消息id
        :param help_str: pylint --help-msg 时显示
        :return: None
        """
        self._check_error_code(error_code)
        self._msgs[error_code] = (display, symbol, help_str)

    @staticmethod
    def _check_error_code(error_code: str):
        if not error_code:
            raise ErrorCodeNotValid("error_code不可以为空")
        if error_code[0] not in ["C", "W", "E", "F", "R"]:
            raise ErrorCodeNotValid("error_code首位必须在大写的 CWEFR 之中")
        if len(error_code) != 5:
            raise ErrorCodeNotValid("error_code长度必须为5")
