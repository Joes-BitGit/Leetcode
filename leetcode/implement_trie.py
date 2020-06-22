# DESCRIPTION
# Implement a trie with insert, search, and startsWith methods.

# EXAMPLE:
# Trie trie = new Trie();

# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");
# trie.search("app");     // returns true

# Note:
# You may assume that all inputs consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.

class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.complete = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        Time: O(N), where N is the len of the word
        Space: O(N), where N is the len of the word
        """
        node = self.root

        for i in word:

            if node.children[ord(i)-ord('a')] == None:
                node.children[ord(i)-ord('a')] = TrieNode()

            node = node.children[ord(i)-ord('a')]

        node.complete = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        Time: O(N), N is the len of word
        Space: O(1), no extra space
        """
        node = self.root

        for i in word:

            if node.children[ord(i)-ord('a')] == None:
                return False
            node = node.children[ord(i)-ord('a')]

        return node.complete

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        Time: O(N), N is the len of prefix
        Space: O(1)
        """
        node = self.root

        for i in prefix:

            if node.children[ord(i)-ord('a')] == None:
                return False
            node = node.children[ord(i)-ord('a')]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
