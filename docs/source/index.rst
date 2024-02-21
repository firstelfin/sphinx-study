.. sphinx-repo documentation master file, created by
   sphinx-quickstart on Sun Feb 18 18:09:01 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

欢迎使用 sphinx-repo 文档教程!
=======================================

python的Shpinx 项目构建

官网参考: `Sphinx <https://www.sphinx-doc.org/en/master/tutorial/getting-started.html>`_

.. toctree::
   :maxdepth: 2
   :caption: 导航

   document/extensions/extension
   document/python/python
   document/rst语法/res_usage
   sphinx_study/modules



1、快速体验Sphinx项目
-----------------------

1.1 准备python项目
*********************

.. code-block:: shell

   Sphinx_test
   ├── infer.py
   └── sphinx_utils
      └── app_func.py


我们首先构建一个python项目

1.2 安装环境
***************

.. highlight:: pygments.lexers.shell.BashLexer

.. code-block:: shell

   pip install -U sphinx


repo测试sphinx是在一个conda虚拟环境中!

1.3 初始化sphinx
************************

快速创建文档项目

.. code-block:: shell

   sphinx-quickstart docs
   > 独立的源文件和构建目录 (y/n) [n]: y
   > 项目名称: sphinx_repo
   > 作者名称: firstelfin
   > 项目发行版本 []: 1.0.0
   > 项目语种 [en]: zh_CN


.. code-block:: shell

   sphinx-build -M html docs/source/ docs/build/

此时可以在`docs/build/html/index.html`路径下打开超文本！

1.4 主题设置
******************

安装喜欢的主题：`主题列表 <https://sphinx-themes.org/>`_

.. code-block:: shell

   pip install sphinx-rtd-theme


在`docs/source/conf.py`设置：

.. code-block:: python3

   html_theme = 'sphinx-rtd-theme'


1.5 在HTML文档中生效主题
*********************************

.. code-block:: shell

   cd docs
   make html



Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
