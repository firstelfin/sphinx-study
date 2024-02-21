#!/usr/bin/env python3
# encoding: utf-8
# @author: firstelfin
# @time: 2024/02/07 15:40:49

from sphinx_study.sphinx_utils.app_func import DataItem


def main():
    """
    执行主程序

    :return res: int
    
    """
    data_item = DataItem()
    res = data_item.infer("15", "32")
    return res


if __name__ == "__main__":
    main()
