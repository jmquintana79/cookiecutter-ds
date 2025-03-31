"""Clean tasks for pyinvoke."""

# %% IMPORTS

import os
import shutil
from invoke.context import Context
from invoke.tasks import task

# %% TASKS

# %% - Tools


@task
def mypy(ctx: Context) -> None:
    """Clean the mypy tool."""
    # define folder/file to be removed
    to_be_removed = ".mypy_cache"
    # remove if exists
    if os.path.exists(to_be_removed):
        shutil.rmtree(to_be_removed)


@task
def ruff(ctx: Context) -> None:
    """Clean the ruff tool."""
    ctx.run("ruff clean")


@task
def pytest(ctx: Context) -> None:
    """Clean the pytest tool."""
    # define folder/file to be removed
    to_be_removed = ".pytest_cache"
    # remove if exists
    if os.path.exists(to_be_removed):
        shutil.rmtree(to_be_removed)


# %% - Sources


@task
def venv(ctx: Context) -> None:
    """Clean the venv folder."""
   # define folder/file to be removed
    to_be_removed = ".venv"
    # remove if exists
    if os.path.exists(to_be_removed):
        shutil.rmtree(to_be_removed)



@task
def poetry(ctx: Context) -> None:
    """Clean poetry lock file."""
   # define folder/file to be removed
    to_be_removed = "poetry.lock"
    # remove if exists
    if os.path.exists(to_be_removed):
        shutil.rmtree(to_be_removed)



@task
def python(ctx: Context) -> None:
    """Clean python caches and bytecodes."""
    # initialize folders to be omited
    exclude_dirs     = [".venv"]
    # loop of paths
    for root, dirs, files in os.walk(path):
        # ommit folders
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        # loop of files
        for file in files:
            # remove .pyc files
            if file.endswith(".pyc"):
                os.remove(os.path.join(root, file))
                print(f"Removing: {os.path.join(root, file)}")
        # loop of dirs
        for dir in dirs:
            # remove __pycache__
            if dir == "__pycache__":
                shutil.rmtree(os.path.join(root, dir))
                print(f"Removing: {os.path.join(root, dir)}")

# %% - Combines


@task(pre=[mypy, ruff, pytest])
def tools(_: Context) -> None:
    """Run all tools tasks."""


@task(pre=[venv, poetry, python])
def sources(_: Context) -> None:
    """Run all sources tasks."""


@task(pre=[tools, sources], default=True)
def all(_: Context) -> None:
    """Run all tools and sources tasks."""

