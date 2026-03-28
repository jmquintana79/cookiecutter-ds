# Cookiecutter template for DS

![Python version](https://img.shields.io/badge/Python-3.x-informational)
![Issues closed](https://img.shields.io/github/issues-closed/jmquintana79/cookiecutter-ds)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

*Juan Quintana (based on [gh:Jswig/cookiecutter-flexible-ml](https://github.com/Jswig/cookiecutter-flexible-ml))*

A flexible cookiecutter template for reproducible data science.
`cookiecutter` is a command-line utility that creates projects from 
cookiecutters (project templates). See
[cookiecutter.readthedocs.io](https://cookiecutter.readthedocs.io/en/1.7.0/index.html).

## Usage

*Requirements*:
- [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.0/min) >= 1.1

Run
```bash
cookiecutter gh:jmquintana79/cookiecutter-ds
```
or directly from outside of the root folder

```bash
cookiecutter cookiecutter-ds/
```

`[Enter]` will select the default option in prompt.


## Generated project structure

Some of these might not be created depending on options picked
```
.
├── CHANGELOG.md
├── LICENSE
├── README.md
├── data
│   ├── artifacts
│   ├── development
│   ├── historical
│   │   ├── features
│   │   ├── intermediate
│   │   ├── processed
│   │   ├── raw
│   │   └── results
│   ├── logs
│   ├── maintenance
│   ├── metadata
│   ├── operative
│   │   ├── features
│   │   ├── intermediate
│   │   ├── processed
│   │   ├── raw
│   │   └── results
│   ├── reports
│   ├── static_tables
│   ├── synthesis
│   └── visualizations
├── docs
│   ├── API
│   ├── how_to_launch
│   │   ├── for_development
│   │   │   ├── pipelines
│   │   │   ├── settings
│   │   │   └── tasks
│   │   └── for_operation
│   │       ├── pipelines
│   │       ├── settings
│   │       └── tasks
│   ├── project_information
│   │   ├── canvas
│   │   │   ├── project_comunication.md
│   │   │   ├── project_hypothesis.md
│   │   │   ├── project_solution.md
│   │   │   ├── project_success_criterion.md
│   │   │   └── project_target.md
│   │   └── reports
│   │       ├── presentation.md
│   │       └── report.md
│   ├── references
│   │   ├── papers
│   │   └── web_references.md
│   └── wiki
│       ├── analysis
│       │   └── notebook_i.md
│       ├── data
│       │   ├── datasets
│       │   │   └── dataset_i
│       │   │       ├── availability.md
│       │   │       ├── describe.md
│       │   │       └── info.md
│       │   ├── inventory.md
│       │   └── tables
│       │       └── table_i
│       │           ├── availability.md
│       │           ├── describe.md
│       │           └── info.md
│       ├── data_processing
│       │   ├── data_cleaning.md
│       │   ├── features_engineering.md
│       │   └── post_processing.md
│       ├── metrics
│       ├── miscellaneous
│       ├── models
│       └── pipelines
│           ├── evaluation
│           ├── operation
│           ├── preprocessing
│           └── training
├── invoke.toml
├── notebooks
│   ├── analysis
│   ├── development
│   └── tools
├── poetry.toml
├── pyproject.toml
├── src
│   └── {{cookiecutter.package_name}}
│       ├── __init__.py
│       ├── configs
│       │   ├── __init__.py
│       │   ├── columns.py
│       │   ├── env.py
│       │   ├── experiment.py
│       │   ├── io.py
│       │   └── operation.py
│       ├── data
│       │   ├── __init__.py
│       │   ├── cleaning.py
│       │   ├── dataloader.py
│       │   ├── features.py
│       │   ├── ingestion.py
│       │   ├── labeling.py
│       │   ├── schemas.py
│       │   ├── splitting.py
│       │   └── validation.py
│       ├── io
│       │   ├── __init__.py
│       │   ├── datasets
│       │   │   ├── __init__.py
│       │   │   └── dataset1.py
│       │   ├── io.py
│       │   └── tables
│       │       ├── __init__.py
│       │       └── table1.py
│       ├── models
│       │   ├── __init__.py
│       │   ├── model1
│       │   │   ├── __init__.py
│       │   │   ├── dataloader.py
│       │   │   ├── hyperparameters_tuning.py
│       │   │   ├── metrics.py
│       │   │   ├── model.py
│       │   │   ├── predict.py
│       │   │   ├── preprocessing.py
│       │   │   └── train.py
│       │   └── schemas.py
│       ├── pipelines
│       │   ├── __init__.py
│       │   ├── flows
│       │   │   ├── __init__.py
│       │   │   ├── data
│       │   │   │   ├── __init__.py
│       │   │   │   ├── availability.py
│       │   │   │   ├── selection.py
│       │   │   │   ├── sourcing.py
│       │   │   │   └── synthesis.py
│       │   │   ├── data_engineering
│       │   │   │   ├── __init__.py
│       │   │   │   ├── cleaning.py
│       │   │   │   ├── exploration.py
│       │   │   │   └── features.py
│       │   │   ├── modeling
│       │   │   │   ├── __init__.py
│       │   │   │   ├── evaluation.py
│       │   │   │   ├── predict.py
│       │   │   │   ├── selection_features.py
│       │   │   │   ├── selection_model.py
│       │   │   │   ├── train.py
│       │   │   │   └── tuning.py
│       │   │   └── operationalizing
│       │   │       ├── __init__.py
│       │   │       ├── deployment.py
│       │   │       ├── monitoring.py
│       │   │       ├── registration.py
│       │   │       └── retraining.py
│       │   └── tasks
│       │       ├── __init__.py
│       │       ├── data.py
│       │       ├── data_engineering.py
│       │       ├── modeling.py
│       │       └── operationalizing.py
│       ├── schemas
│       │   ├── __init__.py
│       │   ├── datasets
│       │   │   ├── __init__.py
│       │   │   └── dataset1.py
│       │   └── tables
│       │       ├── __init__.py
│       │       └── table1.py
│       ├── settings.py
│       └── visualization
│           ├── __init__.py
│           ├── evaluation.py
│           └── exploration.py
├── tasks
│   ├── __init__.py
│   └── devops.py
├── tests
└── {{cookiecutter.repo_name}}.code-workspace
```

## Motivation

A project template that promotes good practices for reproducible data science while giving options for more or less complex projects.

Futhermore, this template allow me to create my own tool according to my daily needs, as for data science purpose as others.

This project is meant to adapt (and borrows liberally from) Driven Data's 
[cookicutter-data-science](https://drivendata.github.io/cookiecutter-data-science#keep-secrets-and-configuration-out-of-version-control) 
structure and philosophy to slightly different needs.


##  License

This project is distributed under the [MIT License](https://github.com/Jswig/cookiecutter-minimal-ml/blob/master/LICENSE).
