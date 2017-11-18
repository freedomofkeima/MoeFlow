# -*- coding: utf-8 -*-
from moeflow.cmds.main import hello_world


def test_hello_world():
    hello_world(object())
    assert True
