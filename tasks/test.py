# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2025-08-12 19:30:17
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2025-08-12 20:03:11

from invoke import task

@task
def all(ctx):
    """
    Run unittest discovery on the tests/ folder.
    """
    ctx.run("python -m unittest discover -s tests")

@task
def creation(ctx):
    """
    Run unittest discovery on the tests/ folder but only test cookiecutter creation repo.
    """
    ctx.run("python -m unittest tests.test_cookiecutter.TestCookiecutterCreation")