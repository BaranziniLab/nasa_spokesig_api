from unittest import TestCase
from nasa_api.app import app


class ContextManagerTestCase(TestCase):
    """Adds enter(context) to TestCase, allowing us to enter a context manager
    (e.g. patch(...)) and have it cleaned up after the test runs, even if
    it errors.
    """
    
    def start(self, manager):
        """Basically, enter a *with* statement that terminates
        on test cleanup.
        Calls manager.__enter__(), registers manager.__exit__ as a cleanup
        action, and returns the context returned by manager.__enter__().
        """
        context = manager.__enter__()
        self.addCleanup(lambda: manager.__exit__(None, None, None))
        return context
    
    
class FlaskTestCase(ContextManagerTestCase):
    def setUp(self):
        super().setUp()
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.start(self.app.test_client())