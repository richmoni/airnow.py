#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

import pytest

import airnow


def test_is_canonical():
    # https://www.python.org/dev/peps/pep-0440/
    assert re.match(r'^([1-9]\d*!)?(0|[1-9]\d*)(\.(0|[1-9]\d*))*((a|b|rc)'
                    + r'(0|[1-9]\d*))?(\.post(0|[1-9]\d*))?(\.dev(0|[1-9]\d*))'
                    + r'?$', airnow.__version__) is not None
