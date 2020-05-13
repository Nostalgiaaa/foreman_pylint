from flint import Rule
from flint import Msg


rule = Rule(name="func_name_rule", priority=-1)
msg = Msg()
msg.add_msg(error_code="W0001", display="函数不可以使用过短的名称", symbol="func_name_too_short")
msg.add_msg(error_code="W0002", display="examples.code文件中统一命名def xxx_api()", symbol="func_name_xxx_api")
msg.add_msg(error_code="W0003", display="不可以声明_tmp变量", symbol="assign_bad_name")
rule.bind_msg(msg)


@rule.bind_def()
def visit_functiondef(self, node):
    if len(node.name) == 1:
        self.add_message(
            'func_name_too_short', node=node
        )
    # self.current_file 返回当前文件路径
    path = self.current_file
    if "examples/code" in path and not node.name.endswith("api"):
        self.add_message(
            'func_name_xxx_api', node=node
        )


@rule.bind_def()
def visit_assign(self, node):
    for target in node.targets:
        if target.name == "_tmp":
            self.add_message(
                'assign_bad_name', node=node
            )
