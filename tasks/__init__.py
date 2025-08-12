# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2025-08-12 18:21:40
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2025-08-12 20:18:20

from invoke import Collection
from . import devops
from . import test

# add submodule as a collection
ns = Collection()
ns.add_collection(Collection(devops), name="devops")
ns.add_collection(Collection(test), name="test")