# THESE ARE INCORRECT:
#####################################################################
FAC_DESC:STREET_HIGHWAY -> FAC_DESC:HIGHWAY_STREET
PRODCUT:OTHER -> PRODUCT:OTHER
FAC:HOTEL -> ORGANIZATION:HOTEL
DATE -> DATE:DATE   [wsj06c.qa]
LOCATION -> LOCATION:OTHER # 5 mentions (districts)

######################################################################
# 13 more types removed.

# There were too few (< 20) of the following entity types,
# so they were changed as follows:

CONTACT_INFO:OTHER -> O     #  3 mentions
SUBSTANCE:NUCLEAR -> O # 3 mentions
CONTACT_INFO:ADDRESS -> O   #  4 mentions

LOCATION:BORDER -> LOCATION:OTHER # 1 mention
LOCATION:CITY -> GPE:CITY # 1 mention

ORGANIZATION:STATE_PROVINCE -> GPE:CITY # 1 mention
ORGANIZATION:CITY -> GPE:CITY # 2 mentions

QUANTITY:TEMPERATURE -> QUANTITY:OTHER # 1 mention
QUANTITY:SPEED -> QUANTITY:OTHER # 14 mentions
QUANTITY:ENERGY -> QUANTITY:OTHER # 20 mentions, but 3 of them are incorrect
                                  # (kilobytes and megabytes).

PRODUCT:FOOD -> PRODUCT:OTHER # 1 mention
PRODUCT:DRUG -> SUBSTANCE:DRUG # 2 mentions

WORK_OF_ART:PAINTING -> WORK_OF_ART:OTHER # 13 mentions


