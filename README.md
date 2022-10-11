## Cookiecutter Python Project Template

A template for Python projects

Requirements to use this cookiecutter template
-----------
 - Python 3.8+
 - `cookiecutter>= 1.4.0` that can be installed with `pip` or `conda`

``` bash
$ pip install cookiecutter
# or
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


To start a new project, run:
------------

    cookiecutter https://github.com/dinhuun/python_project_template.git

## The resulting directory structure

Your new project will look like this: 

```
├── .flake8
├── .gitignore
├── .mypy.ini
├── LICENSE
├── Makefile               <- Makefile with commands like `make env` or `make lint`
├── README.md              <- README for this project
├── VERSION
├── requirements.txt       <- code requirements
├── requirements_dev.txt   <- development requirements
├── setup.py               <- makes project pip installable, such as `pip install -e .` so that src can be imported
├── notebooks              <- jupyter notebooks
├── src                    <- source code
    ├── __init__.py        <- makes src a Python module
    └── project_name       <- where modules are
        ├── core.py        <- module core
        └── __init__.py
└── tests                  <- tests
    ├── __init__.py        <- makes tests a Python module
    └── unit               <- unit tests
        ├── test_core.py   <- tests for module core
        └── __init__.py
```