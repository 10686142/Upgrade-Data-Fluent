===================================
Unit Testing
===================================


I have started implementing Unit Tests in the main repository,
to make my codebase more maintanable. Implemeting these tests makes sure
that I don't accidentally create new errors in the same module or other
modules by changes I have implemented.

This is especially usefull due to the large size of the project and
all the different moving parts.


Main Repo's Structure
=================================

::

    data_fluent_core
    ├── Pipfile
    ├── Pipfile.lock
    ├── accounts
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── templates
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── cc_templates
    │   ├── detail_only
    │   ├── list_detail
    │   └── list_only
    ├── companies
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── templates
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── data_fluent_core
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── api.py
    │   ├── make_css_urls_absolute.py
    │   ├── selenium_click_extract_html.py
    │   ├── settings.py
    │   ├── templates
    │   ├── urls.py
    │   └── wsgi.py
    ├── drivers
    │   └── chromedriver
    ├── manage.py
    ├── projects
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── api.py
    │   ├── api_permissions.py
    │   ├── api_scrapy.py
    │   ├── apps.py
    │   ├── choices.py
    │   ├── city_files
    │   ├── custom_fields.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── serializers.py
    │   ├── templates
    │   ├── templatetags
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── proxy_manager
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── check_port_in_use.py
    │   ├── management
    │   ├── models.py
    │   ├── old_code
    │   ├── proxies
    │   ├── tests.py
    │   └── views.py
    ├── re2
    │   ├── AUTHORS
    │   ├── BUILD
    │   ├── CMakeLists.txt
    │   .................
    ├── react_helper
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── helpers.py
    │   ├── management
    │   ├── server_check.py
    │   ├── templates
    │   └── templatetags
    ├── scrapy_app
    │       ├── __init__.py
    │       ├── __pycache__
    │       │   ├── __init__.cpython-36.pyc
    │       │   ├── pipelines.cpython-36.pyc
    │       │   └── settings.cpython-36.pyc
    │       ├── adblock
    │       │   ├── adblock_rules.py
    │       │   └── easylist_adblock_rules.txt
    │       ├── helpers
    │       ├── items.py
    │       ├── lua_scripts
    │       │   ├── __init__.py
    │       │   ├── click_and_wait_cookie.py
    │       │   ├── click_and_wait_pagination.py
    │       │   └── wait_for_element.py
    │       ├── middlewares.py
    │       ├── pipelines.py
    │       ├── proxy_middlewares.py
    │       └── settings.py
    ................


Current Status
=================================

I have not been able to fully implement all the testing I want, due to
the large size of the main repository and the time I had to finish this
project along with all the other parts.
