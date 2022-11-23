## {{cookiecutter.project_slug}}
This package
* does this
* does that

### Prerequisites
Python 3.9

### Requirements
see `requirements.txt` and `requirements_dev.txt`

### Usage
example:
```sh
$ cd {{cookiecutter.project_slug}}
{{cookiecutter.project_slug}} $ make env
{{cookiecutter.project_slug}} $ source env/bin/activate
(env) {{cookiecutter.project_slug}} $ python src/{{cookiecutter.project_slug}}/hello.py
(env) {{cookiecutter.project_slug}} $ pytest tests/unit/test_hello.py
(env) {{cookiecutter.project_slug}} $ python
>>> from {{cookiecutter.project_slug}}.hello import hello
>>> print(hello("{{cookiecutter.author_name}}"))
```

### Tests
see `tests/unit/` and `tests/integration`
