#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import importlib
import os
import sys
# from yolox_paddle import exp

def get_exp_by_file(exp_file):
    try:
        sys.path.append(os.path.dirname(exp_file))  # 加入文件路径
        current_exp = importlib.import_module(os.path.basename(exp_file).split(".")[0])
        exp = current_exp.Exp()
    except Exception:
        raise ImportError("{} doesn't contains class named 'Exp'".format(exp_file))
    return exp

def get_exp_by_name(exp_name):
    import yolox_paddle
    yolox_path = os.path.dirname(os.path.dirname(yolox_paddle.__file__))  # 模块路径
    filedict = {
        "yolox-s": "yolox_s.py",
        "yolox-m": "yolox_m.py",
        "yolox-l": "yolox_l.py",
        "yolox-x": "yolox_x.py",
        "yolox-tiny": "yolox_tiny.py",
        "yolox-nano": "nano.py",
        "yolov3": "yolov3.py",
    }
    filename = filedict[exp_name]   # 对应文件名
    exp_path = os.path.join(yolox_path, "exps", "default", filename) # 文件名路径
    return get_exp_by_file(exp_path)
    

def get_exp(exp_file, exp_name):
    """
    由file或者name获取exp对象，优先使用exp_file
    Args:
        exp_file (str): file path of experiment.
        exp_name (str): name of experiment. "yolo-s",
    """
    assert (
        exp_file is not None or exp_name is not None
    ), "plz provide exp file or exp name." # 检查exp file 和 exp name不能同时为空
    if exp_file is not None:
        return get_exp_by_file(exp_file)
    else:
        return get_exp_by_name(exp_name)