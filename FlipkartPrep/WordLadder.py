from collections import deque
def WordLadder(beginWord, endWord, wordList):
    wordList=set(wordList)
    if endWord not in wordList:
        return 0
    step=1
    q=deque()
    q.append((beginWord,step))

    while q:
        word,step=q.popleft()
        if word==endWord:
            return step
        for i in range(len(word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                newWord=word[:i]+char+word[i+1:]
                if newWord in wordList:
                    wordList.remove(newWord)
                    q.append((newWord,step+1))
    return 0







print(WordLadder("hit","cog",["hot","dot","dog","lot","log","cog"]))