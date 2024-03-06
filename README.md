# GOOD
This repository is an official implementation of the paper [Gradient optimization for object detection in learning with noisy labels]

If you find GOOD useful in your research then please cite:

`Xia Q, Hu C, Lee F, Chen Q. Gradient optimization for object detection in learning with noisy labels[J]. Information Sciences, 2024.`

Deep neural networks have made significant progress benefiting large-scale correctly human-labeled datasets. However, large-scale human-labeled datasets are often ambiguous because the limited experience can lead to mislabeled classes. Most research related to learning with noisy labels concentrates on image classification, while we focus on object detection that also suffers from noisy labels. In this paper, we propose a method that applies gradient optimization for object detection (GOOD), aiming to combat poor generalization caused by noisy labels in objection detection. Usually, a detection task is divided into a foreground-background subtask and a foreground-object subtask. Hence, gradient descent with cross-entropy exploits corrected gradient guidance for foreground-background subtask, while dynamic gradient underweighted ascent with cross-entropy and variant gradient clipping with improved symmetric cross-entropy are mutually employed to prevent incorrect gradient guidance for foreground-object subtask. We conducted extensive experiments on PASCAL VOC 2012 and COCO 2017, demonstrating the effectiveness of GOOD. Furthermore, we promote GOOD to instance segmentation, and competitive results on Cityscapes show that it is also appropriate for instance segmentation. Specifically, we achieved a 9.4% improvement on PASCAL VOC 2012, 5.2% on COCO 2017, and 4.3% on Cityscapes.

<div align=center>
<img src="https://github.com/QiangqiangXia/GOOD/blob/main/GOOD.png"> <width="500" height="300">
</div>

# Setups
Installtion:
Please check [install.md] for installation instructions.
