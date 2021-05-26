def repeatedDNASequences(s):
    seen, ans = set(), []
    for i in range(len(s)):
        curString = s[i : 10 + i]
        if len(curString) == 10 and curString in seen and curString not in ans:
            ans.append(curString)
        seen.add(curString)
    return sorted(ans)