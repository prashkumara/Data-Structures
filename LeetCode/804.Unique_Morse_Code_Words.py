def uniqueMorseRepresentations(self, words):
    """
    :type words: List[str]
    :rtype: int
    """
    hashmap = {
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--.."
    }

    sets = set()
    for w in words:
        st = ""
        print(w)
        for s in w:
            st = st + hashmap[s]
        sets.add(st)
    return len(sets)