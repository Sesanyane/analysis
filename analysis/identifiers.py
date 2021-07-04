from edc_identifier.simple_identifier import SimpleUniqueIdentifier


class HouseholdIdentifier(SimpleUniqueIdentifier):

    random_string_length = 5
    identifier_type = 'household_identifier'
    template = 'H{device_id}{random_string}'
