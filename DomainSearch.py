from RootDomain import RootDomain

def hard_match(word, tld):
    return word.endswith(tld)

def validate_length(word, tld):
    return len(word) > len(tld) + 3

def remove_last_vowel(word, tld):
    VOWELS = ["a", "e", "i", "o", "u", "y"]
    if word[-2:-1] in VOWELS and word[-3:-2] == tld[0]:
        return True

    return False

def replace_dbl_letters(word):
    results = []
    doubles = [c for c in set(list(word)) if c + c in word]
    for c in doubles:
        _temp = word
        while c + c in _temp:
            head, _sep, tail = _temp.partition(c + c)
            rhead, _rsep, rtail = _temp.rpartition(c + c)
            _temp = head + c + tail
            _rtemp = rhead + c + rtail
            results.extend(set([_temp, _rtemp]))

    return results

def soft_match(word, tld):
    return remove_last_vowel(word, tld)

def verify_domain(word, tld):
    if word is not None:
        if hard_match(word, tld) or soft_match(word, tld):
            return True

    return False

def verify_domains(names, tld):
    results = []

    for name in names:
        root_domain = RootDomain(name, tld)
        results.extend(root_domain.possible_fullnames)

    return results