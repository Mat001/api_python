from unittest import TestLoader, TestSuite, TextTestRunner
from tests.demo import DemoApiTests
from tests.flow import ApiTests

if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(DemoApiTests),
        loader.loadTestsFromTestCase(ApiTests)))

    # run test sequentially using simple TextTestRunner
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)
