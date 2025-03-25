# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2025-03-25 16:28:43
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2025-03-25 16:50:47
import os
import shutil

os_license = '{{ cookiecutter.license }}'
package_manager = '{{ cookiecutter.package_manager }}'
workflow_automation = '{{ cookiecutter.workflow_automation }}'
project_report = '{{ cookiecutter.project_report }}'
notebooks = '{{ cookiecutter.notebooks }}'
src_structure = '{{ cookiecutter.src_structure }}'
setup_project = "{{ cookiecutter.setup_project }}"

if os_license == "Not open source":
    os.remove("LICENSE")


if project_report == "No":
    shutil.rmtree("reports")

if notebooks == "No":
    shutil.rmtree("notebooks")

if src_structure == "Less":
    shutil.rmtree('src/data')
    shutil.rmtree('src/features')
    shutil.rmtree('src/models')
    shutil.rmtree('src/visualization')

"""
if setup_project == "Yes - select this":
    os.system("git init")
    os.system("pipenv install --dev")
    os.system(
        "pipenv run ipython kernel install --name "
        '"py3_{{ cookiecutter.repo_name }}" --user'
    )
"""