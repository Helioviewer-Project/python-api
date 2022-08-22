**********
User Guide
**********

Welcome to ``hvpy``!

This guide provides a walkthrough of the major features in the ``hvpy`` package.
``hvpy`` is a python wrapper for the `Helioviewer API <https://api.helioviewer.org/docs/v2/>`_.
This is the same API that powers `helioviewer.org <https://helioviewer.org>`_.

Basic Usage
-----------
Each API endpoint has a function in ``hvpy`` that shares the same name and has
the same input parameters. So, for example if you are looking at
`getJP2Image <https://api.helioviewer.org/docs/v2/api/api_groups/jpeg2000.html#getjp2image>`_
in the Helioviewer documentation, you would execute this in ``hvpy`` with
the following command

.. code-block:: Python

    import hvpy
    from hvpy.datasources import DataSources
    from datetime import datetime

    jp2 = hvpy.getJP2Image(datetime.now(), DataSources.AIA_94.value)

Managing Return Types
---------------------
``hvpy`` will attempt to coerce the result into a Python datatype
for you. In general, there are 3 types of results you can expect
from the API

1. Raw Data
2. Strings
3. JSON

In ``hvpy`` these return types map to

1. bytearray
2. str
3. dict

Sometimes the return type will change dependending on the input parameters
you specify, so make sure to review your input parameters carefully.
The descriptions in both our :ref:`api-reference` and the `API Docs <https://api.helioviewer.org/docs/v2/>`_
will say whether certain parameters change the output type

Helper Functions
----------------
``hvpy`` provides a few helper functions for certain actions that generally
require multiple API reqeusts, or for actions that may require more work
than a simple API call.

Helper Flows
^^^^^^^^^^^^
For example, creating a movie requires
calling `hvpy.queueMovie` followed by `hvpy.getMovieStatus` to see
if the movie is done, and then calling `hvpy.downloadMovie` to get
the result. ``hvpy`` provides some helper functions to perform these flows
for you. (TODO: Update ref)

Datasource & Event Selection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Some API requests accept a list of datasources and events. These
are in a very specific format. For example layering an AIA_94 image
over an AIA_304 image would look like "[13,1,50],[8,1,50]". Since
our API provides a one to one mapping, you would have to go figure out
how helioviewer likes its layer strings, and find the IDs for
each source.

``hvpy`` makes this easy by providing a function for you. hvpy.util.create_layers (TODO: update ref) will
create the datasources for you, you simply specify a tuple with the source enum you
want, and the opacity it should be in the image.

.. code-block:: Python

    from hvpy.util import create_layers
    from hvpy.datasources import DataSources
    layer_string = create_layers([(DataSources.AIA_304, 50), (DataSources.AIA_94, 50)]
    # layer_string = [13,1,50],[8,1,50]

There is a similar function for choosing events that you want to have displayed
in hvpy.util.create_events (TODO: Update ref)

Miscellaneous Helpers
^^^^^^^^^^^^^^^^^^^^^
``hvpy`` also provides some miscellaneous helper functions.
For example, since many API endpoints return raw data like images or videos,
we've implemented a simple save_file (TODO: Update ref) to save
this binary data to disk.

