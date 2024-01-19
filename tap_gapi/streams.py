"""Stream type classes for tap-gapi."""

from __future__ import annotations

import sys
import typing as t

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_gapi.client import gapiStream

if sys.version_info >= (3, 9):
    import importlib.resources as importlib_resources
else:
    import importlib_resources

class MarketsStream(gapiStream):
    """Define custom stream."""

    name = "markets"
    path = "/business/taxonomy/markets?includeInactive=true"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("name", th.StringType),
        th.Property(
            "id",
            th.StringType,
            description="The Markets's system ID",
        ),
        th.Property(
            "abbreviation",
            th.StringType,
        ),
        th.Property(
            "active",
            th.BooleanType,
        ),
        th.Property("peopleTagAdministrators", th.ArrayType(th.StringType)),
        th.Property("type", th.StringType),
        th.Property(
            "leader",
            th.StringType,
        ),
        th.Property("supportedApplications", th.ArrayType(th.StringType)),
        th.Property("createdBy", th.StringType),
        th.Property("createdOn", th.DateTimeType),
        th.Property("modifiedBy", th.StringType),
        th.Property("modifiedOn", th.DateTimeType),
    ).to_dict()

class CapabilitiesStream(gapiStream):
    """Define custom stream."""

    name = "capabilities"
    path = "/business/taxonomy/capabilities?includeInactive=true"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property(
            "id",
            th.StringType,
            description="The Markets's system ID",
        ),
        th.Property(
            "name",
            th.StringType,
        ),
        th.Property(
            "active",
            th.BooleanType,
        ),
        th.Property("subcapabilities", th.ArrayType(th.StringType)),
        th.Property("createdBy", th.StringType),
        th.Property("createdOn", th.DateTimeType),
        th.Property("modifiedBy", th.StringType),
        th.Property("modifiedOn", th.DateTimeType),
    ).to_dict()

class SubcapabilitiesStream(gapiStream):
    """Define custom stream."""

    name = "subcapabilities"
    path = "/business/taxonomy/subcapabilities?includeInactive=true"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property(
            "id",
            th.StringType,
            description="The Markets's system ID",
        ),
        th.Property(
            "name",
            th.StringType,
        ),
        th.Property(
            "active",
            th.BooleanType,
        ),
        th.Property("groups", th.ArrayType(th.StringType)),
        th.Property("createdBy", th.StringType),
        th.Property("createdOn", th.DateTimeType),
        th.Property("modifiedBy", th.StringType),
        th.Property("modifiedOn", th.DateTimeType),
    ).to_dict()

class GroupsStream(gapiStream):
    """Define custom stream."""

    name = "groups"
    path = "/business/taxonomy/groups?includeInactive=true"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property(
            "id",
            th.StringType,
            description="The Markets's system ID",
        ),
        th.Property(
            "name",
            th.StringType,
        ),
        th.Property(
            "active",
            th.BooleanType,
        ),
        th.Property("createdBy", th.StringType),
        th.Property("createdOn", th.DateTimeType),
        th.Property("modifiedBy", th.StringType),
        th.Property("modifiedOn", th.DateTimeType),
    ).to_dict()