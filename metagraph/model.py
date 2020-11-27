from py2neo.ogm import Model, Property, RelatedTo, RelatedFrom


class Database(Model):
    __primarykey__ = 'name'
    name = Property()

    contains = RelatedTo('Entity', 'CONTAINS')
    contains_relation = RelatedTo('Relation', '')


class Entity(Model):
    __primarykey__ = 'name'
    name = Property()

    contained_by = RelatedFrom('Database', 'CONTAINS')
    described_by = RelatedTo('Ontology', 'DESCRIBES')

    def __init__(self, name):
        self.name = name


class Ontology(Model):
    __primarykey__ = 'name'
    name = Property()

    describes = RelatedTo('Entity', 'DESCRIBES')


class Relation(Model):
    __primarykey__ = 'uid'
    uid = Property()

    connects = RelatedTo('Entity', 'CONNECTS')
