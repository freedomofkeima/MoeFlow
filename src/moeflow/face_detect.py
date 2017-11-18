# -*- coding: utf-8 -*-
import logging
import os
import subprocess


def run_face_detection(input_image_path):
    """
    Receives input image path
    Return list of path (detected faces in /tmp directory)
    """
    args = [
        'ruby',
        'detect.rb',
        input_image_path,
        '/tmp'
    ]
    results = []
    # Execute
    try:
        output = subprocess.check_output(
            args,
            shell=False,
            timeout=30
        )
    except Exception:
        logging.exception("Face detection failed!")
        return []
    input_name_base = os.path.basename(input_image_path)
    input_name_without_ext = os.path.splitext(input_name_base)[0]
    for filename in os.listdir('/tmp'):
        if filename.startswith(input_name_without_ext + '_out'):
            results.append("/tmp/{}".format(filename))
    return results

