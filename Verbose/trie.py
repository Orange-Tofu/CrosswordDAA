# noinspection PyShadowingNames
class Trie:
    def __init__(self, is_end=False):
        self.children = {}
        self.is_end = is_end

    def insert(self, s):
        node = self
        for ch in s:
            if ch not in node.children:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.is_end = True

    def build(self, words):
        for word in words:
            self.insert(word)
        return self

    def search(self, s):
        node = self
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node if node.is_end else None

    def delete(self, s):
        def rec(node, s, i):
            if i == len(s):
                node.is_end = False
                return len(node.children) == 0
            else:
                next_deletion = rec(node.children[s[i]], s, i+1)
                if next_deletion:
                    del node.children[s[i]]
                return next_deletion and not node.is_end and len(node.children) == 0
        if self.search(s):
            rec(self, s, 0)

    def get_strings(self):
        def rec(node, string, strings):
            if node.is_end:
                strings.append("".join(string))
            for ch in node.children:
                string.append(ch)
                rec(node.children[ch], string, strings)
                string.pop()
        strings = []
        rec(self, [], strings)
        return strings