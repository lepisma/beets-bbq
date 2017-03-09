"""
Allow blackbird style search queries in beets
"""

from beets import config
from beets.dbcore.query import FieldQuery
from beets.plugins import BeetsPlugin


def get_bbq_patterns(pattern):
    """
    Return union and exception patterns
    """

    tokens = pattern.split(" ")

    bbq_patterns = []

    last_token = "+"
    in_range = True

    for idx, token in enumerate(tokens):
        if token == "+" or token == "-":
            last_token = token
            in_range = False
        else:
            if not in_range or idx == 0:
                bbq_patterns.append(last_token + token)
            else:
                bbq_patterns[-1] = bbq_patterns[-1] + " " + token

            in_range = True

    return bbq_patterns


def match_bbq_patterns(val, bbq_patterns, debug=False):
    """
    Return the final match verdict
    """

    matches = {"+": [], "-": []}

    for bbq_pattern in bbq_patterns:
        root = bbq_pattern[0]
        matches[root].append([w in val for w in bbq_pattern[1:].split(" ")])

    pos = [all(m) for m in matches["+"]]
    neg = [all(m) for m in matches["-"]]

    if debug:
        print(val, bbq_patterns, pos, neg)

    return any(pos) and not any(neg)


class BBQuery(FieldQuery):
    def __init__(self, field, pattern, fast=True):
        super().__init__(field, pattern, fast)

        # Search in these fields only
        self.search_fields = config["bbq"]["fields"].as_str_seq()

    def match(self, item):
        combined_fields = [item.get(f) for f in self.search_fields]
        combined_string = " ".join(combined_fields).lower()

        # Assuming clean queries as of now
        bbq_patterns = get_bbq_patterns(self.pattern.lower())
        return match_bbq_patterns(combined_string.lower(), bbq_patterns)


class BBQ(BeetsPlugin):
    def __init__(self):
        super().__init__()
        self.config.add({
            "prefix": "#",
            "fields": ["artist", "title", "album"]  # Default search fields
        })

    def queries(self):
        prefix = self.config["prefix"].as_str()
        return {prefix: BBQuery}
