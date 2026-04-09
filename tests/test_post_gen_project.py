# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2026-03-28 18:07:39
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2026-03-28 20:07:46
"""
Tests funcionales para hooks/post_gen_project.py
"""

import os
from pathlib import Path
from unittest.mock import call, patch

import pytest

from helpers import (
    CLEAN_DIRS_TO_REMOVE,
    DS_DIRS_TO_REMOVE,
    PACKAGE_NAME,
    create_project_structure,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def render_script(
    package_name: str,
    os_license: str,
    src_structure: str,
    project_type: str,
    setup_project: str,
) -> str:
    return f"""
import os
import shutil

package_name  = {package_name!r}
os_license    = {os_license!r}
src_structure = {src_structure!r}
project_type  = {project_type!r}
setup_project = {setup_project!r}

if os_license == "Not open source":
    os.remove("LICENSE")

if project_type == "ML":
    pass
elif project_type == "DS":
    shutil.rmtree("data/artifacts")
    shutil.rmtree("data/development")
    shutil.rmtree("data/logs")
    shutil.rmtree("data/maintenance")
    shutil.rmtree("data/metadata")
    shutil.rmtree("data/historical/features")
    shutil.rmtree("data/operative/features")
elif project_type == "library":
    src_structure = "Clean"

if src_structure == "Clean":
    shutil.rmtree("notebooks")
    shutil.rmtree("data")
    shutil.rmtree("docs/how_to_launch")
    shutil.rmtree("docs/project_information")
    shutil.rmtree("docs/references")
    shutil.rmtree("docs/wiki")
    shutil.rmtree(f"src/{{package_name}}/configs")
    shutil.rmtree(f"src/{{package_name}}/data")
    shutil.rmtree(f"src/{{package_name}}/io")
    shutil.rmtree(f"src/{{package_name}}/pipelines")
    shutil.rmtree(f"src/{{package_name}}/models")
    shutil.rmtree(f"src/{{package_name}}/schemas")
    shutil.rmtree(f"src/{{package_name}}/visualization")

if setup_project == "Yes":
    os.system("git init")
    os.rename(".template_gitignore", ".gitignore")
    os.system("poetry install --with dev,tests")
"""


def run_post_gen(
    project_dir: Path,
    package_name: str = PACKAGE_NAME,
    os_license: str = "MIT",
    src_structure: str = "Full",
    project_type: str = "ML",
    setup_project: str = "No",
) -> "MagicMock":
    script = render_script(package_name, os_license, src_structure, project_type, setup_project)
    original_dir = os.getcwd()
    os.chdir(project_dir)
    try:
        with patch("os.system") as mock_system:
            exec(compile(script, "post_gen_project.py", "exec"), {})
            return mock_system
    finally:
        os.chdir(original_dir)


# ---------------------------------------------------------------------------
# Tests: licencia
# ---------------------------------------------------------------------------

class TestLicense:
    def test_license_removed_when_not_open_source(self, project_dir):
        run_post_gen(project_dir, os_license="Not open source")
        assert not (project_dir / "LICENSE").exists()

    def test_license_kept_when_mit(self, project_dir):
        run_post_gen(project_dir, os_license="MIT")
        assert (project_dir / "LICENSE").exists()

    def test_license_kept_when_apache(self, project_dir):
        run_post_gen(project_dir, os_license="Apache-2.0")
        assert (project_dir / "LICENSE").exists()


# ---------------------------------------------------------------------------
# Tests: project_type == "ML"
# ---------------------------------------------------------------------------

class TestProjectTypeML:
    def test_ml_keeps_all_dirs(self, project_dir):
        run_post_gen(project_dir, project_type="ML", src_structure="Full")
        for d in DS_DIRS_TO_REMOVE:
            assert (project_dir / d).exists(), f"Directorio eliminado incorrectamente: {d}"

    def test_ml_keeps_clean_dirs(self, project_dir):
        run_post_gen(project_dir, project_type="ML", src_structure="Full")
        for d in CLEAN_DIRS_TO_REMOVE:
            assert (project_dir / d).exists(), f"Directorio eliminado incorrectamente: {d}"


# ---------------------------------------------------------------------------
# Tests: project_type == "DS"
# ---------------------------------------------------------------------------

class TestProjectTypeDS:
    def test_ds_removes_specific_data_subdirs(self, project_dir):
        run_post_gen(project_dir, project_type="DS", src_structure="Full")
        for d in DS_DIRS_TO_REMOVE:
            assert not (project_dir / d).exists(), f"Directorio no eliminado: {d}"

    def test_ds_does_not_remove_clean_dirs(self, project_dir):
        run_post_gen(project_dir, project_type="DS", src_structure="Full")
        # notebooks y src/* deben seguir intactos
        assert (project_dir / "notebooks").exists()
        assert (project_dir / f"src/{PACKAGE_NAME}/models").exists()

    def test_ds_with_clean_structure_removes_everything(self, project_dir):
        run_post_gen(project_dir, project_type="DS", src_structure="Clean")
        for d in DS_DIRS_TO_REMOVE:
            assert not (project_dir / d).exists()
        for d in CLEAN_DIRS_TO_REMOVE:
            assert not (project_dir / d).exists()


# ---------------------------------------------------------------------------
# Tests: project_type == "library"
# ---------------------------------------------------------------------------

class TestProjectTypeLibrary:
    def test_library_triggers_clean_structure(self, project_dir):
        """library fuerza src_structure='Clean' internamente."""
        run_post_gen(project_dir, project_type="library", src_structure="Full")
        for d in CLEAN_DIRS_TO_REMOVE:
            assert not (project_dir / d).exists(), f"Directorio no eliminado: {d}"

    def test_library_ignores_src_structure_param(self, project_dir):
        """Aunque se pase src_structure='Full', library lo sobreescribe a Clean."""
        run_post_gen(project_dir, project_type="library", src_structure="Full")
        assert not (project_dir / "notebooks").exists()

    def test_library_removes_data_via_clean(self, project_dir):
        run_post_gen(project_dir, project_type="library")
        assert not (project_dir / "data").exists()


# ---------------------------------------------------------------------------
# Tests: src_structure == "Clean" directo
# ---------------------------------------------------------------------------

class TestCleanStructure:
    def test_clean_removes_all_expected_dirs(self, project_dir):
        run_post_gen(project_dir, project_type="ML", src_structure="Clean")
        for d in CLEAN_DIRS_TO_REMOVE:
            assert not (project_dir / d).exists(), f"Directorio no eliminado: {d}"

    def test_full_keeps_all_dirs(self, project_dir):
        run_post_gen(project_dir, project_type="ML", src_structure="Full")
        for d in CLEAN_DIRS_TO_REMOVE:
            assert (project_dir / d).exists(), f"Directorio eliminado incorrectamente: {d}"

    def test_clean_fails_if_dir_missing(self, tmp_path):
        """Si falta un directorio esperado, el script debe lanzar error."""
        create_project_structure(tmp_path)
        (tmp_path / "notebooks").rmdir()
        with pytest.raises(FileNotFoundError):
            run_post_gen(tmp_path, project_type="ML", src_structure="Clean")


# ---------------------------------------------------------------------------
# Tests: setup_project
# ---------------------------------------------------------------------------

class TestSetupProject:
    def test_setup_yes_calls_git_init(self, project_dir):
        mock_system = run_post_gen(project_dir, setup_project="Yes")
        mock_system.assert_any_call("git init")

    def test_setup_yes_calls_poetry_install(self, project_dir):
        mock_system = run_post_gen(project_dir, setup_project="Yes")
        mock_system.assert_any_call("poetry install --with dev,tests")

    def test_setup_yes_commands_in_order(self, project_dir):
        mock_system = run_post_gen(project_dir, setup_project="Yes")
        assert mock_system.call_args_list == [
            call("git init"),
            call("poetry install --with dev,tests"),
        ]

    def test_setup_yes_renames_gitignore(self, project_dir):
        run_post_gen(project_dir, setup_project="Yes")
        assert not (project_dir / ".template_gitignore").exists()
        assert (project_dir / ".gitignore").exists()

    def test_setup_no_does_not_call_os_system(self, project_dir):
        mock_system = run_post_gen(project_dir, setup_project="No")
        mock_system.assert_not_called()

    def test_setup_no_keeps_template_gitignore(self, project_dir):
        run_post_gen(project_dir, setup_project="No")
        assert (project_dir / ".template_gitignore").exists()
        assert not (project_dir / ".gitignore").exists()


# ---------------------------------------------------------------------------
# Tests: combinaciones completas
# ---------------------------------------------------------------------------

class TestCombinations:
    def test_ml_full_no_setup(self, project_dir):
        mock_system = run_post_gen(
            project_dir, os_license="MIT", project_type="ML",
            src_structure="Full", setup_project="No",
        )
        assert (project_dir / "LICENSE").exists()
        assert (project_dir / "notebooks").exists()
        mock_system.assert_not_called()

    def test_ml_clean_with_setup(self, project_dir):
        mock_system = run_post_gen(
            project_dir, os_license="MIT", project_type="ML",
            src_structure="Clean", setup_project="Yes",
        )
        for d in CLEAN_DIRS_TO_REMOVE:
            assert not (project_dir / d).exists()
        mock_system.assert_any_call("git init")

    def test_ds_full_no_setup(self, project_dir):
        run_post_gen(
            project_dir, os_license="MIT", project_type="DS",
            src_structure="Full", setup_project="No",
        )
        for d in DS_DIRS_TO_REMOVE:
            assert not (project_dir / d).exists()
        assert (project_dir / "notebooks").exists()

    def test_library_not_open_source_with_setup(self, project_dir):
        mock_system = run_post_gen(
            project_dir, os_license="Not open source", project_type="library",
            src_structure="Full", setup_project="Yes",
        )
        assert not (project_dir / "LICENSE").exists()
        for d in CLEAN_DIRS_TO_REMOVE:
            assert not (project_dir / d).exists()
        mock_system.assert_any_call("git init")
        assert (project_dir / ".gitignore").exists()