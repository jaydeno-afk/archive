"""Validation rules for manuscript records.

YOU IMPLEMENT THIS FILE.

Every validate_* function takes a raw string (exactly as it came out of the
CSV file) and returns a tuple:

    (True, "")              the value is trustworthy
    (False, "reason here")  the value is not, and here is why

The reason is a short human-readable string. The autograder checks the
boolean, not your exact wording — but a teammate reading your rejection log
should understand it, so write it for them.

READ THIS BEFORE YOU START
--------------------------
The year range is INCLUSIVE at both ends: 1100 and 1900 are VALID.
1099 and 1901 are not. Most marks lost in Part A are lost on that line.
"""

from archive.errors import MalformedRecordError  # noqa: F401  (you may not need it here)

KNOWN_CITIES = ["Timbuktu", "Djenne", "Gao", "Walata", "Chinguetti"]

VALID_CONDITIONS = ["fragile", "fair", "good"]

MIN_YEAR = 1100
MAX_YEAR = 1900


def validate_id(value):
    """An ID is the letters 'MS' followed by exactly three digits.

    Valid:   "MS001", "MS742"
    Invalid: "MS1", "MS0012", "ms001", "XX001", "", "MS00A"

    Returns (bool, str).
    """
    if len(value)!=5:
        return False, "wrong number of terms in ID"
    elif value[0]!='M' or value[1]!='S':
        return False, "wrong inital format of the ID"
    else:
        for i in range(2,5):
            if not value[i].isdigit():
                return False,"non digit in final 3 spaces for ID"
    return True,""


def validate_title(value):
    """A title must be present and at least 3 characters once stripped.

    Valid:   "Tarikh al-Sudan"
    Invalid: "", "   ", "Ab"

    Returns (bool, str).
    """
    value=value.strip()
    if len(value)<3:
        return False,"not enough characters in title"
    return True,""


def validate_city(value):
    """A city must be present and appear in KNOWN_CITIES.

    Comparison is case-insensitive: "timbuktu" is acceptable.
    "Kano" is not in our list, so it is rejected — and that is a real
    decision with a cost. Write about it in your README.

    Returns (bool, str).
    """
    raise NotImplementedError("validate_city")


def validate_year(value):
    """A year must be present, numeric, and between MIN_YEAR and MAX_YEAR
    INCLUSIVE.

    Valid:   "1655", "1100", "1900"
    Invalid: "", "   ", "c.1590", "sixteen fifty", "1099", "1901", "2087"

    Note that "2087" parses perfectly well as a number. It is still wrong.
    That is the whole point of a range check.

    Returns (bool, str).
    """
    raise NotImplementedError("validate_year")


def validate_condition(value):
    """A condition must be one of VALID_CONDITIONS, case-insensitively.

    Valid:   "fragile", "GOOD", "Fair"
    Invalid: "excellent", "", "ok"

    Returns (bool, str).
    """
    raise NotImplementedError("validate_condition")


def validate_record(record):
    """Validate a whole record dictionary.

    record is a dict with the keys: id, title, city, year, condition.

    Returns a LIST of reasons the record is invalid — one string per broken
    rule, in this field order: id, title, city, year, condition.
    An empty list means the record is valid.

    Do not re-write the rules here. Call the five functions above.
    """
    result=[]
    di=validate_id(record['id'])
    title=validate_title(record['title'])
    city=validate_city(record['city'])
    year=validate_year(record['year'])
    condition=validate_condition(record['condition'])
    checking=[di,title,city,year,condition]
    for item in checking:
        if not item[0]:
            result.append(item[1])
    return result


