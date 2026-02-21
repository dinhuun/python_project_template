## Cookiecutter Python Project Template

This is a `cookiecutter` Python project template that you can use to create new projects.

### Prerequisites
* Python 3.13+
* `cookiecutter` that can be installed with `pip` or `conda`

```
$ pip install cookiecutter
# or
$ conda config --add channels conda-forge
$ conda install cookiecutter
```

### Create new project
```
cookiecutter https://github.com/dinhuun/python_project_template.git  # or python_project_template if cloned to local
project_name: your project name, Enter
project_slug: your project slug, Enter
author_name: author name, Enter
author_email: author email, Enter
description: description, Enter
open_source_license: 1/2/3, Enter
```
and a new project `project_slug` will be created in current directory.

It will look like this
```
project_name               <- top level
├── data                   <- data
├── notebooks              <- jupyter notebooks
├── src                    <- source code
    └── project_slug       <- where modules are
        ├── hello.py       <- module hello
        └── __init__.py
└── tests                  <- tests
    ├── integration        <- integration tests to test that internal parts and external parts collectively work
    └── unit               <- unit tests to test that internal parts individually work
        ├── test_hello.py  <- tests for module hello
        └── __init__.py
├── .gitignore
├── Makefile               <- Makefile with commands like `make env` or `make lint`
├── pyproject.toml         <- makes project pip installable, such as `pip install -e .` so that src can be imported
├── README.md              <- README for this project
```