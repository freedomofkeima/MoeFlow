# -*- coding: utf-8 -*-
import jinja2
import logging
import magic
import os
from sanic import Sanic, response
from moeflow.jinja2_env import render
from moeflow.util import resize_large_image

app = Sanic(__name__)
dir_path = os.path.dirname(os.path.realpath(__file__))
app.static('/static', os.path.join(dir_path, '..', 'static'))


ALLOWED_MIMETYPE = ['image/jpeg', 'image/png']

@app.route("/", methods=['GET', 'POST'])
async def hello_world(request):
    if request.method == "POST":
        uploaded_image  = request.files.get('uploaded_image')
        mime_type =  magic.from_buffer(uploaded_image.body, mime=True)
        if mime_type not in ALLOWED_MIMETYPE:
            return response.redirect('/')
        image = resize_large_image(uploaded_image.body)
        width, height = image.shape[:2]
        logging.info("Resized Width: {} Height: {}".format(width, height))
    return response.html(render("main.html"))


def main():
    # Set logger
    logging.basicConfig(level=logging.INFO)
    app.run(host="0.0.0.0", port=8888)

if __name__ == '__main__':
    main()

