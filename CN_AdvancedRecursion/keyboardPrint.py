hashTable = [" ", " ", "abc", "def", "ghi", "jkl",
             "mno", "pqrs", "tuv", "wxyz"]


def printWordsUtil(number, curr, output, n):
    if (curr == n):
        print("".join(output))
        return

    for i in range(len(hashTable[number[curr]])):
        output.append(hashTable[number[curr]][i])
        printWordsUtil(number, curr + 1, output, n)
        output.pop()
        if (number[curr] == 0 or number[curr] == 1):
            return;

def printWords(number, n):
    printWordsUtil(number, 0, [], n)

number=input()
arr=[int(x) for x in number]
n=len(arr)
printWords(arr, n)


