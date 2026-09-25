# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CURQ Documentation'
copyright = '2026, Manfred'
author = 'Manfred'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

locale_dirs = ["../locale/"]
gettext_compact = False

language = "en"

# -- Multiversion -------------------------------------------------

smv_branch_whitelist = r"^(16\.0|17\.0|18\.0|19\.0|main)$"
smv_remote_whitelist = r"^origin$"

# Optional: mark the latest version
smv_latest_version = "19.0"
