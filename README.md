# foreman pylint

快速开发pylint插件，来实现自定义的公司或个人代码规范

## 依赖
```bash
pip install pylint==2.4.4
```

## 快速使用
```bash
git clone https://github.com/Nostalgiaaa/foreman_pylint.git
```

创建rule（参考  examples/func_name_rule.py, orm_rule.py）
```python
from flint import Rule
from flint import Msg

# 定义规则的名称以及优先级
rule = Rule(name="func_name_rule", priority=-1)
msg = Msg()
# 创建报错信息
msg.add_msg(error_code="W0001", display="函数不可以使用过短的名称", symbol="func_name_too_short")
rule.bind_msg(msg)

# 绑定visit函数
@rule.bind_def()
def visit_functiondef(self, node):
    if len(node.name) == 1:
        self.add_message(
            'func_name_too_short', node=node
        )
```

注册 rule （参考 examples/\_\_init__.py）
```
from .func_name_rule import rule as func_rule
from .orm_rule import rule as orm_rule
from flint import rule_reg_func


# 此处注册所有生成的checker
def register(linter):
    rule_reg_func([func_rule, orm_rule], linter)
```

***⚠️注意必须把 examples 路径加到 PYTHONPATH 中⚠️***


使用命令：
```bash
pylint  --load-plugins examples examples/code.py
```

结果:
```bash
pylint  --load-plugins examples examples/code.py
************* Module examples.code
examples/code.py:1:0: C0114: Missing module docstring (missing-module-docstring)
examples/code.py:1:0: C0103: Function name "a" doesn't conform to snake_case naming style (invalid-name)
examples/code.py:1:0: C0116: Missing function or method docstring (missing-function-docstring)
examples/code.py:1:0: W0001: 函数不可以使用过短的名称 (func_name_too_short)
examples/code.py:1:0: W0002: demo.code文件中统一命名def xxx_api() (func_name_xxx_api)
examples/code.py:5:0: C0116: Missing function or method docstring (missing-function-docstring)
examples/code.py:10:0: C0103: Function name "t" doesn't conform to snake_case naming style (invalid-name)
examples/code.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
examples/code.py:10:0: W0002: demo.code文件中统一命名def xxx_api() (func_name_xxx_api)
examples/code.py:14:0: C0116: Missing function or method docstring (missing-function-docstring)
examples/code.py:14:0: W0002: demo.code文件中统一命名def xxx_api() (func_name_xxx_api)
examples/code.py:18:0: C0116: Missing function or method docstring (missing-function-docstring)
examples/code.py:18:0: W0002: demo.code文件中统一命名def xxx_api() (func_name_xxx_api)
examples/code.py:19:4: E1120: No value for argument 'sql' in function call (no-value-for-parameter)
examples/code.py:19:4: W0011: raw_sql函数不可以随处调用 (raw_sql_cant_use)
examples/code.py:22:0: C0116: Missing function or method docstring (missing-function-docstring)
examples/code.py:23:4: W0011: raw_sql函数不可以随处调用 (raw_sql_cant_use)
examples/code.py:23:4: W0012: sql拼接不可以使用format函数 (sql_cant_use_format)
examples/code.py:24:4: W0003: 不可以声明_tmp变量 (assign_bad_name)

------------------------------------
Your code has been rated at -7.69/10

```
## 开发插件细节
基于pylint开发

msg定义:
文档 [pylint](http://pylint.pycqa.org/en/latest/user_guide/message-control.html)
只能 C/R/W/E/F 开头，后四位为数字，不可重复

visit函数：
参考 [node](https://greentreesnakes.readthedocs.io/en/latest/nodes.html)
其中展示了所有的节点类型，在访问每个节点时，会调用 visit_xxx 函数。

想要对调用进行检查，首先查询文档 [node](https://greentreesnakes.readthedocs.io/en/latest/nodes.html#Call)，例如函数调用
```
>>> parseprint("func(a, b=c, *d, **e)") # Python 3.4
Module(body=[
    Expr(value=Call(func=Name(id='func', ctx=Load()),
                    args=[Name(id='a', ctx=Load())],
                    keywords=[keyword(arg='b', value=Name(id='c', ctx=Load()))],
                    starargs=Name(id='d', ctx=Load()),     # gone in 3.5
                    kwargs=Name(id='e', ctx=Load()))),     # gone in 3.5
  ])

>>> parseprint("func(a, b=c, *d, **e)") # Python 3.5
Module(body=[
    Expr(value=Call(func=Name(id='func', ctx=Load()),
         args=[
                Name(id='a', ctx=Load()),
                Starred(value=Name(id='d', ctx=Load()), ctx=Load()) # new in 3.5
             ],
         keywords=[
                keyword(arg='b', value=Name(id='c', ctx=Load())),
                keyword(arg=None, value=Name(id='e', ctx=Load()))   # new in 3.5
             ]))
    ])
```
找到对应的类型，定义visit_call即可访问该节点。具体使用可以看 examples

## 搭配工具
[pre-commit](https://pre-commit.com/) 通过 pre-commit 每次commit都按照公司代码规范检查

[travis-ci](https://travis-ci.org/) 集成到ci中，减少review工作量。

