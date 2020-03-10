#!/usr/bin/env python3

import unittest

NBDIR = './'

Test = testipynb.TestNotebooks(directory=NBDIR, timeout=21000)
TestNotebooks = Test.get_tests()

if __name__ == "__main__":
    unittest.main()
