def wordBreak( s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: List[str]
    """

    trie = {}
    for word in wordDict:
        node = trie
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['#'] = 1

    graph = {}
    to_check = [0]
    while to_check:
        i = to_check.pop()
        if i in graph:
            continue
        node = trie
        row = []
        start = i
        while i < len(s) and s[i] in node:
            node = node[s[i]]
            i += 1
            if '#' in node:
                row.append(i)
                to_check.append(i)
        graph[start] = row

    memo = {len(s): [[]]}
    for i in range(len(s) - 1, -1, -1):
        if i in graph:
            res = []
            for k in graph[i]:
                if k in memo:

                    for tail in memo[k]:
                        res.append([s[i:k]] + tail)
            memo[i] = res

    return [' '.join(words) for words in memo[0]]

s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
print(wordBreak(s,wordDict))

