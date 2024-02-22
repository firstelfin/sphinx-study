#!/usr/bin/env python3
# encoding: utf-8
# @author: firstelfin
# @time: 2024/02/22 10:50:22

import os
import math
import time
from pydantic import BaseModel
from typing import Union, List, Dict, Optional


class SuppressParam(BaseModel):
    """

    :param reportNum:       默认None, 上次异常上报后, 识别到的异常数量
    :type reportNum:        [int, None]
    :param suppressWinSize: 默认4     设置的异常周期, 单位小时
    :type suppressWinSize:  int
    :param lastTime:        默认0.0   上次异常上报请求的时间戳, 单位秒
    :type lastTime:         float
    :param maxEpoch:        默认2     最大重置周期
    :type maxEpoch:         int

    参数用于处理：

    :math:

        `State(k,W,T_{s},T,\sigma) = I(k \times \Delta_{W} + \sigma \times (T_{s} + W - T) - 1 + \delta)`
    
    """

    reportNum:  Optional[int] = None      # 上次异常上报后, 识别到的异常数量
    suppressWinSize:    float = 4         # 设置的异常周期, 单位小时
    lastTime: Optional[float] = .0        # 上次异常上报请求的时间戳, 单位秒
    maxEpoch:   Optional[int] = 2         # 最大重置周期


def post_suppress(suppress: SuppressParam, delta: float = 0.95, cf=12, percent=None):
    """
    :param suppress: 抑制参数对象
    :type suppress: SuppressParam
    :param delta: 显著性指标
    :type delta: float
    :param cf: 每小时请求频数
    :type cf: int
    :param percent: 期望抑制次数 / 窗口总请求数, 默认35%[None]的请求有异常就上报
    :type percent: [float, None]

    :return: 布尔值或者0/1
    :rtype: [bool, int]
    """

    if percent is None:
        percent = float(os.getenv("PERCENT", 0.35))
    
    assert suppress.maxEpoch > 1, f"SuppressParam Error: {suppress.maxEpoch=}, excepted > 1."
    assert suppress.suppressWinSize > 0, f"SuppressParam Error: {suppress.suppressWinSize=}, excepted > 0."

    gain = 1 / (cf * suppress.suppressWinSize * percent + 0.001)  # 评分增益

    score = (suppress.reportNum * gain + 
             math.floor((time.time() - suppress.lastTime) / (suppress.suppressWinSize * 3600)) / suppress.maxEpoch - 
             delta)

    return 1 if score > 0 else 0
