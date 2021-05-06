from collections import Counter
def minSubstringWithAllChars(s, t):
    if len(t) == 0: return ""
    m = Counter(t)
    begin = 0
    end = 0
    r = 1000000000
    ans = 0
    missing = len(m) 
    while end < len(s):
        temp = s[end]
        if temp in m:
            m[temp] -= 1
            if m[temp] == 0: missing -= 1
        end += 1
        
        while missing == 0:
            temp1 = s[begin]
            if temp1 in m:
                m[temp1] += 1
                if m[temp1] > 0: missing += 1
            if end - begin < r:
                r = end - begin
                ans = begin
            begin += 1
    return s[ans : ans + r]
    