import os
import shutil

package_name = '{{ cookiecutter.package_name }}'
os_license = '{{ cookiecutter.license }}'
src_structure = '{{ cookiecutter.src_structure }}'
project_type = '{{ cookiecutter.project_type }}'
setup_project = "{{ cookiecutter.setup_project }}"
python_version = "{{cookiecutter.python_version}}"

if os_license == "Not open source":
    os.remove("LICENSE")

if project_type == "DS":
    shutil.rmtree("tests")
    shutil.rmtree("logs")
    shutil.rmtree("data/features")
    # tasks ????

if src_structure == "Clean":
    shutil.rmtree(f'src/{package_name}/data')
    shutil.rmtree(f'src/{package_name}/pipelines')
    shutil.rmtree(f'src/{package_name}/models')
    shutil.rmtree(f'src/{package_name}/visualization')

if setup_project == "Yes":
    os.system("git init")
    os.rename(".template_gitignore", ".gitignore")
    os.system(f"poetry env use {python_version}")
    os.system("poetry install --with dev,tests")