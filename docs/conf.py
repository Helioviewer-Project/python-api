"""
Configuration file for the Sphinx documentation builder.
"""
from datetime import datetime

# -- Project information -----------------------------------------------------
project = "hvpy"
author = "The Helioviewer Project"
copyright = f"{datetime.now().year}, {author}"
from hvpy import __version__

release = __version__

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.inheritance_diagram",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx_automodapi.automodapi",
    "sphinx_automodapi.smart_resolver",
    "sphinx_autodoc_typehints",
]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
source_suffix = ".rst"
master_doc = "index"
default_role = "obj"
# Enable nitpicky mode, which forces links to be non-broken
nitpicky = True
# This is not used. See docs/nitpick-exceptions file for the actual listing.
nitpick_ignore = []
for line in open("nitpick-exceptions"):
    if line.strip() == "" or line.startswith("#"):
        continue
    dtype, target = line.split(None, 1)
    target = target.strip()
    nitpick_ignore.append((dtype, target))

# -- Options for intersphinx extension -----------------------------------------
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/reference/", None),
    "matplotlib": ("https://matplotlib.org/stable", None),
    "aiapy": ("https://aiapy.readthedocs.io/en/stable/", None),
    "astropy": ("https://docs.astropy.org/en/stable/", None),
    "requests": ("https://requests.readthedocs.io/en/stable/", None),
}

# -- Options for HTML output ---------------------------------------------------
# The theme to use for HTML and HTML Help pages.
html_theme = "sphinx_book_theme"
html_theme_options = {
    "repository_url": "https://github.com/Helioviewer-Project/python-api/",
    "use_repository_button": True,
    "extra_navbar": "",
}
html_title = "hvpy"
