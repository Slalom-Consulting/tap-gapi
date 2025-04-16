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

"""
GAPI FINANACE COA STREAMS
"""
class FinanceCOACostCenterStream(gapiStream):
    """Define custom stream."""

    name = "costcenter"
    path = "/finance/chart-of-account/cost-center"
    primary_keys = ["costCenterId"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("costCenterId", th.StringType),
        th.Property("costCenterName", th.StringType),
        th.Property("legalEntityId", th.StringType),
        th.Property("geographyId", th.StringType),
        th.Property("organizationId", th.StringType),
        th.Property("departmentId", th.StringType),
        th.Property("functionType", th.StringType),
        th.Property("marketId", th.StringType),
        th.Property("marketName", th.StringType),
        th.Property("revenueEligibleFlag", th.BooleanType),
        th.Property("peopleEligibleFlag", th.BooleanType),
        th.Property("peopleAlignmentType", th.StringType),
        th.Property("effectiveStartDate", th.StringType),
        th.Property("effectiveEndDate", th.StringType),
        th.Property("creationDate", th.StringType),
        th.Property("lastUpdateDate", th.StringType),
        th.Property("functionId", th.StringType),
        th.Property("gtmMarketId", th.StringType),
        th.Property("gtmMarketName", th.StringType),
        th.Property("gtmCountryRegionId", th.StringType),
        th.Property("gtmCountryRegionName", th.StringType),
    ).to_dict()

class FinanceCOAFunctionStream(gapiStream):
    """Define custom stream."""

    name = "function"
    path = "/finance/chart-of-account/function"
    primary_keys = ["functionId"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("functionId", th.StringType),
        th.Property("functionName", th.StringType),
        th.Property("functionType", th.StringType),
        th.Property("functionHierarchy", th.StringType),
        th.Property("functionHierarchyLevel", th.StringType),
        th.Property("functionParentId", th.StringType),
        th.Property("peopleEligibleFlag", th.BooleanType),
        th.Property("revenueEligibleFlag", th.BooleanType),
        th.Property("postingAllowedFlag", th.BooleanType),
        th.Property("plAlignment", th.StringType),
        th.Property("effectiveStartDate", th.StringType),
        th.Property("effectiveEndDate", th.StringType),
        th.Property("creationDate", th.StringType),
        th.Property("lastUpdateDate", th.StringType),
        th.Property("utilizationEligible", th.BooleanType),
        th.Property("peopleAlignmentType", th.StringType),
        th.Property("workforceTaxonomyId", th.StringType),
    ).to_dict()

class FinanceCOAGeographyStream(gapiStream):
    """Define custom stream."""

    name = "geography"
    path = "/finance/chart-of-account/geography"
    primary_keys = ["geographyId"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("geographyId", th.StringType),
        th.Property("geographyName", th.StringType),
        th.Property("abbreviation", th.StringType),
        th.Property("geographyHierarchyLevel", th.StringType),
        th.Property("geographyType", th.StringType),
        th.Property("geographyParentId", th.StringType),
        th.Property("postingAllowedFlag", th.BooleanType),
        th.Property("effectiveStartDate", th.StringType),
        th.Property("effectiveEndDate", th.StringType),
        th.Property("creationDate", th.StringType),
        th.Property("lastUpdateDate", th.StringType),
    ).to_dict()

class FinanceCOALegalEntityStream(gapiStream):
    """Define custom stream."""

    name = "legalentity"
    path = "/finance/chart-of-account/legal-entity"
    primary_keys = ["legalEntityId"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("legalEntityName", th.StringType),
        th.Property(
            "legalEntityId",
            th.StringType,
            description="The legal entity's system ID",
        ),
        th.Property("legalEntityContractName", th.StringType),
        th.Property("legalEntityParentId", th.StringType),
        th.Property("legalEntityHierarchyLevel", th.StringType),
        th.Property("legalEntityType", th.StringType),
        th.Property("operationalEntity", th.StringType),
        th.Property("abbreviation", th.StringType),
        th.Property("postingAllowedFlag", th.BooleanType),
        th.Property("primaryCurrencyCode", th.StringType),
        th.Property("effectiveStartDate", th.StringType),
        th.Property("effectiveEndDate", th.StringType),
        th.Property("creationDate", th.StringType),
        th.Property("lastUpdateDate", th.StringType),
        th.Property("operationalStatus", th.StringType)
    ).to_dict()

