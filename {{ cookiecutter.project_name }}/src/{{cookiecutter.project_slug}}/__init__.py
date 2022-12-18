"""
project metadata that user can access
>>> import {{cookiecutter.project_slug}}
>>> {{cookiecutter.project_slug}}.author
>>> ...
>>> {{cookiecutter.project_slug}}.version
>>> {{cookiecutter.project_slug}}.__version__
"""

import importlib.metadata


metadata = importlib.metadata.metadata("{{cookiecutter.project_slug}}")
author = metadata["author"]
description = summary = metadata["summary"]
email = metadata["author-email"]
name = metadata["name"]
url = metadata["home-page"]
version = __version__ = metadata["version"]
