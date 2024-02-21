
python项目源码文档生成
==========================


1、准备好python项目
--------------------------

我们在这里定制了sphinx_study库, 注意这里python包都要有 **__init__.py** 文件, 这样自动化才能有效链接。


2、简单尝试自动化文档
--------------------------

编辑 conf.py

.. code-block:: python

    import os
    import sys
    sys.path.insert(0, os.path.abspath('sphinx_study所在路径'))

我们使用官方自带的扩展

.. code-block:: shell

    pip install --upgrade myst-parser
    sphinx-apidoc -o source/sphinx_study ../sphinx_study/
    

**参考链接**
    1. `sphinx自动化文档 <https://blog.csdn.net/lly1122334/article/details/103970663>`_
    2. `apidoc <https://github.com/sphinx-contrib/apidoc>`_
    3. `autodoc <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#module-sphinx.ext.autodoc>`_
