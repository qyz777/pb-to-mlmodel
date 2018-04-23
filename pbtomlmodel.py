import tfcoreml

tfcoreml.convert(tf_model_path="./model_0.pb",
                 mlmodel_path="./model.mlmodel",
                 output_feature_names=['out:0'],
                 input_name_shape_dict={'x-input:0': [1, 36]})
