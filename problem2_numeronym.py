"""
In software engineering, two common shorthand abbreviations that people often use are
"a11y" to represent "accessibility" and "i18n" to represent "internationalization".
The numnbers in the shorthand simply represent a number of letters ("accessibility"
is "a" then 11 letters then "y").

You can imagine this being extrapolated into a generic text matching system, where a
number in a pattern represents that number of letters in a string. For example, the
string "technology" would be matched by all of the following patterns:

- t8y (t-echnolog-y)
- t9 (t-echnology)
- 9y (technolog-y)
- tech2logy (tech-no-logy)
- 8g1 (technolo-g-y)
- te2n4y (te-ch-n-olog-y)

 and many others! Note that these patterns match many other strings as well. However,
 the word "technology" would not be matched by the pattern t9y, for example, because
 "technology" has 10 letters and "t9y" would only match 11-letter strings that start
 with "t" and end with "y".

 Please write a function that takes two strings as parameters, one string like
 "technology" and one pattern like "t8y", and returns a boolean indicating whether
 the given pattern matches the given string.

"""

import re


def match_pattern(input_str: str = "", input_pattern: str = ""):
    """
    match pattern against the input string and return True or False
    """

    tokenized_pattern = []

    def expand_pattern(value: str = ""):
        if value.isdigit():
            tokenized_pattern.extend(['-1'] * int(value))
        else:
            tokenized_pattern.extend(list(value))

    # Splitting text and number in string
    # pattern = "Ins15on", Split result = ['Ins', '15', 'on']
    split_pattern = re.findall(r'[A-Za-z]+|\d+', input_pattern)

    # Given input pattern = "Ins15on"
    # result is ['I', 'n', 's', '-1', '-1', '-1', '-1', '-1', '-1',
    # '-1', '-1', '-1', '-1', '-1', '-1', '-1', '-1', '-1', 'o', 'n']
    # pylint: disable=expression-not-assigned
    [expand_pattern(x) for x in split_pattern]

    # If input string and deduced pattern length do not match then the
    # pattern is not a match for the string.
    if len(input_str) != len(tokenized_pattern):
        return False

    # Match each letter with its position to each letter and its deduced
    # position in the pattern. It should be exact match for the pattern to
    # be considered a match for the word.
    return all([1 if a == b else 0 for a, b in
                zip(list(input_str), tokenized_pattern) if b != '-1'])


if __name__ == "__main__":

    print(match_pattern())  # True
    print(match_pattern("Institutionalization", "Ins15on"))  # True
    print(match_pattern("Institutionalization", "ins15on"))  # False
    print(match_pattern("Institutionalization", "Ins14on"))  # False
    print(match_pattern("Institutionalization", "Ins15ns"))  # False
    print(match_pattern("Institutionalization", "I18n"))  # True
    print(match_pattern("Institutionalization", "12liz4n"))  # True
