"""Provide constant values of the meta-model."""

# This code has been automatically generated by aas-core-codegen.
# Do NOT edit or append.

from typing import Set

import aas_core3_1.types as aas_types

#: Enumeration of all identifiable elements within an asset administration shell.
GENERIC_FRAGMENT_KEYS: Set[aas_types.KeyTypes] = {
    aas_types.KeyTypes.FRAGMENT_REFERENCE
}

#: Enumeration of different key value types within a key.
GENERIC_GLOBALLY_IDENTIFIABLES: Set[aas_types.KeyTypes] = {
    aas_types.KeyTypes.GLOBAL_REFERENCE
}

#: Enumeration of different key value types within a key.
AAS_IDENTIFIABLES: Set[aas_types.KeyTypes] = {
    aas_types.KeyTypes.ASSET_ADMINISTRATION_SHELL,
    aas_types.KeyTypes.CONCEPT_DESCRIPTION,
    aas_types.KeyTypes.IDENTIFIABLE,
    aas_types.KeyTypes.SUBMODEL
}

#: Enumeration of all submodel elements within an asset administration shell.
AAS_SUBMODEL_ELEMENTS_AS_KEYS: Set[aas_types.KeyTypes] = {
    aas_types.KeyTypes.ANNOTATED_RELATIONSHIP_ELEMENT,
    aas_types.KeyTypes.BASIC_EVENT_ELEMENT,
    aas_types.KeyTypes.BLOB,
    aas_types.KeyTypes.CAPABILITY,
    aas_types.KeyTypes.DATA_ELEMENT,
    aas_types.KeyTypes.ENTITY,
    aas_types.KeyTypes.EVENT_ELEMENT,
    aas_types.KeyTypes.FILE,
    aas_types.KeyTypes.MULTI_LANGUAGE_PROPERTY,
    aas_types.KeyTypes.OPERATION,
    aas_types.KeyTypes.PROPERTY,
    aas_types.KeyTypes.RANGE,
    aas_types.KeyTypes.REFERENCE_ELEMENT,
    aas_types.KeyTypes.RELATIONSHIP_ELEMENT,
    aas_types.KeyTypes.SUBMODEL_ELEMENT,
    aas_types.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
    aas_types.KeyTypes.SUBMODEL_ELEMENT_LIST
}

#: Enumeration of different fragment key value types within a key.
AAS_REFERABLE_NON_IDENTIFIABLES: Set[aas_types.KeyTypes] = {
    aas_types.KeyTypes.ANNOTATED_RELATIONSHIP_ELEMENT,
    aas_types.KeyTypes.BASIC_EVENT_ELEMENT,
    aas_types.KeyTypes.BLOB,
    aas_types.KeyTypes.CAPABILITY,
    aas_types.KeyTypes.DATA_ELEMENT,
    aas_types.KeyTypes.ENTITY,
    aas_types.KeyTypes.EVENT_ELEMENT,
    aas_types.KeyTypes.FILE,
    aas_types.KeyTypes.MULTI_LANGUAGE_PROPERTY,
    aas_types.KeyTypes.OPERATION,
    aas_types.KeyTypes.PROPERTY,
    aas_types.KeyTypes.RANGE,
    aas_types.KeyTypes.REFERENCE_ELEMENT,
    aas_types.KeyTypes.RELATIONSHIP_ELEMENT,
    aas_types.KeyTypes.SUBMODEL_ELEMENT,
    aas_types.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
    aas_types.KeyTypes.SUBMODEL_ELEMENT_LIST
}

#: Enumeration of referables. We need this to check that model references refer to a Referable. For example, the observed attribute of the Basic Event Element object must be a model reference to a Referable.
AAS_REFERABLES: Set[aas_types.KeyTypes] = {
    aas_types.KeyTypes.ASSET_ADMINISTRATION_SHELL,
    aas_types.KeyTypes.CONCEPT_DESCRIPTION,
    aas_types.KeyTypes.IDENTIFIABLE,
    aas_types.KeyTypes.SUBMODEL,
    aas_types.KeyTypes.ANNOTATED_RELATIONSHIP_ELEMENT,
    aas_types.KeyTypes.BASIC_EVENT_ELEMENT,
    aas_types.KeyTypes.BLOB,
    aas_types.KeyTypes.CAPABILITY,
    aas_types.KeyTypes.DATA_ELEMENT,
    aas_types.KeyTypes.ENTITY,
    aas_types.KeyTypes.EVENT_ELEMENT,
    aas_types.KeyTypes.FILE,
    aas_types.KeyTypes.MULTI_LANGUAGE_PROPERTY,
    aas_types.KeyTypes.OPERATION,
    aas_types.KeyTypes.PROPERTY,
    aas_types.KeyTypes.RANGE,
    aas_types.KeyTypes.REFERENCE_ELEMENT,
    aas_types.KeyTypes.REFERABLE,
    aas_types.KeyTypes.RELATIONSHIP_ELEMENT,
    aas_types.KeyTypes.SUBMODEL_ELEMENT,
    aas_types.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
    aas_types.KeyTypes.SUBMODEL_ELEMENT_LIST
}

