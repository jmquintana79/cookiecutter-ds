# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2025-08-12 19:52:44
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2025-08-12 20:11:28

import unittest
import subprocess
import shutil
import os

class TestCookiecutterCreation(unittest.TestCase):
    """Test Cookiecutter repo creation"""

    # initialization folder and name of dummy repo created and removed
    TEMPLATE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    DUMMY_NAME = "dummy_project_unittest"

    def run_cookiecutter(self, repo_name, project_type, src_structure, setup_project):
        """Run cookiecutter repo creation experiment

        Arguments:
            repo_name {_type_} -- Repos name fixed.
            project_type {_type_} -- Project type (ML, DS, library).
            src_structure {_type_} -- If create a full or cleaned structure.
            setup_project {_type_} -- If install settings or not.
        """
        # create command
        cmd = [
            "cookiecutter",
            self.TEMPLATE_PATH,
            "--no-input",
            f"repo_name={repo_name}",
            f"project_type={project_type}",
            f"src_structure={src_structure}",
            f"setup_project={setup_project}",
            "user=testuser",
            f"name={repo_name}",
            "author_name=Test Author <test@example.com>",
            "description=Test project",
            "version=0.1.0",
            "python_version=3.12",
            "license=MIT License",
            "data_libraries=No",
        ]
        # execute command
        subprocess.run(cmd, check=True)

    def tearDown(self):
        """Remove automatically the created repo if exist"""
        if os.path.exists(self.DUMMY_NAME):
            shutil.rmtree(self.DUMMY_NAME)

    """ testing all types + MORE + NO instalation """

    def test_ml_more_no(self):
        """Test ML with MORE structure and NO settings instalation"""
        self.run_cookiecutter(self.DUMMY_NAME, "ML", "More", "No")
        self.assertTrue(os.path.exists(self.DUMMY_NAME))

    def test_ds_more_no(self):
        """Test DS with MORE structure and NO settings instalation"""
        self.run_cookiecutter(self.DUMMY_NAME, "DS", "More", "No")
        self.assertTrue(os.path.exists(self.DUMMY_NAME))

    def test_library_more_no(self):
        """Test LIBRARY with MORE structure and NO settings instalation"""
        self.run_cookiecutter(self.DUMMY_NAME, "library", "More", "No")
        self.assertTrue(os.path.exists(self.DUMMY_NAME))

    """ testing all types + CLEAN + NO instalation """

    """ testing all types + MORE + YES instalation """