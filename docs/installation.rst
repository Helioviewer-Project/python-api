.. _installation:

************
Installation
************

Installing ``hvpy``
-------------------

If you are new to Python and/or do not have familiarity with `Python virtual environments <https://docs.python.org/3/tutorial/venv.html>`_, then we recommend starting by installing the `Anaconda Distribution <https://www.anaconda.com/distribution/>`_. This works on all platforms (linux, Mac, Windows) and installs a full-featured Python environment in your user directory without requiring root privileges.

Using pip
---------
.. warning::

    Users of the Anaconda Python distribution should follow the instructions
    for :ref:`anaconda_install`.

To install ``hvpy`` with `pip <https://pip.pypa.io/en/stable/>`_, run::

    pip install hvpy

.. _anaconda_install:

Using Conda
-----------

To install ``hvpy`` using `conda <https://docs.conda.io/projects/conda/en/latest//>`_ run::

    conda install hvpy

Requirements
------------

``hvpy`` has the following requirements:

- `requests <https://requests.readthedocs.io/en/latest/>`_ >=2.27.0 or higher
- `pydantic <https://pydantic-docs.helpmanual.io/>`_ >=1.9.1 or higher

Obtaining the Source Packages
-----------------------------

Source Packages
^^^^^^^^^^^^^^^

The latest stable source package for ``hvpy`` can be `downloaded here
<https://pypi.org/project/hvpy>`_.

Development Repository
^^^^^^^^^^^^^^^^^^^^^^

The latest development version of ``hvpy`` can be cloned from GitHub
using this command::

   git clone git@github.com:Helioviewer-Project/python-api.git

Building and Installing
^^^^^^^^^^^^^^^^^^^^^^^

To build and install ``hvpy`` (from the root of the source tree)::

    pip install -e .

which installs ``hvpy`` in develop mode -- this then means that
changes in the code are immediately reflected in the installed version.


Building Documentation
----------------------

Todo: add documentation for building documentation

"""
