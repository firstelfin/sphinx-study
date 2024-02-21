超链接的使用
====================


1、网页链接
---------------------

.. code-block::

    `link text <http url>`_

格式说明:
    1. 单引号加下划线;
    2. 引号内部是显示标题+url, 两者之间使用空格分隔;

或者使用下面的引用形式:

.. code-block::

    This is a paragraph that contains `a link`_.

    .. _a link: https://domain.invalid/


This is a paragraph that contains `URL-NAME`_.

.. _URL-NAME: https://www.baidu.com


2、内链引用
---------------------

我们在上面定义了URL-NAME, 下面就可以直接使用这个标签名

.. code-block::

    .. _my-reference-label:

    Section to cross-reference
    --------------------------

    This is the text of the section.

    It refers to the section itself, see :ref:`my-reference-label`.

.. _TEST-LABEL:

    label title
    -------------------

    **test squence.**



内链引用参考，见 :ref:`text link <TEST-LABEL>`, 注意我们使用的 `:ref:`,与label之间不能有空格!

