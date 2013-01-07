# coding=utf-8
import unittest
# Runs all tests in the project.

if __name__ == "__main__":
    loader = unittest.TestLoader()
    tests = loader.discover('.')
    test_runner = unittest.runner.TextTestRunner()
    test_runner.run(tests)

