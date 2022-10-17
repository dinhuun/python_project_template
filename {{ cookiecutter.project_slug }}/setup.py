import re

from setuptools import find_packages, setup


VERSION_RE = re.compile(r"""([0-9dev.]+)""")
EDITABLE_INSTALL_RE = re.compile(r"""^-e\s+(.+)""")


def get_version():
    with open("VERSION", "r") as fh:
        init = fh.read().strip()
    return VERSION_RE.search(init).group(1)


def requirement_specification(requirements_line):
    """
    extracts requirement from a line in requirements.txt
    :param requirements_line:
    :return: requirement
    """
    editable_requirement = EDITABLE_INSTALL_RE.match(requirements_line)
    if editable_requirement is None:
        return requirements_line.strip()
    else:
        path = editable_requirement.group(1)
        return path.split("/")[-1]


def get_requirements():
    with open("requirements.txt", "r") as f:
        lines = f.read().splitlines()
    return [requirement_specification(line) for line in lines]


setup(
    author="{{ cookiecutter.author_name }}",
    author_email="to be disclosed",
    description="{{ cookiecutter.description }}",
    include_package_data=True,
    install_requires=get_requirements(),
    license="{% if cookiecutter.open_source_license == 'MIT' %}MIT{% elif cookiecutter.open_source_license == 'BSD - "
            "3 - Clause' %}BSD-3{% endif %}",
    name="{{ cookiecutter.project_slug }}",
    packages=find_packages("src"),
    package_data={"{{ cookiecutter.project_slug }}": ["VERSION", "requirements.txt", "MANIFEST.in"]},
    package_dir={"": "src"},
    url="to be determined",
    version=get_version(),
)
