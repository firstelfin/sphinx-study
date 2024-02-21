
python 代码块
==========================

1、简单实现
---------------

.. code-block:: python3
    :linenos:
    :emphasize-lines: 2

    def add_str(a: str, b: str) -> int:
        return int(a) + int(b)


上面的代码块实现有几个关键因素:
    1. 设置代码高量支持，默认是支持python3；
    2. 书写 **.. code-block::** 标识开始代码块；
    3. 标识符号后面要空行表示标识本身的结束；

其他代码的支持可以参考：`usage configuration <https://www.sphinx-doc.org/en/master/usage/index.html>`_ 和 `代码高量与代码块设置 <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-code-block>`_.


2、引用源代码
----------------------

文件引用，点击查看源码可以查看restructuredtext语法。

.. literalinclude:: ../../../../sphinx_study/sphinx_utils/app_func.py

