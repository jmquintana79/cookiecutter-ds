# Cookiecutter Flexible ML

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

`[Enter]` will select the default option in prompt.


## Generated project structure

Some of these might not be created depending on options picked
```
.
├── .env                <- Environemt variables.
├── .template_gitignore/<- Gitignore file template.
├── LICENSE
├── environment.yml /   <- File specifying an environment
|   requirements.txt   
├── README.md
├── run.py/Makefile     <- Script for running the full
|    /Snakefile          analysis.
│                        
├── data
|   ├── external        <- External datasets.
|   ├── interim         <- Intermediate data that has been transformed.
│   ├── processed       <- The final, canonical data sets for modeling. 
│   └── raw             <- The original, immutable data dump.
├── docs                <- Saved reference documents.
|   ├── web_references.md    <- List of references urls.
├── notebooks           <- Jupyter notebooks.
├── output              <- For outputs of running the analysis.
│   ├── models          <- Saved models and predictions.      
│   └── visualizations  <- Graphics created during analysis.       
├── reports             <- Generated analysis as HTML, PDF, LaTeX, etc.
└── src                 <- Source code for this project.
    ├── __init__.py     <- Makes this a Python module.
    ├── settings.py     <- Module to collect environment variables.
    ├── data                 <- Scripts to download or generate data.
    |   └── make_dataset.py  
    ├── features             <- Scripts to turn raw data into features for modeling.
    |   └── build_features.py  
    ├── models               <- Scripts used to generate models and inference results.
    └── visualization        <- Scripts to generate graphics.
        └── visualize.py
```    

## Motivation

A project template that promotes good practices for reproducible 
data science (immutablity of raw data, seperation of exploratory code and 
"final" analysis code), while giving options for more or less complex projects.

 - A python script is used by default for workflow automation instead of
  a `Makefile` (though it is left as an option) to avoid issues for Windows 
  users. `snakemake` is preferred for "real" projects.
 - The template does not include boilerplate for generating documentation or 
 python packages, which is not necessary for the intended use case of personal
 /classroom projects.

Futhermore, this template allow me to create my own tool according to 
my daily needs, as for data science purpose as others.

This project is meant to adapt (and borrows liberally from) Driven Data's 
[cookicutter-data-science](https://drivendata.github.io/cookiecutter-data-science#keep-secrets-and-configuration-out-of-version-control) 
structure and philosophy to slightly different needs.


##  License

This project is distributed under the [MIT License](https://github.com/Jswig/cookiecutter-minimal-ml/blob/master/LICENSE).
