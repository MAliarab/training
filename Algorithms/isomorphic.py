"""
Check if two strings are isomorphic or not
"""


def is_isomorphic(st1, st2):
    if len(st1) != len(st2):
        return False

    char_match = {}
    passed_chars = set()

    for i in range(len(st1)):
        if not st1[i] in char_match:
            if st2[i] in passed_chars:
                return False

            char_match[st1[i]] = st2[i]
            passed_chars.add(st2[i])

        elif char_match[st1[i]] != st2[i]:
            return False

    return True


# Test cases
print(is_isomorphic("paper", "title"))  # -> True
print(is_isomorphic("egg", "add"))  # -> True
print(is_isomorphic("bar", "foo"))  # -> False
