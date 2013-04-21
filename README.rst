`GoScale CMS bootstrap template <https://github.com/sternoru/goscalecms-bootstrap#readme>`_
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

Change `project_name` to your actual project name.

1. Create a project from template
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    django-admin.py startproject --template=https://github.com/sternoru/goscalecms-bootstrap/archive/master.zip --extension=py,md,rst project_name
    cd project_name
    
2. Create a virtual environment (if not already created)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I suggest to use virtualenv or, even better, `virtualenvwrapper <http://virtualenvwrapper.readthedocs.org/en/latest/install.html#installation>`_ for managing requirements::

    # Create an environment if you have virtualenvwrapper installed
    mkvirtualenv project_env

3. Install requirements and bootstrap the project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    pip install -r requirements.txt
    fab bootstrap
    
4. Run it!
^^^^^^^^^^

You're good to go!
Run it like any other Django project or use fabric shortcut::

    fab run
    
This template comes with a pre-created superuser: admin/123, so you can quickly login to the django admin interface.
It also has fixtures with some pages and plugins + twitter bootstrap theme to quick start the front-end.

5. Keep rolling
^^^^^^^^^^^^^^^

To run your project later you just need to activate the virtualenv from the project directory::

    # if you're using virtualenvwrapper
    cd project_name
    workon project_env
    fab run
    
Screenshot of the succesfull installation
-----------------------------------------

.. image:: http://www.clipular.com/c?5069109=EEszsxZ23KG_TLB9A9ZnYQ3bRjY&f=.png

