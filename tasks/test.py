# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2025-08-12 19:30:17
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2026-03-28 18:29:59

from invoke import task

@task
def all(ctx):
    """
    Run unittest discovery on the tests/ folder.
    """
    ctx.run("python -m pytest tests/ -v")
