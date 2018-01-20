# -*- coding: utf-8 -*-
import logging
import tensorflow as tf


def read_tensor_from_image_file(file_name, input_height=299, input_width=299,
                                input_mean=0, input_std=255):
    input_name = "file_reader"
    output_name = "normalized"
    file_reader = tf.read_file(file_name, input_name)
    image_reader = tf.image.decode_jpeg(
        file_reader,
        channels=3,
        name='jpeg_reader'
    )
    float_caster = tf.cast(image_reader, tf.float32)
    dims_expander = tf.expand_dims(float_caster, 0)
    resized = tf.image.resize_bilinear(
        dims_expander,
        [input_height, input_width]
    )
    normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
    sess = tf.Session()
    result = sess.run(normalized)

    return result


def classify_resized_face(file_name, label_lines, graph):
    results = []
    logging.info('Processing classification')
    with tf.Session(graph=graph) as sess:
        # Feed the image data as input to the graph and get first prediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        input_operation = sess.graph.get_operation_by_name("Mul")
        t = read_tensor_from_image_file(file_name)
        predictions = sess.run(
            softmax_tensor,
            {input_operation.outputs[0]: t}
        )
        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-3:][::-1]

        for node_id in top_k:
            human_string = label_lines[node_id]
            score = predictions[0][node_id]
            results.append((human_string, score))
    return results

