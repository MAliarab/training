from typing import List


def misras_gries(array: List[int], k: int = 2):

    keys = {}
    for item in array:
        val = str(item)
        if val in keys:
            keys[val] += 1
        elif len(keys) < k - 1:
            keys[val] = 1
        else:
            for key in list(keys):
                keys[key] -= 1
                if keys[key] == 0:
                    del keys[key]

    suspects = keys.keys()
    frequencies = {}
    for suspect in suspects:
        freq = _count_frequency(array, int(suspect))
        if freq >= len(array) / k:
            frequencies[suspect] = freq

    return frequencies if len(frequencies) > 0 else None


def _count_frequency(array: List[int], element: int):
    return array.count(element)


# Test cases
print(misras_gries([1, 4, 4, 4, 5, 4, 4]))
print(misras_gries([0, 0, 0, 1, 1, 1, 1]))
print(misras_gries([0, 0, 0, 0, 1, 1, 1, 2, 2], 3))
