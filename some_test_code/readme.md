# 测试环境和数据集环境是否安装成功

## 1.测试环境是否安装成功

终端
cpu:pip install paddle paddlepaddle
gpu:pip install paddle paddlepaddle-gpu

运行python yolox-paddle/test_paddle_gpu.py

出现版本号和Your Paddle Fluid is installed successfully!说明成功

安装参考：https://www.paddlepaddle.org.cn/documentation/docs/zh/install/pip/linux-pip.html

## 2.数据集准备

### 安装pycocotools
pip install cython; pip install 'git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI'

### 数据集准备
官网下载coco2017数据集https://cocodataset.org/#download，或者百度云https://pan.baidu.com/s/1OLX8weMf63wgn4Eugx1jKw（提取码：evnp）
解压到数据集目录datasets，数据集目录应该是如下形式
```
COCO/
  annotations/
    instances_{train,val}2017.json
  {train,val}2017/
    # image files that are mentioned in the corresponding json
```