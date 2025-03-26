import os
import shutil

os_license = '{{ cookiecutter.license }}'
src_structure = '{{ cookiecutter.src_structure }}'
setup_project = "{{ cookiecutter.setup_project }}"

if os_license == "Not open source":
    os.remove("LICENSE")

"""
if src_structure == "Less":
    shutil.rmtree('src/data')
    shutil.rmtree('src/features')
    shutil.rmtree('src/models')
    shutil.rmtree('src/visualization')
    shutil.rmtree("reports")
"""

"""
if setup_project == "Yes - select this":
    os.system("git init")
    os.system("pipenv install --dev")
    os.system(
        "pipenv run ipython kernel install --name "
        '"py3_{{ cookiecutter.repo_name }}" --user'
    )
"""