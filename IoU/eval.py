# -*- coding: utf-8 -*-
from metrics import Evaluator
from PIL import Image
import numpy as np
import os

def evaluate_single(gt,pred,num_of_class):
    evaluator = Evaluator(num_of_class)
    # evaluator.reset()
    evaluator.add_batch(gt,pred)
    
    Acc = evaluator.Pixel_Accuracy()
    Acc_class = evaluator.Pixel_Accuracy_Class()
    mIoU = evaluator.Mean_Intersection_over_Union()
    FWIoU = evaluator.Frequency_Weighted_Intersection_over_Union()

    return Acc, Acc_class, mIoU, FWIoU

def evaluate_batch(gt_list,pred_list,num_of_class):
    evaluator = Evaluator(num_of_class)
    # evaluator.reset()
    for i in range(len(gt_list)):
        evaluator.add_batch(gt_list[i],pred_list[i])
    Acc = evaluator.Pixel_Accuracy()
    Acc_class = evaluator.Pixel_Accuracy_Class()
    mIoU = evaluator.Mean_Intersection_over_Union()
    FWIoU = evaluator.Frequency_Weighted_Intersection_over_Union()

    return Acc, Acc_class, mIoU, FWIoU

def main():
    # Example code: 
    #
    # Both pred and gt has to be numpy array (or with cuda accelerated).
    # Both pred and gt has to be in form of label map, 
    # namely single channel with value of [0,1,2,3,...],
    # starting from definite 0 to (num_of_class - 1).
    # This means you might have to run certain scripts to transform masks into label maps.
    # 
    # If you have labels [0,1,2,3,4] where label = 4 indicates ignored label,
    # just configure the number of class to be 4,
    # so the script will only read pixels 
    # where the value of gt belongs to [0,1,2,3].

    pred = np.array(Image.open("1/pred/DJI_0285.JPG"))
    gt = np.array(Image.open("1/gt/DJI_0285.png"))
    print(evaluate_single(pred,gt,5))

    pred_list = []
    gt_list = []
    for root, _, files in os.walk("1/pred"):
    # root 表示当前正在访问的文件夹路径
    # dirs 表示该文件夹下的子目录名list
    # files 表示该文件夹下的文件list
        for f in files:
            pred_list.append(np.array(Image.open(os.path.join(root,f))))

    for root, _, files in os.walk("1/gt"):
        for f in files:
            gt_list.append(np.array(Image.open(os.path.join(root,f))))

    # pred_list.append(np.array(Image.open("c.png")))
    # pred_list.append(np.array(Image.open("d.png")))
    # gt_list.append(np.array(Image.open("c.png")))
    # gt_list.append(np.array(Image.open("d.png")))
    print(evaluate_batch(pred_list,gt_list,5))

main()