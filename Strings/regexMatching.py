def regexMatching(pattern, test):
    if pattern[0] == '^':
        a = pattern[1 :]
        b = len(a)
        if test[: b] == a: return True
        return False
    if pattern[-1] == '$':
        a = pattern[: -1]
        b = len(a)
        if test[-b :] == a: return True
        return False
    else:
        a = test.find(pattern)
        if a != -1: return True
        return False