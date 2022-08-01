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

Building Documentation
----------------------

.. note::

    Building the documentation is not necessary unless you are
    writing new documentation or do not have internet access, because
    the latest versions of ``hvpy``'s documentation should be available
    at `hvpy.readthedocs.io <https://hvpy.readthedocs.io/>`__.

Dependencies
^^^^^^^^^^^^

Building the documentation requires the ``hvpy`` source code and some additional packages.
The easiest way to build the documentation is to use `tox <https://tox.readthedocs.io/en/latest/>`__ as detailed in :ref:`hvpy-doc-building`.

.. note::

    This does not include `Graphviz <http://www.graphviz.org>`__.
    If you do not install this package separately then the documentation build process will produce a very large number of lengthy warnings (which can obscure bona fide warnings) and also not generate inheritance graphs.

.. _hvpy-doc-building:

Building
^^^^^^^^

There are two ways to build the ``hvpy`` documentation. The easiest way is to
execute the following tox command (from the ``hvpy`` source directory)::

    tox -e build_docs

If you do this, you do not need to install any of the documentation dependencies
as this will be done automatically. The documentation will be built in the
``docs/_build/html`` directory, and can be read by pointing a web browser to
``docs/_build/html/index.html``.

Alternatively, you can do::

    cd docs
    make html

And the documentation will be generated in the same location. Note that
this uses the installed version of hvpy, so if you want to make sure
the current repository version is used, you will need to install it with
e.g.::

    pip install -e .[docs]

before changing to the ``docs`` directory.
