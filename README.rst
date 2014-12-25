Scrapy Random User-Agent
========================

Does your scrapy spider get identified and blocked by servers because
you use the default user-agent or a generic one?

Use this ``random_useragent`` module and set a random user-agent for
every request. You are limited only by the number of different
user-agents you set in a text file.

Installing
----------

Installing it is pretty simple.

.. code-block:: python

    pip install scrapy-random-useragent

Usage
-----

In your ``settings.py`` file, update the ``DOWNLOADER_MIDDLEWARES``
variable like this.

.. code-block:: python

    DOWNLOADER_MIDDLEWARES = {
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
        'random_useragent.RandomUserAgentMiddleware': 400
    }

This disables the default ``UserAgentMiddleware`` and enables the
``RandomUserAgentMiddleware``.

Then, create a new variable ``USER_AGENT_LIST`` with the path to your
text file which has the list of all user-agents
(one user-agent per line).

.. code-block:: python

    USER_AGENT_LIST = "/path/to/useragents.txt"

Now all the requests from your crawler will have a random user-agent
picked from the text file.
