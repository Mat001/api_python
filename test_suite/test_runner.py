from unittest import TestLoader, TestSuite, TextTestRunner
from tests.fake_rest_api import ApiTests
from tests.salesforce import Salesforce

if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(ApiTests),
        loader.loadTestsFromTestCase(Salesforce)))

    # run test sequentially using simple TextTestRunner
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)
