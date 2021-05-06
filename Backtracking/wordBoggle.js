class Node {
    constructor() {
        this.children = {}
        this.isEnd = false
    }
}
class Trie {
    constructor() {
        this.root = new Node()
    }
    addWord(word) {
        let current = this.root
        for(const char of word) {
            if(!(char in current.children)) {
                current.children[char] = new Node()
            }
            current = current.children[char]
        }
        current.isEnd = true
    }
    search(word) {
        let current = this.root
        for(const char of word) {
            if(char in current.children) {
                current = current.children[char]
            } else {
                return false
            }
        }
        return current.isEnd
    }
    searchWithPrefix(word) {
        let current = this.root
        for(const char of word) {
            if(char in current.children) {
                current = current.children[char]
            } else {
                return false
            }
        }
        return true
    }
}
findWordBoard = (board, ans, node, curWord, [x, y], m, n, visited) => {
    if(node.search(curWord)) {
        ans.add(curWord)
    }
    visited[x][y] = true
    for(const [di, dj] of [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]) {
        const dx = x + di
        const dy = y + dj
        if(dx >= 0 && dx < m && dy >= 0 && dy < n && !visited[dx][dy] && node.searchWithPrefix(curWord + board[dx][dy])) {
            findWordBoard(board, ans, node, curWord + board[dx][dy], [dx, dy], m, n, visited)
        }
    }
    visited[x][y] = false
}
wordBoggle = (board, words) => {
    const [m, n] = [board.length, board[0].length]
    if(!m || !n) return [] 
    const trie = new Trie()
    let ans = new Set()
    for(const word of words) { trie.addWord(word) }
    const visited = [...new Array(m)].map(() => new Array(n).fill(false))
    for(let i = 0; i < m; i++) {
        for(let j = 0; j < n; j++) {
            if(trie.searchWithPrefix(board[i][j])) {
                findWordBoard(board, ans, trie, board[i][j], [i, j], m, n, visited)
            }
        }
    }
    return [...ans].sort()
}