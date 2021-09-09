class RootDomain:

    def __init__(self, word, tld):
        self.tld = tld.strip()
        self.basename = word.strip()
        self.fullname = f"{self.basename}.{self.tld}"
        self.alternatives = self.create_alternatives([self.basename], True, 0)
        self.possible_fullnames = [self.create_fullname(n) for n in self.alternatives]
        
    def get_fullnames_for_alts(self):
        names = set([
            self.create_fullname(x) for
            x in self.alternatives
        ])
        
        return names

    def create_fullname(self, name=""):
        name = name if name else self.basename
        if len(name) > len(self.tld) and name.endswith(self.tld):
            return f"{name[:-len(self.tld)]}.{self.tld}"
        if len(name) > len(self.tld) and name.endswith(self.tld[0]):
            return f"{name[:-1]}.{self.tld}"
            
        return name + "." + self.tld
    
    def create_alternatives(self, alts=[], changed=False, start=0):

        if not changed:
            return set(alts)
        
        if changed:
            changed = False
            for n in alts[start:]:
                _temp = [
                    self.remove_dbl_chars(n),
                    self.remove_last_dbl(n),
                    self.remove_all_vowels(n),
                    self.remove_last_vowel(n)
                ]
                if any(_temp):
                    alts.extend(list(filter(lambda x: x and x not in alts, _temp)))
                    changed=True
                    start += 1
                    
        return self.create_alternatives(alts, changed, start)

    def tld_at_end(self, name=""):
        name = name if name else self.basename
        if name.endswith(self.tld):
            _temp = f"{name[:-len(self.tld)]}.{self.tld}"
            return _temp
            
        return False

    def remove_dbl_chars(self, name=""):
        result = name if name else self.basename
        dbls = [c + c for c in self.basename]
        for d in dbls:
            result = result.replace(d, d[0])
        if result != name:
            return result
        else:
            return False

    def remove_last_dbl(self, name=""):
        result = name if name else self.basename
        if result.endswith(result[-1] + result[-1]):
            return result[:-1]
        else:
            return False

    def remove_all_vowels(self, name=""):
        VOWELS = ["a", "e", "i", "o", "u", "y"]
        result = name if name else self.basename
        for v in VOWELS:
            result = result.replace(v, "")
        if result != name:
            return result
        else:
            return False

    def remove_last_vowel(self, name=""):
        name = name if name else self.basename
        VOWELS = ["a", "e", "i", "o", "u", "y"]
        for i in range(len(name) - 1, 0, -1):
            if name[i] in VOWELS:
                return name[:i] + name[i + 1:]

        return False