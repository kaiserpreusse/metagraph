import pytest
import os

@pytest.fixture(scope='session')
def testfile_path():
    return os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'testfiles')