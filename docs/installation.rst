.. _installation:

************
Installation
************

Installing ``hvpy``
-------------------

If you are new to Python and/or do not have familiarity with `Python virtual environments <https://docs.python.org/3/tutorial/venv.html>`__, then we recommend starting by installing `mini-forge <https://github.com/conda-forge/miniforge#miniforge3>`__.
This works on all platforms (Linux, Mac, Windows) and installs a full-featured Python environment in your user directory without requiring root privileges.

Using pip
---------

.. warning::

    Users of any conda distribution should follow the instructions for :ref:`conda_install`.

To install ``hvpy`` with `pip <https://pip.pypa.io/en/stable/>`__, run ::

    pip install hvpy

.. _conda_install:

Using Conda
-----------

To install ``hvpy`` using `conda <https://docs.conda.io/projects/conda/en/latest/>`__ run ::

    conda install -c conda-forge hvpy

Obtaining the Source Package
----------------------------

Source Package
^^^^^^^^^^^^^^

The latest stable source package for ``hvpy`` can be `downloaded at pypi.org <https://pypi.org/project/hvpy>`__.

Development Repository
^^^^^^^^^^^^^^^^^^^^^^

The latest development version of ``hvpy`` can be cloned from `GitHub <https://github.com/Helioviewer-Project/python-api/>`__ ::

   git clone git@github.com:Helioviewer-Project/python-api.git

Building and Installing
^^^^^^^^^^^^^^^^^^^^^^^

To build and install ``hvpy`` (from the root of the source tree) ::

    pip install -e .

which installs ``hvpy`` in development mode, this means that a change in the source code is immediately reflected.
