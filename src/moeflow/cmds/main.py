# -*- coding: utf-8 -*-
import cv2
import jinja2
import logging
import magic
import os
import shutil
import tempfile
import tensorflow as tf
import uuid
from base64 import b64encode
from sanic import Sanic, response
from moeflow.classify import classify_resized_face
from moeflow.face_detect import run_face_detection
from moeflow.jinja2_env import render
from moeflow.util import resize_large_image, resize_faces, cleanup_image_cache

app = Sanic(__name__)
dir_path = os.path.dirname(os.path.realpath(__file__))
static_path = os.path.join(dir_path, '..', 'static')
app.static('/static', static_path)

ALLOWED_MIMETYPE = ['image/jpeg', 'image/png']


@app.route("/", methods=['GET', 'POST'])
async def main_app(request):
    if request.method == "POST":
        uploaded_image  = request.files.get('uploaded_image')
        mime_type =  magic.from_buffer(uploaded_image.body, mime=True)
        if mime_type not in ALLOWED_MIMETYPE:
            return response.redirect('/')
        # Scale down input image to ~800 px
        image = resize_large_image(uploaded_image.body)
        with tempfile.NamedTemporaryFile(mode="wb", suffix='.jpg') as input_jpg:
            filename = input_jpg.name
            logging.info("Input file is created at {}".format(filename))
            cv2.imwrite(filename, image)
            # Copy to image directory
            ori_name = uuid.uuid4().hex + ".jpg"
            shutil.copyfile(filename, os.path.join(
                static_path, 'images', ori_name
            ))
            results = []
            # Run face detection with animeface-2009
            detected_faces = run_face_detection(filename)
            # This operation will rewrite detected faces to 96 x 96 px
            resize_faces(detected_faces)
            # Classify with TensorFlow
            if not detected_faces:  # Use overall image as default
                detected_faces = [filename]
            for face in detected_faces:
                predictions = classify_resized_face(
                    face,
                    app.label_lines,
                    app.graph
                )
                face_name = uuid.uuid4().hex + ".jpg"
                shutil.copyfile(face, os.path.join(
                    static_path, 'images', face_name
                ))
                results.append({
                    "image_name": face_name,
                    "prediction": predictions
                })
                logging.info(predictions)
            # Cleanup
            cleanup_image_cache(os.path.join(static_path, 'images'))
            for faces in detected_faces:
                if faces != filename:
                    os.remove(faces)
        return response.html(
            render(
                "main.html",
                ori_name=ori_name,
                results=results
            )
        )
    return response.html(render("main.html"))


@app.route("/hello_world")
async def hello_world(request):
    return response.text("Hello world!")


@app.listener('before_server_start')
async def initialize(app, loop):
    moeflow_path = os.environ.get('MOEFLOW_MODEL_PATH')
    label_path = os.path.join(os.sep, moeflow_path, "output_labels_2.txt")
    model_path = os.path.join(os.sep, moeflow_path, "output_graph_2.pb")
    app.label_lines = [
        line.strip() for line in tf.gfile.GFile(label_path)
    ]
    graph = tf.Graph()
    graph_def = tf.GraphDef()
    with tf.gfile.FastGFile(model_path, 'rb') as f:
        graph_def.ParseFromString(f.read())
    with graph.as_default():
        tf.import_graph_def(graph_def, name='')
    app.graph = graph
    logging.info("MoeFlow model is now initialized!")


def main():
    # Set logger
    logging.basicConfig(level=logging.INFO)
    app.run(host="0.0.0.0", port=8888)

if __name__ == '__main__':
    main_app()

