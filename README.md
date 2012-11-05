django-test-exclude
====================

Rationale
---------

List apps that you want to exclude when running `manage.py test`.

Django-nose test runner allows to skip tests for applications that are listed
in `INSTALLED_APPS`, but are not present in your Django project's directory.
However if you prefer to store *your own* apps on the `PYTHONPATH` instead of
inside your project's directory, they will also be skipped and this well...
sucks.

Sometimes tests from a third party app installed installed in your
`PYTHONPATH` fail for no reason, making output of `manage.py test` noisy
 and this, well... sucks. 

Django-test-exclude is a one-file solution. Just list the packages
you want to skip during testing and voilla!

Installation
------------

### Using pip

	$ pip install django-test-exclude

### Living on the edge

	$ git clone https://github.com/lolek09/django-test-exclude.git

Configuration
-------------

Just add to your `settings.py`:

	TEST_RUNNER = 'django_test_exclude.runners.ExcludeTestSuiteRunner'
	TEST_EXCLUDE = (
		'app1',
		'app2',
	)

Use cases
---------

Skipping whole Django test suite:

	TEST_EXCLUDE = (
		'django.contrib',
	)

Skipping parts of Django test suite:

	TEST_EXCLUDE = (
		'django.contrib.messages',
		'django.contrib.sessions',
	)

Skipping some third party apps or their subpackages:

	TESTS_EXCLUDE = (
		'some_app1',
		'some_app2.subpackage',
	)

Happy coding!
