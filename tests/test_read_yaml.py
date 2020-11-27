import os

from metagraph.read_yaml import read_yaml

def test_read_yaml(testfile_path):

    entry_test_file = os.path.join(
        testfile_path, 'entry.yaml'
    )

    read_yaml(entry_test_file)

    assert 0