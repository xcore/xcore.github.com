Xcore Open Source Repository Index
==================================

.. attention::

  Learn how to use an Xcore Github repository with our `XCore/Github howto <github_howto.html>`_

The XCore Open Source Project on GitHub is officially sponsored by
XMOS as a true open-source project. A number of the community members
are paid members of XMOS staff, while many others are simply excellent
volunteers who are interested in building quality stuff.

{% for group in groups %}

{{ group.title }}
-----------------

.. list-table::
  :header-rows: 1

  * - Repository
    - Description
{% for repo in group.repos %}
  * - `{{ repo.name }} <{{repo.name}}_readme.html>`_
    - {{ repo.description }}
{% endfor %}

{% endfor %}
