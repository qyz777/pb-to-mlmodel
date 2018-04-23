# pb-to-mlmodel
## 把pb模型转化为CoreML的mlmodel模型

最近有需求需要把tensorflow训练的模型在iOS上使用，然后我在GitHub上发现了一个叫[tf-coreml](https://github.com/tf-coreml/tf-coreml)的库，他可以把pb模型转化为mlmodel模型。这里讲一下我踩坑的心得

首先你得有个pb模型，然后用他们那个库里utils/下的一个inspect_pb.py文件

![img](https://github.com/qyz777/pb-to-mlmodel/blob/master/images/01.png)

![img](https://github.com/qyz777/pb-to-mlmodel/blob/master/images/02.png)

这个文件可以把pb模型图里的所有信息写在一个txt格式的文件里

![img](https://github.com/qyz777/pb-to-mlmodel/blob/master/images/03.png)

然后上代码

	import tfcoreml

	tfcoreml.convert(tf_model_path="./model_0.pb",
                 mlmodel_path="./model.mlmodel",
                 output_feature_names=['out:0'],
                 input_name_shape_dict={'x-input:0': [1, 36]})

这里解释一下，第一个参数是pb模型的路径，第二个参数是生成mlmodel模型的路径，第三个是输出的名字，这个输出的名字需要在之前生成的txt文件里有，且是你需要的，第四个是可选的，像我的x-input的shape是[?, 36]，所以我这里写了