class FinanceCOAOrganizationStream(gapiStream):
    """Define custom stream."""

    name = "organization"
    path = "/finance/chart-of-account/organization"
    primary_keys = ["organizationId"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("organizationName", th.StringType),
        th.Property(
            "organizationId",
            th.StringType,
            description="The organizations's system ID",
        ),
        th.Property(
            "abbreviation",
            th.StringType,
        ),
        th.Property("organizationHierarchyLevel", th.StringType),
        th.Property("organizationFunctionProfile", th.StringType),
        th.Property("organizationType", th.StringType),
        th.Property("organizationType2", th.StringType),
        th.Property("organizationParentId", th.StringType),
        th.Property("peopleEligibleFlag", th.BooleanType),
        th.Property("postingAllowedFlag", th.BooleanType),
        th.Property("effectiveStartDate", th.StringType),
        th.Property("effectiveEndDate", th.StringType),
        th.Property("creationDate", th.StringType),
        th.Property("lastUpdateDate", th.StringType),
    ).to_dict()



"""
GAPI BUSINESS STREAMS
"""
class BusinessTaxonomyMarketsStream(gapiStream):
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
            description="The Market's system ID",
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

class BusinessTaxonomyCapabilitiesStream(gapiStream):
    """Define custom stream."""

    name = "capabilities"
    path = "/business/taxonomy/capabilities?includeInactive=true"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property(
            "id",
            th.StringType,
            description="The Capability's system ID",
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

class BusinessTaxonomySubcapabilitiesStream(gapiStream):
    """Define custom stream."""

    name = "subcapabilities"
    path = "/business/taxonomy/subcapabilities?includeInactive=true"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property(
            "id",
            th.StringType,
            description="The Subcapability's system ID",
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

class BusinessTaxonomyGroupsStream(gapiStream):
    """Define custom stream."""

    name = "groups"
    path = "/business/taxonomy/groups?includeInactive=true"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property(
            "id",
            th.StringType,
            description="The group's system ID",
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

class BusinessTaxonomyTaxonomyTypesStream(gapiStream):
    """Define custom stream."""

    name = "taxonomy_types"
    path = "/business/taxonomy/types"
    primary_keys: t.ClassVar[list[str]] = ["enterpriseId"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("enterpriseId", th.StringType),
        th.Property("name", th.StringType),
        th.Property("idPrefix", th.StringType),
        th.Property("isActive", th.BooleanType),
        th.Property("url", th.StringType),
        th.Property("isWorkforceTaxonomy", th.BooleanType),
        th.Property("levelMax", th.IntegerType),
        th.Property("labelL1", th.StringType),
        th.Property("labelL2", th.StringType),
        th.Property("labelL3", th.StringType),
        th.Property("labelL4", th.StringType),
        th.Property("createdOn", th.DateTimeType),
        th.Property("createdBy", th.StringType),
        th.Property("modifiedOn", th.DateTimeType),
        th.Property("modifiedBy", th.StringType),
    ).to_dict()

class BusinessTaxonomyTaxonomyTypesCapabilities(gapiStream):
    """Define custom stream."""

    name = "taxonomy_types_capabilities"
    path = "/business/taxonomy/types/capabilities"
    primary_keys: t.ClassVar[list[str]] = ["enterpriseId"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("enterpriseId", th.StringType),
        th.Property("name", th.StringType),
        th.Property("isActive", th.BooleanType),
        th.Property("parentId", th.StringType),
        th.Property("levelNumber", th.IntegerType),
        th.Property("levelLabel", th.StringType),
        th.Property("maturity", th.StringType),
        th.Property("isRecruitingEligible", th.BooleanType),
        th.Property("isPeopleEligible", th.BooleanType),
        th.Property("isSalesEligible", th.BooleanType),
        th.Property("idL1", th.StringType),
        th.Property("idL2", th.StringType),
        th.Property("idL3", th.StringType),
        th.Property("idL4", th.StringType),
        th.Property("namePath", th.StringType),
        th.Property("createdBy", th.StringType),
        th.Property("createdOn", th.DateTimeType),
        th.Property("modifiedBy", th.StringType),
        th.Property("modifiedOn", th.DateTimeType),
    ).to_dict()

class BusinessTaxonomyTaxonomyTypesIndustriesStream(gapiStream):
    """Define custom stream."""

    name = "taxonomy_types_industries"
    path = "/business/taxonomy/types/industries"
    primary_keys: t.ClassVar[list[str]] = ["enterpriseId"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("enterpriseId", th.StringType),
        th.Property("name", th.StringType),
        th.Property("isActive", th.BooleanType),
        th.Property("parentId", th.StringType),
        th.Property("levelNumber", th.IntegerType),
        th.Property("levelLabel", th.StringType),
        th.Property("isRecruitingEligible", th.BooleanType),
        th.Property("isPeopleEligible", th.BooleanType),
        th.Property("isSalesEligible", th.BooleanType),
        th.Property("idL1", th.StringType),
        th.Property("idL2", th.StringType),
        th.Property("idL3", th.StringType),
        th.Property("idL4", th.StringType),
        th.Property("namePath", th.StringType),
        th.Property("createdBy", th.StringType),
        th.Property("createdOn", th.DateTimeType),
        th.Property("modifiedBy", th.StringType),
        th.Property("modifiedOn", th.DateTimeType),
    ).to_dict()

class BusinessTaxonomyTaxonomyTypesCustomerOutcomesStream(gapiStream):
    """Define custom stream."""

    name = "taxonomy_types_customer_outcomes"
    path = "/business/taxonomy/types/customer-outcomes"
    primary_keys: t.ClassVar[list[str]] = ["enterpriseId"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("enterpriseId", th.StringType),
        th.Property("name", th.StringType),
        th.Property("isActive", th.BooleanType),
        th.Property("parentId", th.StringType),
        th.Property("levelNumber", th.IntegerType),
        th.Property("levelLabel", th.StringType),
        th.Property("isRecruitingEligible", th.BooleanType),
        th.Property("isPeopleEligible", th.BooleanType),
        th.Property("isSalesEligible", th.BooleanType),
        th.Property("idL1", th.StringType),
        th.Property("idL2", th.StringType),
        th.Property("idL3", th.StringType),
        th.Property("idL4", th.StringType),
        th.Property("namePath", th.StringType),
        th.Property("createdBy", th.StringType),
        th.Property("createdOn", th.DateTimeType),
        th.Property("modifiedBy", th.StringType),
        th.Property("modifiedOn", th.DateTimeType),
    ).to_dict()

class BusinessTaxonomyTaxonomyTypesGoToMarketStream(gapiStream):
    """Define custom stream."""

    name = "taxonomy_types_go_to_market"
    path = "/business/taxonomy/types/go-to-market"
    primary_keys: t.ClassVar[list[str]] = ["enterpriseId"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("enterpriseId", th.StringType),
        th.Property("name", th.StringType),
        th.Property("isActive", th.BooleanType),
        th.Property("parentId", th.StringType),
        th.Property("levelNumber", th.IntegerType),
        th.Property("levelLabel", th.StringType),
        th.Property("isRecruitingEligible", th.BooleanType),
        th.Property("isPeopleEligible", th.BooleanType),
        th.Property("isSalesEligible", th.BooleanType),
        th.Property("idL1", th.StringType),
        th.Property("idL2", th.StringType),
        th.Property("idL3", th.StringType),
        th.Property("idL4", th.StringType),
        th.Property("namePath", th.StringType),
        th.Property("createdBy", th.StringType),
        th.Property("createdOn", th.DateTimeType),
        th.Property("modifiedBy", th.StringType),
        th.Property("modifiedOn", th.DateTimeType),
    ).to_dict()

class BusinessTaxonomyTaxonomyTypesSlalomGeographyStream(gapiStream):
    """Define stream for Slalom Geography taxonomy."""

    name = "taxonomy_types_slalom_geography"
    path = "/business/taxonomy/types/slalom-geography"
    primary_keys: t.ClassVar[list[str]] = ["enterpriseId"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("enterpriseId", th.StringType),
        th.Property("name", th.StringType),
        th.Property("nameShort", th.StringType),
        th.Property("parentId", th.StringType),
        th.Property("isActive", th.BooleanType),
        th.Property("isRecruitingEligible", th.BooleanType),
        th.Property("isSalesEligible", th.BooleanType),
        th.Property("isNearestLocationEligible", th.BooleanType),
        th.Property("levelNumber", th.IntegerType),
        th.Property("levelLabel", th.StringType),
        th.Property("namePath", th.StringType),
        th.Property("idL1", th.StringType),
        th.Property("idL2", th.StringType),
        th.Property("idL3", th.StringType),
        th.Property("idL4", th.StringType),
        th.Property("idL5", th.StringType),
        th.Property("idL6", th.StringType),
        th.Property("idL7", th.StringType),
        th.Property("idL8", th.StringType),
    ).to_dict()

