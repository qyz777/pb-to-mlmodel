# -*- coding: utf-8 -*-

import coremltools


# 这里使用coremltools让CoreML model里的输入输出名字更规范
def rename_var():
    spec = coremltools.utils.load_spec('model.mlmodel')
    coremltools.utils.rename_feature(spec, 'Prediction__0', 'Prediction')
    coremltools.utils.rename_feature(spec, 'Input__0', 'Input')
    coremltools.models.utils.save_spec(spec, 'model.mlmodel')
    return