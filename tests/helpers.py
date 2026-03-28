# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2026-03-28 18:26:19
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2026-03-28 20:08:05

from pathlib import Path

PACKAGE_NAME = "my_package"

DS_DIRS_TO_REMOVE = [
    "data/artifacts",
    "data/development",
    "data/logs",
    "data/maintenance",
    "data/metadata",
    "data/historical/features",
    "data/operative/features",
]

CLEAN_DIRS_TO_REMOVE = [
    "notebooks",
    "data",
    "docs/how_to_launch",
    "docs/project_information",
    "docs/references",
    "docs/wiki",
    f"src/{PACKAGE_NAME}/configs",
    f"src/{PACKAGE_NAME}/data",
    f"src/{PACKAGE_NAME}/io",
    f"src/{PACKAGE_NAME}/pipelines",
    f"src/{PACKAGE_NAME}/models",
    f"src/{PACKAGE_NAME}/schemas",
    f"src/{PACKAGE_NAME}/visualization",
]


def create_project_structure(base_path: Path, package_name: str = PACKAGE_NAME) -> None:
    """Replica de la estructura de directorios que genera cookiecutter."""
    dirs = [
        # data
        "data/artifacts",
        "data/development",
        "data/logs",
        "data/maintenance",
        "data/metadata",
        "data/historical/features",
        "data/operative/features",
        # docs
        "docs/how_to_launch",
        "docs/project_information",
        "docs/references",
        "docs/wiki",
        # notebooks
        "notebooks",
        # src
        f"src/{package_name}/configs",
        f"src/{package_name}/data",
        f"src/{package_name}/io",
        f"src/{package_name}/pipelines",
        f"src/{package_name}/models",
        f"src/{package_name}/schemas",
        f"src/{package_name}/visualization",
    ]
    for d in dirs:
        (base_path / d).mkdir(parents=True, exist_ok=True)

    (base_path / "LICENSE").write_text("MIT License")
    (base_path / ".template_gitignore").write_text("*.pyc\n__pycache__/\n")