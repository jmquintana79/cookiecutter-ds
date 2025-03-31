# {{ cookiecutter.name }}

{% if cookiecutter.user == "" -%}
*{{ cookiecutter.author_name }}, {% now 'local', '%d/%m/%Y' %}*
{%- else -%}
*{{ cookiecutter.user }}, {% now 'local', '%d/%m/%Y' %}*
{%- endif %}

{{ cookiecutter.description }}

## Setup



## Project structure
```
{% if cookiecutter.license != "No license file" -%}
├── LICENSE
{%- endif %}
├── README.md                <- The top-level README
├── data
|   ├── interim              <- Intermediate data that has been transformed.
│   ├── processed            <- The final, canonical data sets for modeling.
│   └── raw                  <- The original, immutable data dump.
├── notebooks                <- Jupyter notebooks.
├── output             
|   ├── models               <- Serialized models, predictions, model summaries.
|   └── visualization        <- Graphics created during analysis.
└── src                      <- Source code for this project.
{%- if cookiecutter.src_structure == "Less" %}
    └── __init__.py          <- Makes this a python module.
{%- elif cookiecutter.src_structure == "More" %}
    ├── __init__.py          <- Makes this a python module.
    ├── data                 <- Scripts to download or generate data.
    |   └── make_dataset.py  
    ├── features             <- Scripts to turn raw data into features for modeling.
    |   └── build_features.py  
    ├── models               <- Scripts used to generate models and inference results.
    └── visualization        <- Scripts to generate graphics.
        └── visualize.py
{%- endif %}
```
    
{% if cookiecutter.license != "No license file" -%}
## License

This project is distributed under the  {{ cookiecutter.license }} license.
{%- endif %}