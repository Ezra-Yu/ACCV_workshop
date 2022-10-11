_base_ =[
    './_base_/dataset_vit.py',
    './_base_/default_runtime.py',
    './_base_/scheduler_vit.py'
]
"""
model = dict(
    type='ImageClassifier',
    backbone=dict(
        type='VisionTransformer',
        arch='large',
        img_size=224,
        patch_size=16,
        drop_path_rate=0.1,
        avg_token=True,
        output_cls_token=False,
        final_norm=False,
        init_cfg=dict(
            type='Pretrained',
            checkpoint='~/accv/liuyuan/mae_webnat_pretrain/epoch_1600.pth',
            prefix='backbone.')),
    neck=None,
    head=dict(
        type='LinearClsHead',
        num_classes=5000,
        in_channels=1024,
        loss=dict(
            type='LabelSmoothLoss', label_smooth_val=0.1, mode='original'),
        init_cfg=[dict(type='TruncNormal', layer='Linear', std=2e-05)]),
    train_cfg=dict(augments=[
        dict(type='Mixup', alpha=0.8, num_classes=5000),
        dict(type='CutMix', alpha=1.0, num_classes=5000)
    ]))

"""

custom_imports = dict(imports=['src', 'mmselfsup.engine' ], allow_failed_imports=False)

model = dict(
    type='ImageClassifier',
    backbone=dict(
        type='VisionTransformer',
        arch='large',
        img_size=224,
        patch_size=16,
        drop_path_rate=0.1,
        avg_token=True,
        output_cls_token=False,
        final_norm=False,
        init_cfg=dict(
            type='Pretrained',
            checkpoint='~/accv/liuyuan/mae_webnat_pretrain/epoch_1600.pth',
            prefix='backbone.')),
    neck=None,
    head=dict(
        type='ArcFaceHead',
        num_classes=5000,
        in_channels=1024,
        feature_norm=True,
        weight_norm=True,
        used='after',
        loss = dict(type='CrossEntropyLoss', loss_weight=1.0),
        init_cfg=dict(type='Normal', layer='Linear', std=0.01))
)
