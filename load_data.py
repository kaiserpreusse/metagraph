import os
import logging
from py2neo.ogm import Repository

from metagraph.read_yaml import read_yaml

logging.basicConfig(level=logging.DEBUG)
logging.getLogger('py2neo.client.bolt').setLevel(logging.WARNING)
logging.getLogger('py2neo.client').setLevel(logging.WARNING)


log = logging.getLogger(__name__)


repo = Repository(host='localhost', user='neo4j', password='test', name='metagraph')


datafiles = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

for file in os.listdir(datafiles):
    filepath = os.path.join(datafiles, file)
    log.info(filepath)

    read_yaml(filepath, repo)