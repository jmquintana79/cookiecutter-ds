# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2025-08-12 18:21:40
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2025-08-12 18:21:53

from invoke import Collection
from . import devops

# add submodule as a collection
ns = Collection(devops)