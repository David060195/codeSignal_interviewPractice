def stringPermutations(s):
    def dfs(s, index, ans):
        if index == len(s):
            ans.append(''.join(s))
        else:
            for i in range(index, len(s)):
                s[index], s[i] = s[i], s[index]
                dfs(s, index + 1, ans)
                s[i], s[index] = s[index], s[i]
    s = list(s)
    ans = []
    dfs(s, 0, ans)
    return sorted(set(ans))
