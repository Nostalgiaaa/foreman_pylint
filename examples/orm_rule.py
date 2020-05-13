from flint import Rule
from flint import Msg


rule = Rule(name="orm_rule", priority=-1)
msg = Msg()
msg.add_msg(error_code="W0011", display="raw_sql函数不可以随处调用", symbol="raw_sql_cant_use")
msg.add_msg(error_code="W0012", display="sql拼接不可以使用format函数", symbol="sql_cant_use_format")
rule.bind_msg(msg)


@rule.bind_def()
def visit_call(self, node):
    path = self.current_file
    if "examples/code" in path and "raw_sql" in node.as_string():
        self.add_message(
            'raw_sql_cant_use', node=node
        )

    if "raw_sql" in node.as_string():
        if node.args:
            sql = node.args[0]
            if sql.func.attrname == "format":
                self.add_message(
                    'sql_cant_use_format', node=node
                )
