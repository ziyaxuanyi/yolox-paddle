from pycocotools.coco import COCO   # 导入pycocotools
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np
import random

coco_root = "./datasets/COCO/" # 数据集跟路径
datatype = "val2017" # 验证集
annofile = coco_root + "annotations/instances_{}.json".format(datatype)  # 验证集标注信息

coco_api = COCO(annofile)  # 为实例注释初始化COCO的API

ids = list(sorted(coco_api.imgs.keys()))   # 获取所有图片索引，并按索引排序
print("number of val images: {}".format(len(ids)))  # 验证集图片总数

coco_classes = dict([(v["id"], v["name"]) for _, v in coco_api.cats.items()])  # 构建分类字典，注意这里的id对应的是stuff的91个类别索引

# 可视化前三张图片的标注
for img_id in ids[0:3]:
    # 获取对应图像id的所有标注的索引
    ann_idx = coco_api.getAnnIds(imgIds=img_id)

    # 由标注索引获取对应的标注
    targets = coco_api.loadAnns(ann_idx)

    # 由图片索引获取图片名称
    image_name = coco_api.loadImgs(img_id)[0]["file_name"]

    # 读取图片
    image_path = coco_root + datatype + "/" + image_name
    img = cv2.imread(image_path)

    for target in targets:  # 遍历每个目标
        x, y, w, h = target["bbox"]    # 目标的左上角x,y坐标和宽度w以及高度h
        x1, y1, x2, y2 = int(x), int(y), int(x + w), int(y + h)
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2, 8)  # 绘制矩形框
        cv2.putText(img, coco_classes[target["category_id"]], (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
    
    cv2.imwrite("some_test_code/" + image_name, img)
    cv2.imshow("img", img)
    cv2.waitKey(0)


print("haha")