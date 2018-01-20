# -*- coding: utf-8 -*-
import os

import jinja2

dir_path = os.path.dirname(os.path.realpath(__file__))


def render(tpl_path, **context):
    relative_url_path = os.environ.get("MOEFLOW_RELATIVE_URL_PATH")
    if not relative_url_path:
        relative_url_path = ""
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(
            os.path.join(dir_path, 'templates')
        )
    ).get_template(tpl_path).render(url_path=relative_url_path, **context)
