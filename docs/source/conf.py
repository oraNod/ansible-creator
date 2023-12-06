"""The ansible-creator Documentation builder source."""

# pylint: disable=redefined-builtin,invalid-name

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os # noqa: ERA001
# import sys    # noqa: ERA001
# sys.path.insert(0, os.path.abspath('.'))  # noqa: ERA001

# -- Project information -----------------------------------------------------

project = "Ansible Creator"
copyright = "2023, Ansible"  # noqa: A001   # pylint: disable=redefined-builtin
author = "Ansible"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    "sphinx.ext.duration",
    "sphinx_ansible_theme",
]

myst_enable_extensions = [
    "attrs_inline",
]

autosectionlabel_prefix_document = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_ansible_theme"  # pylint: disable=invalid-name
html_title = "Ansible Creator Documentation"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_theme_options = {
    "display_version": False,
    "titles_only": False,
    "documentation_home_url": "https://ansible-creator.readthedocs.io/en/latest/",
}