from distutils.core import setup

setup(
    name='django-test-exclude',
    license='LICENSE.txt',
    version='0.1.0',
    author='Karol Majta',
    author_email='karolmajta@gmail.com',
    description='Easy application excludes for django projects',
    
    requires=['Django (>=1.3.0)'],

    packages=['django_test_exclude'],
    package_dir={
        'ks_ads_authdownloads': 'django_test_exclude',
    },
)
