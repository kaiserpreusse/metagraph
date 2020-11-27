import yaml
from uuid import uuid4
from py2neo.ogm import Repository

from metagraph.model import Database, Ontology, Entity, Relation


def read_yaml(path: str, repo: Repository):
    """
    Read a yaml file containing database/ontology description.

    :param path:
    :return:
    """

    with open(path, 'r') as stream:
        entry = yaml.safe_load(stream)

    if entry['type'] == 'database':
        d = Database()
        d.name = entry['name']

        for entity_name in entry['entities']:
            e = Entity(entity_name)

            repo.save(e)

            d.contains.update(e)

        repo.save(d)

    elif entry['type'] == 'ontology':
        o = Ontology()
        o.name = entry['name']
        for entity_name in entry['entities']:
            e = Entity(entity_name)
            repo.save(e)

            o.describes.update(e)
        repo.save(o)

    # relations
    if 'relations' in entry:
        for relation in entry['relations']:
            r = Relation()
            r.uid = str(uuid4())

            to_entity = relation['to']
            from_entity = relation['from']

            r.connects.update(
                Entity(to_entity)
            )
            r.connects.update(
                Entity(from_entity)
            )
            repo.save(r)