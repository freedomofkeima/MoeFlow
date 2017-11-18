import os

import jinja2

dir_path = os.path.dirname(os.path.realpath(__file__))


def render(tpl_path, context={}):
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(
            os.path.join(dir_path, 'templates')
        )
    ).get_template(tpl_path).render(context)
