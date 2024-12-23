# -- Project information -----------------------------------------------------
project = 'custom_api_client'
copyright = '2024, Zirui-Wang'
author = 'Zirui-Wang'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx_rtd_theme',  # This enables the Read the Docs theme
    'sphinx.ext.autodoc',  # Enables automatic documentation generation from docstrings
    'sphinx.ext.viewcode',  # Enables the 'View Source' link in the documentation
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'  # Use the RTD theme
html_static_path = ['_static']
