.. container:: download

  .. raw:: html

     <a
     onClick="window.open('https://github.com/xcore/{{repo.name}}/zipball/master');window.focus();return true;" href="{{repo.name}}_master_download.html">Download the latest master branch snapshot</a>

{% for tag in repo.tags %}
.. container:: download

  .. raw:: html

     <a onClick="window.open('https://github.com/xcore/{{repo.name}}/zipball/{{tag.name}}');window.focus();return true;" href="{{repo.name}}_{{tag.name}}_download.html">Download version {{ tag.version }}</a>

{% endfor %}


`Visit the repository Github page <http://github.com/xcore/{{repo.name}}>`_

`Go to repository index <index.html>`_


