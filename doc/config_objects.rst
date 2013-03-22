The Config Object
==================

Confetti deals mostly with :class:`.Config` objects. These objects represent nodes and leaves in a configuration structure, and provide most of the functionality for querying and manipulating the configuration.

By default, parts of the configuration, even scalar values, are wrapped in Config objects when possible. However, Confetti provides ways to access values as simple Python values.

.. autoclass:: confetti.config.Config
   :members:
   :special-members:



