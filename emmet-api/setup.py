# -*- coding: utf-8 -*-
from setuptools import find_namespace_packages, setup

setup(
    name="emmet-api",
    use_scm_version={"root": "..", "relative_to": __file__},
    setup_requires=["setuptools_scm"],
    description="Emmet API Library",
    author="The Materials Project",
    author_email="feedback@materialsproject.org",
    url="https://github.com/materialsproject/emmet",
    packages=find_namespace_packages(include=["emmet.*"]),
    install_requires=[
        "emmet-core[all]",
        "fastapi",
        "uvicorn-tschaume",
        "gunicorn",
        "boto3",
        "maggma",
        "ddtrace",
        "setproctitle",
        "shapely",
    ],
    extras_require={
        "test": [
            "pre-commit",
            "pytest",
            "pytest-cov",
            "pycodestyle",
            "pydocstyle",
            "flake8",
            "mypy",
            "mypy-extensions",
            "types-setuptools",
            "types-requests",
            "wincertstore",
            "openbabel"
        ],
        "docs": [
            "mkdocs",
            "mkdocs-material<8.3",
            "mkdocs-material-extensions",
            "mkdocs-minify-plugin",
            "mkdocstrings",
            "mkdocs-awesome-pages-plugin",
            "mkdocs-markdownextradata-plugin",
            "mkdocstrings[python]",
            "livereload",
            "jinja2",
        ]
    },
    python_requires=">=3.8",
    license="modified BSD",
    zip_safe=False,
)
