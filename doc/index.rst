.. Confetti documentation master file, created by
   sphinx-quickstart on Fri Mar 22 23:33:10 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Confetti
========

Confetti deals mostly with :class:`.Config` objects. These objects represent nodes and leaves in a configuration structure, and provide most of the functionality for querying and manipulating the configuration.

By default, parts of the configuration, even scalar values, are wrapped in Config objects when possible. However, Confetti provides ways to access values as simple Python values.

Basic Operations
~~~~~~~~~~~~~~~~

Initializing Configurations
---------------------------

The most convenient way to initialize a configuration structure is by simply passing a nested dictionary into the :class:`.Config` constructor::

  from confetti import Config
  CONFIG = Config({
      "a" : {
          "b" : 2,
      }
  })

Confetti also has convenience helpers to load from files that contain the above structure (NB the capital ``CONFIG``), via the :func:`.Config.from_filename`, :func:`.Config.from_file` and :func:`.Config.from_string` methods.

Querying the Configuration Tree
-------------------------------

The simplest and most memorizable way to access values in the configuration structure is through the ``root`` member of the Config object. This member is a proxy to the Config object and allows accessing values through attributes::

  >>> from confetti import Config
  >>> c = Config({
  ...   "a" : {"b" : {"c" : 12}},
  ... })
  >>> c.root.a.b.c
  12

You can also use ``__getitem__`` syntax (as in Python dicts) to access nodes and values::

  >>> c["a"]["b"]["c"]
  12

Modifying Configurations
------------------------

Existing Values
+++++++++++++++

Existing values can be changed pretty easily, both by using the ``root`` proxy, and by using ``__setitem__``::

  >>> c["a"]["b"]["c"] = 100
  >>> c.root.a.b.c = 100

New Values and Nodes
++++++++++++++++++++

To avoid mistakes when using or updating configurations, Confetti does not allow setting nonexistent values::

 >>> c["new_value"] = 1 # doctest: +IGNORE_EXCEPTION_DETAIL
 Traceback (most recent call last):
    ...
 CannotSetValue: ...

Configuration objects have the :func:`.Config.extend` method to assign new values or nested structures to an existing configuration, that does the trick:

 >>> c.extend({"new_value" : 1})
 >>> c.root.new_value
 1

Advanced Uses
~~~~~~~~~~~~~

Cross References
----------------

In many cases you want to set a single value in your configuration, and have other leaves take it by default. Instead of repeating yourself like so::

 >>> cfg = Config(dict(
 ...     my_value = 1337,
 ...     value_1 = 1337,
 ...     x = dict(
 ...         y = dict(
 ...             z = 1337,
 ...         )
 ...     )
 ... ))

You can do this:

 >>> from confetti import Ref
 >>> cfg = Config(dict(
 ...     my_value = 1337,
 ...     value_1 = Ref(".my_value"),
 ...     x = dict(
 ...         y = dict(
 ...             z = Ref("...my_value"),
 ...         )
 ...     )
 ... ))
 >>> cfg.root.x.y.z
 1337

Or you can apply a custom filter to the reference, to create derived values::

 >>> cfg = Config(dict(
 ...     my_value = 1337,
 ...     value_1 = Ref(".my_value", filter="I am {0}".format),
 ... ))
 >>> cfg.root.value_1
 'I am 1337'


The confetti.config.Config Class
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: confetti.config.Config
   :members:
   :special-members:






Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

