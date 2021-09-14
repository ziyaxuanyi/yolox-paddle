#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import sys
__dir__ = os.path.dirname(os.path.abspath(__file__))
sys.path.append(__dir__)
sys.path.append(os.path.abspath(os.path.join(__dir__, '..')))

import argparse
from loguru import logger   # 日志库，使用可参考https://xercis.blog.csdn.net/article/details/107516039

# from yolox.exp import get_exp
from yolox_paddle.exp.build import get_exp

def make_parser():       # 解析命令行参数
    parser = argparse.ArgumentParser("YOLOX train parser")

    parser.add_argument("-n", "--name", type=str, default="yolox-s", help="model name")  # 定义此次训练的网络结构s,m,l,x,tiny等

    parser.add_argument(   # 定义此次训练的文件，主要是定义网络的结构s,m,l,x,tiny等
        "-f",
        "--exp_file",
        default=None,
        type=str,
        help="plz input your expriment description file",
    )

    return parser

@logger.catch    # 使用装饰器捕获异常
def main(exp, args):
    pass

if __name__ == "__main__":
    args = make_parser().parse_args()
    exp = get_exp(args.exp_file, args.name)
    print("haha")