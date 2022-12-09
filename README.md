## Cookiecutter Python Project Template

This is a `cookiecutter` Python project template that you can use to create new projects.

### Prerequisites
* Python 3.8+
* `cookiecutter` that can be installed with `pip` or `conda`

```
$ pip install cookiecutter
# or
$ conda config --add channels conda-forge
$ conda install cookiecutter
```

### Create new project
```
cookiecutter https://github.com/dinhuun/python_project_template.git
project_name: name of your project, Enter
project_slug: Enter
author_name: author name, Enter
description: description, Enter
open_source_license: 1/2/3, Enter
python_interpreter: 1/2/3, Enter
```
and a new project `project_slug` will be created in current directory.

It will look like this
```
project_slug               <- top level
├── .flake8
├── .gitignore
├── .mypy.ini
├── LICENSE
├── Makefile               <- Makefile with commands like `make env` or `make lint`
├── README.md              <- README for this project
├── VERSION                <- version for semantic versioning
├── requirements.txt       <- code requirements
├── requirements_dev.txt   <- development requirements
├── setup.py               <- makes project pip installable, such as `pip install -e .` so that src can be imported
├── data                   <- data
├── notebooks              <- jupyter notebooks
├── src                    <- source code
    ├── __init__.py        <- makes src a Python module
    └── project_slug       <- where modules are
        ├── hello.py       <- module hello
        └── __init__.py
└── tests                  <- tests
    ├── __init__.py        <- makes tests a Python module
    ├── integration        <- integration tests to test that internal parts and external parts collectively work
    └── unit               <- unit tests to test that internal parts individually work
        ├── test_hello.py  <- tests for module hello
        └── __init__.py
```