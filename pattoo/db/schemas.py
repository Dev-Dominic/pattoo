#!/usr/bin/env python3
"""pattoo ORM Schema classes.

Used for defining GraphQL interaction

Based on the pages at:

    https://github.com/alexisrolland/flask-graphene-sqlalchemy/wiki/Flask-Graphene-SQLAlchemy-Tutorial
    https://docs.graphene-python.org/projects/sqlalchemy/en/latest/tutorial/

"""
# PIP3 imports
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

# pattoo imports
from .filters import PattooFilterableConnectionField
from pattoo.db.models import (
        Data as DataTable,
        Pair as PairTable,
        DataPoint as DataPointTable,
        Glue as GlueTable,
        Language as LanguageTable,
        PairXlateGroup as PairXlateGroupTable,
        PairXlate as PairXlateTable,
        AgentGroup as AgentGroupTable,
        Agent as AgentTable
    )


def resolve_checksum(obj, _):
    """Convert 'checksum' from bytes to string."""
    return obj.checksum.decode()


def resolve_key(obj, _):
    """Convert 'key' from bytes to string."""
    return obj.key.decode()


def resolve_value(obj, _):
    """Convert 'value' from bytes to string."""
    return obj.value.decode()


def resolve_description(obj, _):
    """Convert 'description' from bytes to string."""
    return obj.description.decode()


def resolve_agent_id(obj, _):
    """Convert 'agent_id' from bytes to string."""
    return obj.agent_id.decode()


def resolve_agent_program(obj, _):
    """Convert 'agent_program' from bytes to string."""
    return obj.agent_program.decode()


def resolve_agent_polled_target(obj, _):
    """Convert 'agent_polled_target' from bytes to string."""
    return obj.agent_polled_target.decode()

def resolve_code(obj, _):
    """Convert 'code' from bytes to string."""
    return obj.code.decode()


class DataAttribute(object):
    """Descriptive attributes of the Data table.

    A generic class to mutualize description of attributes for both queries
    and mutations.

    """

    idx_datapoint = graphene.String(
        description='DataPoint index. (ForeignKey)')

    timestamp = graphene.String(
        description='Data collection timestamp.')

    value = graphene.String(
        description='Data value.')


class Data(SQLAlchemyObjectType, DataAttribute):
    """Data node."""

    class Meta:
        """Define the metadata."""

        model = DataTable
        interfaces = (graphene.relay.Node,)


class DataConnections(relay.Connection):
    """GraphQL / SQlAlchemy Connection to the Data table."""

    class Meta:
        """Define the metadata."""

        node = Data


class PairAttribute(object):
    """Descriptive attributes of the Pair table.

    A generic class to mutualize description of attributes for both queries
    and mutations.

    """

    idx_pair = graphene.String(
        description='Pair index.')

    key = graphene.String(
        resolver=resolve_key,
        description='Key-value pair key.')

    value = graphene.String(
        resolver=resolve_value,
        description='Key-value pair value.')


class Pair(SQLAlchemyObjectType, PairAttribute):
    """Pair node."""

    class Meta:
        """Define the metadata."""

        model = PairTable
        interfaces = (graphene.relay.Node,)


class PairConnections(relay.Connection):
    """GraphQL / SQlAlchemy Connection to the Pair table."""

    class Meta:
        """Define the metadata."""

        node = Pair


class DataPointAttribute(object):
    """Descriptive attributes of the DataPoint table.

    A generic class to mutualize description of attributes for both queries
    and mutations.

    """

    idx_datapoint = graphene.String(
        description='DataPoint index.')

    idx_agent = graphene.String(
        description='Agent table index. (ForeignKey)')

    checksum = graphene.String(
        resolver=resolve_checksum,
        description='Unique DataPoint checksum.')

    data_type = graphene.String(
        description=(
            'Type of data, (String, Integer, Float, Counter, Counter64)'))

    last_timestamp = graphene.String(
        description=('''\
Timestamp when the Data table was last updated for this datapoint.'''))

    polling_interval = graphene.String(
        description='Updating interval in milliseconds for the datapoint.')

    enabled = graphene.String(
        description='True if the DataPoint is enabled.')


class DataPoint(SQLAlchemyObjectType, DataPointAttribute):
    """DataPoint node."""

    class Meta:
        """Define the metadata."""

        model = DataPointTable
        interfaces = (graphene.relay.Node,)


class DataPointConnections(relay.Connection):
    """GraphQL / SQlAlchemy Connection to the DataPoint table."""

    class Meta:
        """Define the metadata."""

        node = DataPoint


class GlueAttribute(object):
    """Descriptive attributes of the Glue table.

    A generic class to mutualize description of attributes for both queries
    and mutations.

    """

    idx_pair = graphene.String(
        description='Pair table index. (ForeignKey)')

    idx_datapoint = graphene.String(
        description='DataPoint table index. (ForeignKey)')


class Glue(SQLAlchemyObjectType, GlueAttribute):
    """Glue node."""

    class Meta:
        """Define the metadata."""

        model = GlueTable
        interfaces = (graphene.relay.Node,)


class GlueConnections(relay.Connection):
    """GraphQL / SQlAlchemy Connection to the Glue table."""

    class Meta:
        """Define the metadata."""

        node = Glue


class LanguageAttribute(object):
    """Descriptive attributes of the Language table.

    A generic class to mutualize description of attributes for both queries
    and mutations.

    """

    idx_language = graphene.String(
        description='Language table index.')

    code = graphene.String(
        resolver=resolve_code,
        description='Language code.')

    description = graphene.String(
        resolver=resolve_description,
        description='Description for language code.')


