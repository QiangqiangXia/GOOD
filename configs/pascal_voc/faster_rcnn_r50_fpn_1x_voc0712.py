_base_ = [
    '../_base_/models/faster_rcnn_r50_fpn.py', '../_base_/datasets/voc0712.py',
    '../_base_/default_runtime.py'
]
model = dict(
    pretrained='torchvision://resnet50',
    roi_head=dict(
            bbox_head=dict(
                type='Shared2FCBBoxHead',
                in_channels=256,
                fc_out_channels=1024,
                roi_feat_size=7,
                num_classes=20,
                bbox_coder=dict(
                    type='DeltaXYWHBBoxCoder',
                    target_means=[0., 0., 0., 0.],
                    target_stds=[0.1, 0.1, 0.2, 0.2]),
                reg_class_agnostic=False,
                loss_cls=dict(
                    type='NewCombinationLoss', use_sigmoid=False, loss_weight=1.0),
                loss_bbox=dict(type='L1Loss', loss_weight=1.0))))
# optimizer
optimizer = dict(type='SGD', lr=0.005, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=dict(max_norm=35, norm_type=2))
custom_hooks = [dict(type='SetEpochInfoHook')]
lr_config = dict(policy='step', step=[2])
total_epochs = 6
log_config = dict(interval=1000)