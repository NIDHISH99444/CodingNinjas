def generateParanthesis(n):

    generate(n,str="",open=0,close=0)


def generate(n,str="",open=0,close=0):
    if len(str)==2*n:
        print(str)
    if open <n:
        generate(n, str+"(", open+1, close)
    if close<open:
        generate(n, str + ")", open, close+1)
print(generateParanthesis(3))

