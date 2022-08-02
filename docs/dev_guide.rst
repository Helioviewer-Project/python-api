.. _dev_guide:

*****************
Developer's Guide
*****************

Developers who wish to contribute to this package can fork the main `GitHub repository <https://github.com/Helioviewer-Project/python-api>`__.

.. note::
    When you install the dependencies, you need to install the development version of the package.
    See the :ref:`obtaining_the_source` section for details.

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

There are two ways to build the ``hvpy`` documentation.
The easiest way is to execute the following tox command (from the ``hvpy`` source directory)::

    tox -e build_docs

If you do this, you do not need to install any of the documentation dependencies as this will be done automatically.
The documentation will be built in the ``docs/_build/html`` directory, and can be read by pointing a web browser to ``docs/_build/html/index.html``.

Alternatively, you can do::

    cd docs
    make html

And the documentation will be generated in the same location.
Note that this uses the installed version of ``hvpy``, so if you want to make sure the current repository version is used, you will need to install it with::

    pip install -e ".[docs]"

before changing to the ``docs`` directory.

Testing Guidelines
------------------

This section describes how to test the ``hvpy`` package.
The testing framework used by ``hvpy`` is the `pytest <https://docs.pytest.org/>`__ framework.

.. _running-tests:

Running Tests
^^^^^^^^^^^^^

There are currently two different ways to invoke ``hvpy`` tests.
Each method invokes `pytest`_ to run the tests but offers different options when calling.
To run the tests, you will need to make sure you have the `pytest`_ package installed.

``tox``
=======

The most robust way to run the tests (which can also be the slowest) is to make use of `Tox <https://tox.readthedocs.io/en/latest/>`__, which is a general purpose tool for automating Python testing.
One of the benefits of ``tox`` is that it first creates a source distribution of the package being tested, and installs it into a new virtual environment, along with any dependencies that are declared in the package, before running the tests.
This can therefore catch issues related to undeclared package data, or missing dependencies.
Since we use tox to run many of the tests on continuous integration services, it can also be used in many cases to reproduce issues seen on those services.

To run the tests with ``tox``, first make sure that ``tox`` is installed, e.g.::

    pip install tox

You can see a list of available test environments with::

    tox -l -v

which will also explain what each of them does.

You can also run checks or commands not directly related to tests - for instance::

    tox -e codestyle

will run checks on the code style using precommit hooks.

``pytest``
==========

The test suite can also be run directly from the native ``pytest`` command, which is generally faster than using tox for iterative development.
In this case, it is important for developers to be aware that they must manually rebuild any extensions by running::

    pip install -e ".[test]"

before running the test with pytest with::

    pytest

To run all the test in the ``hvpy`` package, you can use::

    pytest -c hvpy

you can also run specific test functions with::

    pytest -c hvpy -k test_function
