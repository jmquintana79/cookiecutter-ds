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
    shutil.rmtree("tests")
    shutil.rmtree("logs")
    shutil.rmtree("data/features")
elif project_type == "library":
    shutil.rmtree("data")
    src_structure = "Clean"
else:
    pass

""" cleaned structure """

if src_structure == "Clean":
    shutil.rmtree("notebooks")
    shutil.rmtree("logs")
    shutil.rmtree("tests")
    shutil.rmtree("outputs")
    shutil.rmtree(f'src/{package_name}/data')
    shutil.rmtree(f'src/{package_name}/pipelines')
    shutil.rmtree(f'src/{package_name}/models')
    shutil.rmtree(f'src/{package_name}/visualization')

""" setup project execution """

if setup_project == "Yes":
    os.system("git init")
    os.rename(".template_gitignore", ".gitignore")
    os.system("poetry install --with dev,tests")