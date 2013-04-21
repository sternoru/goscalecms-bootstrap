GoScale CMS bootstrap template
==============================

This is a template project for `GoScale CMS <http://goscalecms.com>`_ (`GitHub repository <https://github.com/sternoru/goscalecms>`_).

If you start your Django project from this template you'll have a boostraped ready to go CMS installation that you can immediately run and build your project based on!

Credits
-------

* `GoScale CMS <http://goscalecms.com>`_
* Product of `Sterno.Ru <http://sterno.ru/en/>`_.
* Developed and maintained under supervision of `Evgeny Demchenko <https://github.com/littlepea>`_

How to install
--------------
::

    django-admin.py startproject --template=https://github.com/sternoru/goscalecms-bootstrap/archive/master.zip --extension=py,md,rst project_name
    cd project_name
    pip install -r requirements.txt
    fab bootstrap

Change `project_name` to your actual project name.

You're good to go!
Run it like any other Django project or use fabric shortcut::

    fab run
