# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2025-06-28 16:04:05
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2026-03-28 20:04:56

import os
import shutil

""" parse arguments """

package_name = '{{ cookiecutter.package_name }}'
os_license = '{{ cookiecutter.license }}'
src_structure = '{{ cookiecutter.src_structure }}'
project_type = '{{ cookiecutter.project_type }}'
setup_project = "{{ cookiecutter.setup_project }}"

""" license """

if os_license == "Not open source":
    os.remove("LICENSE")

""" project type """

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
else:
    pass

""" cleaned structure """

if src_structure == "Clean":
    shutil.rmtree("notebooks")
    shutil.rmtree("data")
    shutil.rmtree("docs/how_to_launch")
    shutil.rmtree("docs/project_information")
    shutil.rmtree("docs/references")
    shutil.rmtree("docs/wiki")
    shutil.rmtree(f'src/{package_name}/configs')
    shutil.rmtree(f'src/{package_name}/data')
    shutil.rmtree(f'src/{package_name}/io')
    shutil.rmtree(f'src/{package_name}/pipelines')
    shutil.rmtree(f'src/{package_name}/models')
    shutil.rmtree(f'src/{package_name}/schemas')
    shutil.rmtree(f'src/{package_name}/visualization')

""" setup project execution """

if setup_project == "Yes":
    os.system("git init")
    os.rename(".template_gitignore", ".gitignore")
    os.system("poetry install --with dev,tests")