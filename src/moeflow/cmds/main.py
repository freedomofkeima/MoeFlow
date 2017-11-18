# -*- coding: utf-8 -*-
import cv2
import jinja2
import logging
import magic
import os
import tempfile
from sanic import Sanic, response
from moeflow.face_detect import run_face_detection
from moeflow.jinja2_env import render
from moeflow.util import resize_large_image

app = Sanic(__name__)
dir_path = os.path.dirname(os.path.realpath(__file__))
app.static('/static', os.path.join(dir_path, '..', 'static'))

ALLOWED_MIMETYPE = ['image/jpeg', 'image/png']


@app.route("/", methods=['GET', 'POST'])
async def main_app(request):
    if request.method == "POST":
        uploaded_image  = request.files.get('uploaded_image')
        mime_type =  magic.from_buffer(uploaded_image.body, mime=True)
        if mime_type not in ALLOWED_MIMETYPE:
            return response.redirect('/')
        image = resize_large_image(uploaded_image.body)
        with tempfile.NamedTemporaryFile(mode="wb", suffix='.jpg') as input_jpg:
            filename = input_jpg.name
            logging.info("Input file is created at {}".format(filename))
            cv2.imwrite(filename, image)
            detected_faces = run_face_detection(filename)
            logging.info(detected_faces)
            # Cleanup
            for faces in detected_faces:
                os.remove(faces)
    return response.html(render("main.html"))


@app.route("/hello_world")
async def hello_world(request):
    return response.text("Hello world!")


def main():
    # Set logger
    logging.basicConfig(level=logging.INFO)
    app.run(host="0.0.0.0", port=8888)

if __name__ == '__main__':
    main_app()

