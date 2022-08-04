from trie import Trie


def check(grid, trie, i, j, i_diff, j_diff, moves):
    n, m = len(grid), len(grid[0])
    node = trie
    start_i, start_j = i, j
    substring = ''
    while 0 <= i < n and 0 <= j < m and grid[i][j] in node.children:
        substring += grid[i][j]
        node = node.children[grid[i][j]]
        if node.is_end:
            moves.append(((start_i + 1, start_j + 1), (i + 1, j + 1)))
            trie.delete(substring)
        i += i_diff
        j += j_diff


def solve(grid, words):
    moves = []
    trie = Trie().build(words)
    n, m = len(grid), len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j] in trie.children:
                for i_diff, j_diff in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                    check(grid, trie, i, j, i_diff, j_diff, moves)
    return moves


if __name__ == '__main__':
    with open('grid.txt', 'r') as f:
        grid = []
        for i in range(15):
            line = f.readline().strip("\n").split()
            grid.append(line)
    with open('wordlist.txt', 'r') as f2:
        word = []
        for i in range(10):
            word.append(f2.readline().strip('\n').upper())
        words = set(word)
    move = solve(grid, words)
    print(move)