#: Enumeration of all referable elements within an asset administration shell
GLOBALLY_IDENTIFIABLES: Set[aas_types.KeyTypes] = {
    aas_types.KeyTypes.GLOBAL_REFERENCE,
    aas_types.KeyTypes.ASSET_ADMINISTRATION_SHELL,
    aas_types.KeyTypes.CONCEPT_DESCRIPTION,
    aas_types.KeyTypes.IDENTIFIABLE,
    aas_types.KeyTypes.SUBMODEL
}

#: Enumeration of different key value types within a key.
FRAGMENT_KEYS: Set[aas_types.KeyTypes] = {
    aas_types.KeyTypes.ANNOTATED_RELATIONSHIP_ELEMENT,
    aas_types.KeyTypes.BASIC_EVENT_ELEMENT,
    aas_types.KeyTypes.BLOB,
    aas_types.KeyTypes.CAPABILITY,
    aas_types.KeyTypes.DATA_ELEMENT,
    aas_types.KeyTypes.ENTITY,
    aas_types.KeyTypes.EVENT_ELEMENT,
    aas_types.KeyTypes.FILE,
    aas_types.KeyTypes.FRAGMENT_REFERENCE,
    aas_types.KeyTypes.MULTI_LANGUAGE_PROPERTY,
    aas_types.KeyTypes.OPERATION,
    aas_types.KeyTypes.PROPERTY,
    aas_types.KeyTypes.RANGE,
    aas_types.KeyTypes.REFERENCE_ELEMENT,
    aas_types.KeyTypes.RELATIONSHIP_ELEMENT,
    aas_types.KeyTypes.SUBMODEL_ELEMENT,
    aas_types.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
    aas_types.KeyTypes.SUBMODEL_ELEMENT_LIST
}

#: IEC 61360 data types for concept descriptions categorized with PROPERTY or VALUE.
DATA_TYPE_IEC_61360_FOR_PROPERTY_OR_VALUE: Set[aas_types.DataTypeIEC61360] = {
    aas_types.DataTypeIEC61360.DATE,
    aas_types.DataTypeIEC61360.STRING,
    aas_types.DataTypeIEC61360.STRING_TRANSLATABLE,
    aas_types.DataTypeIEC61360.INTEGER_MEASURE,
    aas_types.DataTypeIEC61360.INTEGER_COUNT,
    aas_types.DataTypeIEC61360.INTEGER_CURRENCY,
    aas_types.DataTypeIEC61360.REAL_MEASURE,
    aas_types.DataTypeIEC61360.REAL_COUNT,
    aas_types.DataTypeIEC61360.REAL_CURRENCY,
    aas_types.DataTypeIEC61360.BOOLEAN,
    aas_types.DataTypeIEC61360.RATIONAL,
    aas_types.DataTypeIEC61360.RATIONAL_MEASURE,
    aas_types.DataTypeIEC61360.TIME,
    aas_types.DataTypeIEC61360.TIMESTAMP
}

#: IEC 61360 data types for concept descriptions categorized with REFERENCE.
DATA_TYPE_IEC_61360_FOR_REFERENCE: Set[aas_types.DataTypeIEC61360] = {
    aas_types.DataTypeIEC61360.STRING,
    aas_types.DataTypeIEC61360.IRI,
    aas_types.DataTypeIEC61360.IRDI
}

#: IEC 61360 data types for concept descriptions categorized with DOCUMENT.
DATA_TYPE_IEC_61360_FOR_DOCUMENT: Set[aas_types.DataTypeIEC61360] = {
    aas_types.DataTypeIEC61360.FILE,
    aas_types.DataTypeIEC61360.BLOB,
    aas_types.DataTypeIEC61360.HTML
}

#: These data types imply that the unit is defined in the data specification.
IEC_61360_DATA_TYPES_WITH_UNIT: Set[aas_types.DataTypeIEC61360] = {
    aas_types.DataTypeIEC61360.INTEGER_MEASURE,
    aas_types.DataTypeIEC61360.REAL_MEASURE,
    aas_types.DataTypeIEC61360.RATIONAL_MEASURE,
    aas_types.DataTypeIEC61360.INTEGER_CURRENCY,
    aas_types.DataTypeIEC61360.REAL_CURRENCY
}

# This code has been automatically generated by aas-core-codegen.
# Do NOT edit or append.
