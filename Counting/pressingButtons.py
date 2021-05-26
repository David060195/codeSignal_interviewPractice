def pressingButtons(buttons):
    numbers = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}
    words = [list(numbers[i]) for i in buttons]
    if len(buttons) == 0: return []
    ans = []
    dfs(ans, [], 0, words)
    return ans

def dfs(ans, temp, index, words):
    if index == len(words): 
        ans.append(''.join(temp.copy()))
    else:
        for i in range(len(words[index])):
            temp.append(words[index][i])
            dfs(ans, temp, index + 1, words)
            temp.pop()
