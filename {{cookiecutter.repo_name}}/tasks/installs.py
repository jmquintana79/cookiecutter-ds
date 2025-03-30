"""Install tasks for pyinvoke."""

# %% IMPORTS

from invoke.context import Context
from invoke.tasks import task

# %% CONFIGS

REQUIREMENTS = "requirements.txt"


# %% TASKS


@task
def poetry(ctx: Context) -> None:
    """Install poetry packages."""
    ctx.run("poetry install")

@task
def requirements(ctx: Context) -> None:
    """Export the project requirements file."""
    ctx.run(f"poetry export --without-urls --without-hashes --output={REQUIREMENTS}")

@task(pre=[poetry], default=True)
def all(_: Context) -> None:
    """Run all install tasks."""