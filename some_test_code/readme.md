# 测试环境和数据集环境是否安装成功

## 1.测试环境是否安装成功

终端
```shell
pip install paddle paddlepaddle  # cpu
pip install paddle paddlepaddle-gpu # gpu
```

运行
```shell
python some_test_code/test_paddle_gpu.py
```

出现版本号和Your Paddle Fluid is installed successfully!说明成功

安装参考：https://www.paddlepaddle.org.cn/documentation/docs/zh/install/pip/linux-pip.html

## 2.数据集准备

### 安装pycocotools
```shell
pip install cython; pip install 'git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI'
```

### 数据集下载
官网下载coco2017数据集(https://cocodataset.org/#download)，
或者百度云(https://pan.baidu.com/s/1OLX8weMf63wgn4Eugx1jKw),提取码：evnp。
解压到数据集目录datasets，数据集目录应该是如下形式：
```
COCO/
  annotations/
    instances_{train,val}2017.json
  {train,val}2017/
    # image files that are mentioned in the corresponding json
```

## 3.pycocotools简单使用和标注框可视化
运行
```shell
python some_test_code/test_coco_datasets.py
```
可参考https://blog.csdn.net/qq_37541097/article/details/113247318