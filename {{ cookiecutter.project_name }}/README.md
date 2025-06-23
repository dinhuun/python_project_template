## {{cookiecutter.project_slug}}
This package
* does this
* does that

### Prerequisites
Python 3.12+

### Requirements
see `requirements.txt` and `requirements_dev.txt`

### Usage
example:
```sh
$ cd {{cookiecutter.project_name}}
{{cookiecutter.project_name}} $ make env
{{cookiecutter.project_name}} $ source env/bin/activate
(env) {{cookiecutter.project_name}} $ python src/{{cookiecutter.project_slug}}/hello.py
(env) {{cookiecutter.project_name}} $ pytest tests/unit/test_hello.py
(env) {{cookiecutter.project_name}} $ python
>>> from {{cookiecutter.project_slug}}.hello import hello
>>> print(hello("{{cookiecutter.author_name}}"))
```

### Tests
see `tests/unit/` and `tests/integration`
