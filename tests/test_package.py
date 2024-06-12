from __future__ import annotations

import importlib.metadata

import pychannelfinder as m


def test_version():
    assert importlib.metadata.version("pychannelfinder") == m.__version__
