# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
from collections import defaultdict
def topKFrequent( words, k) :
    freq = {}
    for word in words:
        if word not in freq:
            freq[word]=1
        else:
            freq[word]+=1
    frequencies = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    res=[]
    for i,(key,_) in enumerate(frequencies):
        if i<k:
            res.append(key)
    return res

print(topKFrequent(["i", "love", "leetcode", "i", "love", "coding"],2))