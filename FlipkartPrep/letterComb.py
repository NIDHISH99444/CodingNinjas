def letterCombinations( digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if digits == "":
        return []
    res = ['']
    dictionary = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    for i in digits:
        temp = []
        for j in dictionary[i]:
            for k in range(len(res)):
                temp.append(res[k] + j)
        res = temp
    return res

print(letterCombinations("232"))