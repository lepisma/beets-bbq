beets-bbq
=========

.. image:: https://img.shields.io/pypi/v/beets-bbq.svg
  :target: https://pypi.python.org/pypi/beets-bbq

`blackbird
<https://github.com/lepisma/blackbird>`_ style search query plugin for `beets
<https://github.com/beetbox/beets>`_.

Prepend queries with ``#`` and play around with ``+``, ``-`` and spaces.

.. code-block:: bash

   → beet ls '#swift - 1989 + beach house'
   → beet play '#evanescence + within temptation'

Install
-------

``pip install beets-bbq``

Optional ``beets.yaml`` configuration:

.. code-block:: yaml

   bbq:
       fields: <beets db fields to combine>
