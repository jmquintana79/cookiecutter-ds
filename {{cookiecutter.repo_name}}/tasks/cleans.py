"""Clean tasks for pyinvoke."""

# %% IMPORTS

from invoke.context import Context
from invoke.tasks import task

# %% TASKS

# %% - Tools


@task
def mypy(ctx: Context) -> None:
    """Clean the mypy tool."""
    ctx.run("rm -rf .mypy_cache/")


@task
def ruff(ctx: Context) -> None:
    """Clean the ruff tool."""
    ctx.run("ruff clean")


@task
def pytest(ctx: Context) -> None:
    """Clean the pytest tool."""
    ctx.run("rm -rf .pytest_cache/")



# %% - Sources


@task
def venv(ctx: Context) -> None:
    """Clean the venv folder."""
    ctx.run("rm -rf .venv/")


@task
def poetry(ctx: Context) -> None:
    """Clean poetry lock file."""
    ctx.run("rm -f poetry.lock")


@task
def python(ctx: Context) -> None:
    """Clean python caches and bytecodes."""
    ctx.run("find . -type f -name '*.py[co]' -delete")
    ctx.run(r"find . -type d -name __pycache__ -exec rm -r {} \+")


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

