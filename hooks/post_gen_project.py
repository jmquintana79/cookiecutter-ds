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

if package_manager == "conda":
    os.remove("requirements.txt")
    os.remove("poetry.toml")
    os.remove("Pipfile")
elif package_manager == "pip":
    os.remove("environment.yml")
    os.remove("poetry.toml")
    os.remove("Pipfile")
elif package_manager == "poetry":
    os.remove("requirements.txt")
    os.remove("environment.yml")
    os.remove("Pipfile")
elif package_manager == "pipenv":
    os.remove("requirements.txt")
    os.remove("environment.yml")  
    os.remove("poetry.toml")  

if workflow_automation == "Python":
    os.remove("Makefile")
elif workflow_automation == "Make":
    pass
elif workflow_automation == "Invoke":
    os.remove("Makefile")

if project_report == "No":
    shutil.rmtree("reports")

if notebooks == "No":
    shutil.rmtree("notebooks")

if src_structure == "Less":
    shutil.rmtree('src/data')
    #shutil.rmtree('src/features')
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