from django.test.simple import DjangoTestSuiteRunner
from django.conf import settings

EXCLUDED_APPS = getattr(settings, 'TEST_EXCLUDE', [])

class ExcludeTestSuiteRunner(DjangoTestSuiteRunner):
    
    def build_suite(self, *args, **kwargs):
        suite = super(ExcludeTestSuiteRunner, self).build_suite(*args, **kwargs)
        tests = []
        for case in suite:
            pkg = case.__class__.__module__
            add_tests_from_suite = True
            for app in EXCLUDED_APPS:
                if pkg.startswith(app):
                    add_tests_from_suite = False
            if add_tests_from_suite:
                tests.append(case)
        suite._tests = tests 
        return suite