class Language(SQLAlchemyObjectType, LanguageAttribute):
    """Language node."""

    class Meta:
        """Define the metadata."""

        model = LanguageTable
        interfaces = (graphene.relay.Node,)


class LanguageConnections(relay.Connection):
    """GraphQL / SQlAlchemy Connection to the Language table."""

    class Meta:
        """Define the metadata."""

        node = Language


class PairXlateGroupAttribute(object):
    """Descriptive attributes of the PairXlateGroup table.

    A generic class to mutualize description of attributes for both queries
    and mutations.

    """

    idx_pair_xlate_group = graphene.String(
        description='PairXlateGroup table index.')

    description = graphene.String(
        resolver=resolve_description,
        description='Description for language code.')

    enabled = graphene.String(
        description='"True" if the group is enabled.')


class PairXlateGroup(SQLAlchemyObjectType, PairXlateGroupAttribute):
    """PairXlateGroup node."""

    class Meta:
        """Define the metadata."""

        model = PairXlateGroupTable
        interfaces = (graphene.relay.Node,)


class PairXlateGroupConnections(relay.Connection):
    """GraphQL / SQlAlchemy Connection to the PairXlateGroup table."""

    class Meta:
        """Define the metadata."""

        node = PairXlateGroup


class PairXlateAttribute(object):
    """Descriptive attributes of the PairXlate table.

    A generic class to mutualize description of attributes for both queries
    and mutations.

    """

    idx_pair_xlate_group = graphene.String(
        description='PairXlateGroup table index (ForeignKey).')

    idx_language = graphene.String(
        description='Language table index (ForeignKey).')

    key = graphene.String(
        resolver=resolve_key,
        description=('''\
Key-pair key. Part of a composite primary key with "idx_language" and \
"idx_pair_xlate_group"'''))

    description = graphene.String(
        resolver=resolve_description,
        description='Description for for the Key-pair key.')


class PairXlate(SQLAlchemyObjectType, PairXlateAttribute):
    """PairXlate node."""

    class Meta:
        """Define the metadata."""

        model = PairXlateTable
        interfaces = (graphene.relay.Node,)


class PairXlateConnections(relay.Connection):
    """GraphQL / SQlAlchemy Connection to the PairXlate table."""

    class Meta:
        """Define the metadata."""

        node = PairXlate


class AgentGroupAttribute(object):
    """Descriptive attributes of the AgentGroup table.

    A generic class to mutualize description of attributes for both queries
    and mutations.

    """

    idx_agent_group = graphene.String(
        description='AgentGroup table index.')

    idx_pair_xlate_group = graphene.String(
        description='PairXlateGroup table index (ForeignKey).')

    description = graphene.String(
        resolver=resolve_description,
        description='Description of the AgentGroup.')

    enabled = graphene.String(
        description='"True" if the group is enabled.')


class AgentGroup(SQLAlchemyObjectType, AgentGroupAttribute):
    """AgentGroup node."""

    class Meta:
        """Define the metadata."""

        model = AgentGroupTable
        interfaces = (graphene.relay.Node,)


class AgentGroupConnections(relay.Connection):
    """GraphQL / SQlAlchemy Connection to the AgentGroup table."""

    class Meta:
        """Define the metadata."""

        node = AgentGroup


class AgentAttribute(object):
    """Descriptive attributes of the Agent table.

    A generic class to mutualize description of attributes for both queries
    and mutations.

    """

    idx_agent = graphene.String(
        description='Agent table index.')

    idx_agent_group = graphene.String(
        description='AgentGroup table index. (ForeignKey)')

    agent_id = graphene.String(
        resolver=resolve_agent_id,
        description='Agent identifier.')

    agent_polled_target = graphene.String(
        resolver=resolve_agent_polled_target,
        description='Source of the Agent\'s data')

    agent_program = graphene.String(
        resolver=resolve_agent_program,
        description='Name of the Agent program that retrieved the data.')

    enabled = graphene.String(
        description='"True" if the Agent is enabled.')


class Agent(SQLAlchemyObjectType, AgentAttribute):
    """Agent node."""

    class Meta:
        """Define the metadata."""

        model = AgentTable
        interfaces = (graphene.relay.Node,)


class AgentConnections(relay.Connection):
    """GraphQL / SQlAlchemy Connection to the Agent table."""

    class Meta:
        """Define the metadata."""

        node = Agent


class Query(graphene.ObjectType):
    """Define GraphQL queries."""

    node = relay.Node.Field()

    glue = graphene.relay.Node.Field(Glue)
    all_glues = SQLAlchemyConnectionField(GlueConnections)

    datapoint = graphene.relay.Node.Field(DataPoint)
    all_datapoints = SQLAlchemyConnectionField(DataPointConnections)

    pair = graphene.relay.Node.Field(Pair)
    all_pairs = SQLAlchemyConnectionField(PairConnections)

    data = graphene.relay.Node.Field(Data)
    all_data = SQLAlchemyConnectionField(DataConnections)

    language = graphene.relay.Node.Field(Language)
    all_language = SQLAlchemyConnectionField(LanguageConnections)

    pairxlategroup = graphene.relay.Node.Field(PairXlateGroup)
    all_pairxlategroup = SQLAlchemyConnectionField(PairXlateGroupConnections)

    pairxlate = graphene.relay.Node.Field(PairXlate)
    all_pairxlate = PattooFilterableConnectionField(PairXlateConnections)

    agentgroup = graphene.relay.Node.Field(AgentGroup)
    all_agentgroup = SQLAlchemyConnectionField(AgentGroupConnections)

    agent = graphene.relay.Node.Field(Agent)
    all_agent = SQLAlchemyConnectionField(AgentConnections)


# Make the schema global
SCHEMA = graphene.Schema(query=Query)
