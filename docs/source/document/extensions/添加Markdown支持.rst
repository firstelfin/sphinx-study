Markdown文件支持设置
=======================

1、安装Markdown解析器MyST-Parser
-------------------------------------

.. code-block::

    pip install --upgrade myst-parser


2、添加解析器到配置文件config的extensions列表
------------------------------------------------

.. code-block::

    extensions = ["myst_parser"]


3、设在源文件后缀映射
------------------------

.. code-block::

    source_suffix = {
        ".rst": "restructuredtext",
        ".txt": "markdown",
        ".md": "markdown",
    }


4、添加非标准Markdown语法
---------------------------

可以参考 `syntax-optional <https://myst-parser.readthedocs.io/en/latest/using/syntax-optional.html>`_

