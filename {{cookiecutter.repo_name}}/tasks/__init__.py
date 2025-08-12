from invoke import Collection
from . import devops

# add submodule as a collection
ns = Collection()
ns.add_collection(Collection(devops), name="devops")