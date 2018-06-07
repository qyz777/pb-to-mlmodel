# -*- coding: utf-8 -*-
# 注意，经过本人尝试，tfcoreml这个库只支持python2，具体信息查看https://github.com/tf-coreml/tf-coreml
#
# 如果你的输入是图片，直接使用tfcoreml，你的CoreML model的输入只会是MultiArrays
# 所以你需要对你的输入进行一些改动才能让CoreML model显示的输入是图片
# 具体参考 https://github.com/tf-coreml/tf-coreml/blob/master/examples/style_transfer_example.ipynb

import tensorflow as tf
from tensorflow.core.framework import graph_pb2
import operator
import sys
import pbtomlmodel
import tool


def inspect(model_pb, output_txt_file):
    graph_def = graph_pb2.GraphDef()
    with open(model_pb, "rb") as f:
        graph_def.ParseFromString(f.read())

    tf.import_graph_def(graph_def)

    sess = tf.Session()
    OPS = sess.graph.get_operations()

    ops_dict = {}

    sys.stdout = open(output_txt_file, 'w')
    for i, op in enumerate(OPS):
        print(
        '---------------------------------------------------------------------------------------------------------------------------------------------')
        print("{}: op name = {}, op type = ( {} ), inputs = {}, outputs = {}".format(i, op.name, op.type, ", ".join(
            [x.name for x in op.inputs]), ", ".join([x.name for x in op.outputs])))
        print('@input shapes:')
        for x in op.inputs:
            print("name = {} : {}".format(x.name, x.get_shape()))
        print('@output shapes:')
        for x in op.outputs:
            print("name = {} : {}".format(x.name, x.get_shape()))
        if op.type in ops_dict:
            ops_dict[op.type] += 1
        else:
            ops_dict[op.type] = 1

    print(
    '---------------------------------------------------------------------------------------------------------------------------------------------')
    sorted_ops_count = sorted(ops_dict.items(), key=operator.itemgetter(1))
    print('OPS counts:')
    for i in sorted_ops_count:
        print("{} : {}".format(i[0], i[1]))


if __name__ == "__main__":
    # 生成网络结构文件，可以通过这个文件查看你需要的输入和输出
    inspect("./model_0.pb", "./network-info.txt")
    # 转换成CoreML model
    pbtomlmodel.convert()
    # 规范化CoreML model的输入输出名
    tool.rename_var()
