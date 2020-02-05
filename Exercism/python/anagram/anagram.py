from typing import List


def find_anagrams(word: str, candidates: List[str]) -> List[str]:
    """
    Check if there are anagrams for the given candidates

    :param
    word: str
    candidates: List[str]

    :return:
    anagrams: List[str
    """
    matches = list()

    for item in candidates:
        if item.lower() != word.lower() and sorted(item.lower()) == sorted(word.lower()):
            matches.append(item)

    return matches
