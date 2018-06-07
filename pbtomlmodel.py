import tfcoreml


def convert():
    tfcoreml.convert(tf_model_path="./model_0.pb",
                     mlmodel_path="./model.mlmodel",
                     output_feature_names=['Prediction:0'],
                     input_name_shape_dict={'Input:0': [1, 36]})
