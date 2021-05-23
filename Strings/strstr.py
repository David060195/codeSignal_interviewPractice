def strstr(s, x):
    if not x: return 0
    sHash, xHash, h, d, q = 0, 0, 1, 256, 97
    for _ in range(len(x) - 1):
        h  = (h * d) % q
    for i in range(len(x)):
        sHash = (sHash * d + ord(s[i])) % q
        xHash = (xHash * d + ord(x[i])) % q
    if sHash == xHash and s[:len(x)] == x: return 0
    for i in range(len(x), len(s)):
        sHash = (d * (sHash - h * ord(s[i - len(x)])) + ord(s[i])) % q
        if sHash == xHash and x == s[i - len(x) + 1 : i + 1]:
            return i - len(x) + 1
    return -1