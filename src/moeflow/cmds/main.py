# -*- coding: utf-8 -*-
import jinja2
import logging
import os
from sanic import Sanic, response
from moeflow.jinja2_env import render

app = Sanic(__name__)
dir_path = os.path.dirname(os.path.realpath(__file__))
app.static('/static', os.path.join(dir_path, '..', 'static'))


@app.route("/", methods=['GET', 'POST'])
async def hello_world(request):
    if request.method == "POST":
        uploaded_image  = request.files.get('uploaded_image')
        logging.info(uploaded_image.name)
    return response.html(render("main.html"))


def main():
    # Set logger
    logging.basicConfig(level=logging.INFO)
    app.run(host="0.0.0.0", port=8888)

if __name__ == '__main__':
    main()

